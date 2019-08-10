import logging
import math
import time

import numpy as np
from scipy import signal
from scipy.interpolate import PchipInterpolator

ADJUST_BY_3DB = 1 / (2 ** 0.5)
# 1 micro m/s2 in G produces 0dB means 1G = ~140dB, 0.1G = ~120dB, 0.01G = ~100dB, 0.001G = ~80dB and 0.0001G = ~60dB
REF_ACCELERATION_IN_G = (10 ** -6) / 9.80665
X_RESOLUTION = 32769

logger = logging.getLogger('qvibe.signal')


class TriAxisSignal:

    def __init__(self, preferences, data, fs, resolution_shift, pre_calc=False):
        self.__x = Signal(preferences, data[:, 2], fs, resolution_shift, pre_calc=pre_calc)
        self.__y = Signal(preferences, data[:, 3], fs, resolution_shift, pre_calc=pre_calc)
        self.__z = Signal(preferences, data[:, 4], fs, resolution_shift, pre_calc=pre_calc)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    def recalc(self):
        self.x.recalc()
        self.y.recalc()
        self.z.recalc()


class Analysis:
    def __init__(self, values):
        self.__x = values[0]
        self.__y = values[1]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Signal:

    def __init__(self, preferences, data, fs, resolution_shift, mode='vibration', pre_calc=False):
        '''
        Creates a new signal.
        :param preferences: common prefs.
        :param data: the sample date.
        :param fs: the sample rate.
        :param resolution_shift: the analysis frequency resolution.
        :param mode: optional analysis mode, can be none (raw data), vibration or tilt.
        :param pre_calc: if True, calculate the required views.
        '''
        self.__preferences = preferences
        if mode == 'vibration':
            self.__data = butter(fs, data, 'high')
        elif mode == 'tilt':
            self.__data = butter(fs, data, 'low')
        else:
            self.__data = data
        self.__fs = fs
        self.__resolution_shift = resolution_shift
        avg = self.__calculate_avg() if pre_calc is True else None
        self.__output = {
            'avg': avg
        }

    def recalc(self):
        self.__output['avg'] = self.__calculate_avg()

    @property
    def avg(self):
        ''' The x-y data for the avg spectrum. '''
        return self.__output['avg']

    @property
    def fs(self):
        return self.__fs

    def __calculate_avg(self):
        from model.preferences import ANALYSIS_RESOLUTION, ANALYSIS_AVG_WINDOW
        resolution = self.__preferences.get(ANALYSIS_RESOLUTION)
        resolution_shift = int(math.log(resolution, 2))
        # peak_wnd = self.__get_window(self.__preferences, ANALYSIS_PEAK_WINDOW)
        avg_wnd = get_window(self.__preferences, ANALYSIS_AVG_WINDOW)
        avg = self.avg_spectrum(resolution_shift=resolution_shift, window=avg_wnd, average='mean')
        # self.__peak = self.peak_spectrum(resolution_shift=resolution_shift, window=peak_wnd)
        return Analysis(avg)

    def avg_spectrum(self, ref=REF_ACCELERATION_IN_G, resolution_shift=0, window=None, **kwargs):
        """
        analyses the source to generate the linear spectrum.
        :param ref: the reference value for dB purposes.
        :param resolution_shift: allows resolution to go down (if positive) or up (if negative).
        :param mode: cq or none.
        :return:
            f : ndarray
            Array of sample frequencies.
            Pxx : ndarray
            linear spectrum.
        """
        nperseg = get_segment_length(self.fs, resolution_shift=resolution_shift)
        f, Pxx_spec = signal.welch(self.__data, self.fs, nperseg=nperseg, scaling='spectrum', detrend=False,
                                   window=window if window else 'hann', **kwargs)
        # a 3dB adjustment is required to account for the change in nperseg
        Pxx_spec = amplitude_to_db(np.nan_to_num(np.sqrt(Pxx_spec)), ADJUST_BY_3DB * REF_ACCELERATION_IN_G)
        return f, Pxx_spec
        # return rescale_x(f, Pxx_spec)


def butter(fs, data, btype, f3=2, order=2):
    """
    Applies a digital butterworth filter via filtfilt at the specified f3 and order. Default values are set to
    correspond to apparently sensible filters that distinguish between vibration and tilt from an accelerometer.
    :param data: the data to filter.
    :param btype: high or low.
    :param f3: the f3 of the filter.
    :param order: the filter order.
    :return: the filtered signal.
    """
    b, a = signal.butter(order, f3 / (0.5 * fs), btype=btype)
    y = signal.filtfilt(b, a, data)
    return y


def get_window(preferences, key):
    '''
    Gets the preferred window for the given type with a default fallback if no preference is set.
    :param preferences: the preferences store.
    :param key: the preferences key.
    :return: the window.
    '''
    from model.preferences import ANALYSIS_WINDOW_DEFAULT
    window = preferences.get(key)
    if window is None or window == ANALYSIS_WINDOW_DEFAULT:
        window = None
    else:
        if window == 'tukey':
            window = (window, 0.25)
    return window


def amplitude_to_db(s, ref=1.0):
    '''
    Convert an amplitude spectrogram to dB-scaled spectrogram. Implementation taken from librosa to avoid adding a
    dependency on librosa for a few util functions.
    :param s: the amplitude spectrogram.
    :return: s_db : np.ndarray ``s`` measured in dB
    '''
    magnitude = np.abs(np.asarray(s))
    power = np.square(magnitude, out=magnitude)
    ref_power = np.abs(ref ** 2)
    amin = 1e-20
    top_db = 80.0
    log_spec = 10.0 * np.log10(np.maximum(amin, power))
    log_spec -= 10.0 * np.log10(np.maximum(amin, ref_power))
    log_spec = np.maximum(log_spec, log_spec.max() - top_db)
    return log_spec


def rescale_x(x, y):
    step = (x[-1] - x[0]) / X_RESOLUTION
    steps = np.arange(x[0], x[-1], step)
    if len(steps) == len(x):
        return x, y
    else:
        import time
        start = time.time()
        x2, y2 = interp(x, y, steps)
        end = time.time()
        logger.debug(f"Interpolation from {len(x)} to {len(x2)} in {round((end - start) * 1000, 3)}ms")
        return x2, y2


def interp(x1, y1, x2, smooth=False):
    ''' Interpolates xy based on the preferred smoothing style. '''
    start = time.time()
    if smooth is True:
        cs = PchipInterpolator(x1, y1)
        y2 = cs(x2)
    else:
        y2 = np.interp(x2, x1, y1)
    end = time.time()
    logger.debug(f"Interpolation from {len(x1)} to {len(x2)} in {round((end - start) * 1000, 3)}ms")
    return x2, y2


def get_segment_length(fs, resolution_shift=0):
    """
    Calculates a segment length such that the frequency resolution of the resulting analysis is in the region of
    ~1Hz subject to a lower limit of the number of samples in the signal.
    For example, if we have a 10s signal with an fs is 500 then we convert fs-1 to the number of bits required to
    hold this number in binary (i.e. 111110011 so 9 bits) and then do 1 << 9 which gives us 100000000 aka 512. Thus
    we have ~1Hz resolution.
    :param resolution_shift: shifts the resolution up or down by the specified number of bits.
    :return: the segment length.
    """
    return 1 << ((fs - 1).bit_length() - int(resolution_shift))
