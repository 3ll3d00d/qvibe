# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 679)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.chartControlLayout = QtWidgets.QVBoxLayout()
        self.chartControlLayout.setObjectName("chartControlLayout")
        self.chartControlsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chartControlsLabel.setFont(font)
        self.chartControlsLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.chartControlsLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.chartControlsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chartControlsLabel.setObjectName("chartControlsLabel")
        self.chartControlLayout.addWidget(self.chartControlsLabel)
        self.activeRecordersLabel = QtWidgets.QLabel(self.centralwidget)
        self.activeRecordersLabel.setObjectName("activeRecordersLabel")
        self.chartControlLayout.addWidget(self.activeRecordersLabel)
        self.activeRecorders = QtWidgets.QListWidget(self.centralwidget)
        self.activeRecorders.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.activeRecorders.setObjectName("activeRecorders")
        self.chartControlLayout.addWidget(self.activeRecorders)
        self.visibleCurvesLabel = QtWidgets.QLabel(self.centralwidget)
        self.visibleCurvesLabel.setObjectName("visibleCurvesLabel")
        self.chartControlLayout.addWidget(self.visibleCurvesLabel)
        self.visibleCurves = QtWidgets.QListWidget(self.centralwidget)
        self.visibleCurves.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.visibleCurves.setResizeMode(QtWidgets.QListView.Fixed)
        self.visibleCurves.setObjectName("visibleCurves")
        item = QtWidgets.QListWidgetItem()
        self.visibleCurves.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.visibleCurves.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.visibleCurves.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.visibleCurves.addItem(item)
        self.chartControlLayout.addWidget(self.visibleCurves)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.chartControlLayout.addItem(spacerItem)
        self.extraControlsLayout = QtWidgets.QGridLayout()
        self.extraControlsLayout.setObjectName("extraControlsLayout")
        self.fps = QtWidgets.QSpinBox(self.centralwidget)
        self.fps.setMinimum(1)
        self.fps.setMaximum(50)
        self.fps.setProperty("value", 20)
        self.fps.setObjectName("fps")
        self.extraControlsLayout.addWidget(self.fps, 5, 1, 1, 1)
        self.resolutionHzLabel = QtWidgets.QLabel(self.centralwidget)
        self.resolutionHzLabel.setObjectName("resolutionHzLabel")
        self.extraControlsLayout.addWidget(self.resolutionHzLabel, 3, 0, 1, 1)
        self.bufferSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.bufferSizeLabel.setObjectName("bufferSizeLabel")
        self.extraControlsLayout.addWidget(self.bufferSizeLabel, 4, 0, 1, 1)
        self.magMin = QtWidgets.QSpinBox(self.centralwidget)
        self.magMin.setMaximum(150)
        self.magMin.setObjectName("magMin")
        self.extraControlsLayout.addWidget(self.magMin, 2, 1, 1, 1)
        self.freqLayout = QtWidgets.QHBoxLayout()
        self.freqLayout.setObjectName("freqLayout")
        self.freqMin = QtWidgets.QSpinBox(self.centralwidget)
        self.freqMin.setMinimum(1)
        self.freqMin.setMaximum(1000)
        self.freqMin.setObjectName("freqMin")
        self.freqLayout.addWidget(self.freqMin)
        self.freqMax = QtWidgets.QSpinBox(self.centralwidget)
        self.freqMax.setMinimum(1)
        self.freqMax.setMaximum(1000)
        self.freqMax.setObjectName("freqMax")
        self.freqLayout.addWidget(self.freqMax)
        self.extraControlsLayout.addLayout(self.freqLayout, 0, 1, 1, 1)
        self.fpsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsLabel.setObjectName("fpsLabel")
        self.extraControlsLayout.addWidget(self.fpsLabel, 5, 0, 1, 1)
        self.resolutionHz = QtWidgets.QComboBox(self.centralwidget)
        self.resolutionHz.setObjectName("resolutionHz")
        self.resolutionHz.addItem("")
        self.resolutionHz.addItem("")
        self.resolutionHz.addItem("")
        self.resolutionHz.addItem("")
        self.resolutionHz.addItem("")
        self.extraControlsLayout.addWidget(self.resolutionHz, 3, 1, 1, 1)
        self.actualFPS = QtWidgets.QSpinBox(self.centralwidget)
        self.actualFPS.setEnabled(False)
        self.actualFPS.setMaximum(120)
        self.actualFPS.setObjectName("actualFPS")
        self.extraControlsLayout.addWidget(self.actualFPS, 6, 1, 1, 1)
        self.bufferSize = QtWidgets.QSpinBox(self.centralwidget)
        self.bufferSize.setMinimum(1)
        self.bufferSize.setMaximum(240)
        self.bufferSize.setProperty("value", 30)
        self.bufferSize.setObjectName("bufferSize")
        self.extraControlsLayout.addWidget(self.bufferSize, 4, 1, 1, 1)
        self.actualFPSLabel = QtWidgets.QLabel(self.centralwidget)
        self.actualFPSLabel.setObjectName("actualFPSLabel")
        self.extraControlsLayout.addWidget(self.actualFPSLabel, 6, 0, 1, 1)
        self.magRangeLabel = QtWidgets.QLabel(self.centralwidget)
        self.magRangeLabel.setObjectName("magRangeLabel")
        self.extraControlsLayout.addWidget(self.magRangeLabel, 1, 0, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.extraControlsLayout.addWidget(self.label, 7, 0, 1, 1)
        self.elapsedTime = QtWidgets.QTimeEdit(self.centralwidget)
        self.elapsedTime.setReadOnly(True)
        self.elapsedTime.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.elapsedTime.setObjectName("elapsedTime")
        self.extraControlsLayout.addWidget(self.elapsedTime, 7, 1, 1, 1)
        self.freqLabel = QtWidgets.QLabel(self.centralwidget)
        self.freqLabel.setObjectName("freqLabel")
        self.extraControlsLayout.addWidget(self.freqLabel, 0, 0, 1, 1)
        self.magMax = QtWidgets.QSpinBox(self.centralwidget)
        self.magMax.setMaximum(150)
        self.magMax.setProperty("value", 150)
        self.magMax.setObjectName("magMax")
        self.extraControlsLayout.addWidget(self.magMax, 1, 1, 1, 1)
        self.chartControlLayout.addLayout(self.extraControlsLayout)
        self.chartControlLayout.setStretch(2, 2)
        self.chartControlLayout.setStretch(4, 1)
        self.chartControlLayout.setStretch(5, 1)
        self.mainLayout.addLayout(self.chartControlLayout)
        self.chartLayout = QtWidgets.QGridLayout()
        self.chartLayout.setContentsMargins(-1, -1, 0, -1)
        self.chartLayout.setObjectName("chartLayout")
        self.chartTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.chartTabs.setObjectName("chartTabs")
        self.vibrationTab = QtWidgets.QWidget()
        self.vibrationTab.setObjectName("vibrationTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.vibrationTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.liveVibrationChart = PlotWidgetWithDateAxis(self.vibrationTab)
        self.liveVibrationChart.setMidLineWidth(0)
        self.liveVibrationChart.setObjectName("liveVibrationChart")
        self.gridLayout_3.addWidget(self.liveVibrationChart, 1, 0, 1, 2)
        self.vibrationAnalysis = QtWidgets.QComboBox(self.vibrationTab)
        self.vibrationAnalysis.setObjectName("vibrationAnalysis")
        self.vibrationAnalysis.addItem("")
        self.vibrationAnalysis.addItem("")
        self.vibrationAnalysis.addItem("")
        self.gridLayout_3.addWidget(self.vibrationAnalysis, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.chartTabs.addTab(self.vibrationTab, "")
        self.rtaTab = QtWidgets.QWidget()
        self.rtaTab.setObjectName("rtaTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.rtaTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rtaChart = PlotWidgetForSpectrum(self.rtaTab)
        self.rtaChart.setObjectName("rtaChart")
        self.gridLayout_2.addWidget(self.rtaChart, 1, 0, 1, 1)
        self.rtaControlsLayout = QtWidgets.QHBoxLayout()
        self.rtaControlsLayout.setObjectName("rtaControlsLayout")
        self.rtaAverageLabel = QtWidgets.QLabel(self.rtaTab)
        self.rtaAverageLabel.setObjectName("rtaAverageLabel")
        self.rtaControlsLayout.addWidget(self.rtaAverageLabel)
        self.rtaAverage = QtWidgets.QComboBox(self.rtaTab)
        self.rtaAverage.setObjectName("rtaAverage")
        self.rtaAverage.addItem("")
        self.rtaAverage.addItem("")
        self.rtaAverage.addItem("")
        self.rtaAverage.addItem("")
        self.rtaControlsLayout.addWidget(self.rtaAverage)
        self.rtaViewLabel = QtWidgets.QLabel(self.rtaTab)
        self.rtaViewLabel.setObjectName("rtaViewLabel")
        self.rtaControlsLayout.addWidget(self.rtaViewLabel)
        self.rtaView = QtWidgets.QComboBox(self.rtaTab)
        self.rtaView.setObjectName("rtaView")
        self.rtaView.addItem("")
        self.rtaView.addItem("")
        self.rtaView.addItem("")
        self.rtaControlsLayout.addWidget(self.rtaView)
        self.smoothRta = QtWidgets.QCheckBox(self.rtaTab)
        self.smoothRta.setObjectName("smoothRta")
        self.rtaControlsLayout.addWidget(self.smoothRta)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rtaControlsLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.rtaControlsLayout, 0, 0, 1, 1)
        self.chartTabs.addTab(self.rtaTab, "")
        self.spectrogramTab = QtWidgets.QWidget()
        self.spectrogramTab.setObjectName("spectrogramTab")
        self.gridLayout = QtWidgets.QGridLayout(self.spectrogramTab)
        self.gridLayout.setObjectName("gridLayout")
        self.spectrogramView = GraphicsLayoutWidget(self.spectrogramTab)
        self.spectrogramView.setObjectName("spectrogramView")
        self.gridLayout.addWidget(self.spectrogramView, 0, 0, 1, 1)
        self.chartTabs.addTab(self.spectrogramTab, "")
        self.chartLayout.addWidget(self.chartTabs, 0, 0, 1, 1)
        self.mainLayout.addLayout(self.chartLayout)
        self.addRecorderLayout = QtWidgets.QVBoxLayout()
        self.addRecorderLayout.setContentsMargins(0, -1, -1, -1)
        self.addRecorderLayout.setObjectName("addRecorderLayout")
        self.configHeaderLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.configHeaderLabel.setFont(font)
        self.configHeaderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.configHeaderLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.configHeaderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.configHeaderLabel.setObjectName("configHeaderLabel")
        self.addRecorderLayout.addWidget(self.configHeaderLabel)
        self.targetConfigLayout = QtWidgets.QGridLayout()
        self.targetConfigLayout.setObjectName("targetConfigLayout")
        self.accelerometerLabel = QtWidgets.QLabel(self.centralwidget)
        self.accelerometerLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.accelerometerLabel.setObjectName("accelerometerLabel")
        self.targetConfigLayout.addWidget(self.accelerometerLabel, 2, 0, 1, 1)
        self.targetBatchSize = QtWidgets.QSpinBox(self.centralwidget)
        self.targetBatchSize.setMinimum(1)
        self.targetBatchSize.setMaximum(100)
        self.targetBatchSize.setProperty("value", 50)
        self.targetBatchSize.setObjectName("targetBatchSize")
        self.targetConfigLayout.addWidget(self.targetBatchSize, 1, 1, 1, 1)
        self.targetAccelerometerLayout = QtWidgets.QVBoxLayout()
        self.targetAccelerometerLayout.setObjectName("targetAccelerometerLayout")
        self.targetAccelEnabled = QtWidgets.QCheckBox(self.centralwidget)
        self.targetAccelEnabled.setChecked(True)
        self.targetAccelEnabled.setObjectName("targetAccelEnabled")
        self.targetAccelerometerLayout.addWidget(self.targetAccelEnabled)
        self.targetAccelSens = QtWidgets.QComboBox(self.centralwidget)
        self.targetAccelSens.setObjectName("targetAccelSens")
        self.targetAccelSens.addItem("")
        self.targetAccelSens.addItem("")
        self.targetAccelSens.addItem("")
        self.targetAccelSens.addItem("")
        self.targetAccelerometerLayout.addWidget(self.targetAccelSens)
        self.targetConfigLayout.addLayout(self.targetAccelerometerLayout, 2, 1, 1, 1)
        self.gyroLabel = QtWidgets.QLabel(self.centralwidget)
        self.gyroLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gyroLabel.setObjectName("gyroLabel")
        self.targetConfigLayout.addWidget(self.gyroLabel, 3, 0, 1, 1)
        self.targetGyroLayout = QtWidgets.QVBoxLayout()
        self.targetGyroLayout.setObjectName("targetGyroLayout")
        self.targetGyroEnabled = QtWidgets.QCheckBox(self.centralwidget)
        self.targetGyroEnabled.setObjectName("targetGyroEnabled")
        self.targetGyroLayout.addWidget(self.targetGyroEnabled)
        self.targetGyroSens = QtWidgets.QComboBox(self.centralwidget)
        self.targetGyroSens.setObjectName("targetGyroSens")
        self.targetGyroSens.addItem("")
        self.targetGyroSens.addItem("")
        self.targetGyroSens.addItem("")
        self.targetGyroSens.addItem("")
        self.targetGyroLayout.addWidget(self.targetGyroSens)
        self.targetConfigLayout.addLayout(self.targetGyroLayout, 3, 1, 1, 1)
        self.targetBatchSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.targetBatchSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.targetBatchSizeLabel.setObjectName("targetBatchSizeLabel")
        self.targetConfigLayout.addWidget(self.targetBatchSizeLabel, 1, 0, 1, 1)
        self.resetTargetButton = QtWidgets.QToolButton(self.centralwidget)
        self.resetTargetButton.setObjectName("resetTargetButton")
        self.targetConfigLayout.addWidget(self.resetTargetButton, 1, 2, 1, 1)
        self.applyTargetButton = QtWidgets.QToolButton(self.centralwidget)
        self.applyTargetButton.setObjectName("applyTargetButton")
        self.targetConfigLayout.addWidget(self.applyTargetButton, 0, 2, 1, 1)
        self.targetSampleRate = QtWidgets.QSpinBox(self.centralwidget)
        self.targetSampleRate.setMinimum(100)
        self.targetSampleRate.setMaximum(1000)
        self.targetSampleRate.setProperty("value", 500)
        self.targetSampleRate.setObjectName("targetSampleRate")
        self.targetConfigLayout.addWidget(self.targetSampleRate, 0, 1, 1, 1)
        self.targetSampleRateLabel = QtWidgets.QLabel(self.centralwidget)
        self.targetSampleRateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.targetSampleRateLabel.setObjectName("targetSampleRateLabel")
        self.targetConfigLayout.addWidget(self.targetSampleRateLabel, 0, 0, 1, 1)
        self.addRecorderLayout.addLayout(self.targetConfigLayout)
        self.recordersHeaderLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.recordersHeaderLabel.setFont(font)
        self.recordersHeaderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.recordersHeaderLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.recordersHeaderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.recordersHeaderLabel.setObjectName("recordersHeaderLabel")
        self.addRecorderLayout.addWidget(self.recordersHeaderLabel)
        self.recordersLayout = QtWidgets.QVBoxLayout()
        self.recordersLayout.setObjectName("recordersLayout")
        self.addRecorderLayout.addLayout(self.recordersLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.addRecorderButton = QtWidgets.QPushButton(self.centralwidget)
        self.addRecorderButton.setObjectName("addRecorderButton")
        self.buttonLayout.addWidget(self.addRecorderButton)
        self.saveRecordersButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveRecordersButton.setObjectName("saveRecordersButton")
        self.buttonLayout.addWidget(self.saveRecordersButton)
        self.addRecorderLayout.addLayout(self.buttonLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.addRecorderLayout.addItem(spacerItem3)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.addRecorderLayout.addWidget(self.resetButton)
        self.mainLayout.addLayout(self.addRecorderLayout)
        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 10)
        self.mainLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 30))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")
        self.actionShow_Logs = QtWidgets.QAction(MainWindow)
        self.actionShow_Logs.setObjectName("actionShow_Logs")
        self.actionRelease_Notes = QtWidgets.QAction(MainWindow)
        self.actionRelease_Notes.setObjectName("actionRelease_Notes")
        self.actionSave_Chart = QtWidgets.QAction(MainWindow)
        self.actionSave_Chart.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave_Chart.setObjectName("actionSave_Chart")
        self.actionExport_Wav = QtWidgets.QAction(MainWindow)
        self.actionExport_Wav.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionExport_Wav.setObjectName("actionExport_Wav")
        self.menuSettings.addAction(self.action_Preferences)
        self.menu_Help.addAction(self.actionShow_Logs)
        self.menu_Help.addAction(self.actionRelease_Notes)
        self.menu_File.addAction(self.actionSave_Chart)
        self.menu_File.addAction(self.actionExport_Wav)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.chartTabs.setCurrentIndex(0)
        self.resetTargetButton.clicked.connect(MainWindow.reset_target)
        self.applyTargetButton.clicked.connect(MainWindow.apply_target)
        self.targetSampleRate.valueChanged['int'].connect(MainWindow.update_target)
        self.targetBatchSize.valueChanged['int'].connect(MainWindow.update_target)
        self.targetAccelEnabled.stateChanged['int'].connect(MainWindow.update_target)
        self.targetAccelSens.currentIndexChanged['int'].connect(MainWindow.update_target)
        self.targetGyroEnabled.stateChanged['int'].connect(MainWindow.update_target)
        self.targetGyroSens.currentIndexChanged['int'].connect(MainWindow.update_target)
        self.saveRecordersButton.clicked.connect(MainWindow.save_recorders)
        self.bufferSize.valueChanged['int'].connect(MainWindow.set_buffer_size)
        self.addRecorderButton.clicked.connect(MainWindow.add_new_recorder)
        self.chartTabs.currentChanged['int'].connect(MainWindow.set_visible_chart)
        self.resetButton.clicked.connect(MainWindow.reset_recording)
        self.visibleCurves.itemSelectionChanged.connect(MainWindow.set_visible_curves)
        self.activeRecorders.itemSelectionChanged.connect(MainWindow.set_visible_recorders)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.targetSampleRate, self.targetBatchSize)
        MainWindow.setTabOrder(self.targetBatchSize, self.targetAccelEnabled)
        MainWindow.setTabOrder(self.targetAccelEnabled, self.targetAccelSens)
        MainWindow.setTabOrder(self.targetAccelSens, self.targetGyroEnabled)
        MainWindow.setTabOrder(self.targetGyroEnabled, self.targetGyroSens)
        MainWindow.setTabOrder(self.targetGyroSens, self.applyTargetButton)
        MainWindow.setTabOrder(self.applyTargetButton, self.resetTargetButton)
        MainWindow.setTabOrder(self.resetTargetButton, self.addRecorderButton)
        MainWindow.setTabOrder(self.addRecorderButton, self.saveRecordersButton)
        MainWindow.setTabOrder(self.saveRecordersButton, self.resetButton)
        MainWindow.setTabOrder(self.resetButton, self.resolutionHz)
        MainWindow.setTabOrder(self.resolutionHz, self.bufferSize)
        MainWindow.setTabOrder(self.bufferSize, self.fps)
        MainWindow.setTabOrder(self.fps, self.actualFPS)
        MainWindow.setTabOrder(self.actualFPS, self.elapsedTime)
        MainWindow.setTabOrder(self.elapsedTime, self.activeRecorders)
        MainWindow.setTabOrder(self.activeRecorders, self.visibleCurves)
        MainWindow.setTabOrder(self.visibleCurves, self.rtaAverage)
        MainWindow.setTabOrder(self.rtaAverage, self.rtaChart)
        MainWindow.setTabOrder(self.rtaChart, self.vibrationAnalysis)
        MainWindow.setTabOrder(self.vibrationAnalysis, self.liveVibrationChart)
        MainWindow.setTabOrder(self.liveVibrationChart, self.rtaView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QVibe Analyser"))
        self.chartControlsLabel.setText(_translate("MainWindow", "Chart Controls"))
        self.activeRecordersLabel.setText(_translate("MainWindow", "Visible Recorders"))
        self.visibleCurvesLabel.setText(_translate("MainWindow", "Visible Curves"))
        __sortingEnabled = self.visibleCurves.isSortingEnabled()
        self.visibleCurves.setSortingEnabled(False)
        item = self.visibleCurves.item(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.visibleCurves.item(1)
        item.setText(_translate("MainWindow", "y"))
        item = self.visibleCurves.item(2)
        item.setText(_translate("MainWindow", "z"))
        item = self.visibleCurves.item(3)
        item.setText(_translate("MainWindow", "sum"))
        self.visibleCurves.setSortingEnabled(__sortingEnabled)
        self.resolutionHzLabel.setText(_translate("MainWindow", "Resolution"))
        self.bufferSizeLabel.setText(_translate("MainWindow", "Buffer"))
        self.magMin.setSuffix(_translate("MainWindow", " dB"))
        self.freqMin.setSuffix(_translate("MainWindow", " Hz"))
        self.freqMax.setSuffix(_translate("MainWindow", " Hz"))
        self.fpsLabel.setText(_translate("MainWindow", "Target FPS"))
        self.resolutionHz.setItemText(0, _translate("MainWindow", "0.25 Hz"))
        self.resolutionHz.setItemText(1, _translate("MainWindow", "0.5 Hz"))
        self.resolutionHz.setItemText(2, _translate("MainWindow", "1.0 Hz"))
        self.resolutionHz.setItemText(3, _translate("MainWindow", "2.0 Hz"))
        self.resolutionHz.setItemText(4, _translate("MainWindow", "4.0 Hz"))
        self.bufferSize.setSuffix(_translate("MainWindow", " s"))
        self.actualFPSLabel.setText(_translate("MainWindow", "Actual FPS"))
        self.magRangeLabel.setText(_translate("MainWindow", "Magnitude"))
        self.label.setText(_translate("MainWindow", "Elapsed"))
        self.elapsedTime.setDisplayFormat(_translate("MainWindow", "mm:ss.zzz"))
        self.freqLabel.setText(_translate("MainWindow", "Frequency"))
        self.magMax.setSuffix(_translate("MainWindow", " dB"))
        self.vibrationAnalysis.setItemText(0, _translate("MainWindow", "Vibration"))
        self.vibrationAnalysis.setItemText(1, _translate("MainWindow", "Tilt"))
        self.vibrationAnalysis.setItemText(2, _translate("MainWindow", "Raw"))
        self.chartTabs.setTabText(self.chartTabs.indexOf(self.vibrationTab), _translate("MainWindow", "By Time"))
        self.rtaAverageLabel.setText(_translate("MainWindow", "Averages"))
        self.rtaAverage.setItemText(0, _translate("MainWindow", "1x"))
        self.rtaAverage.setItemText(1, _translate("MainWindow", "2x"))
        self.rtaAverage.setItemText(2, _translate("MainWindow", "5x"))
        self.rtaAverage.setItemText(3, _translate("MainWindow", "Forever"))
        self.rtaViewLabel.setText(_translate("MainWindow", "View"))
        self.rtaView.setItemText(0, _translate("MainWindow", "avg"))
        self.rtaView.setItemText(1, _translate("MainWindow", "peak"))
        self.rtaView.setItemText(2, _translate("MainWindow", "psd"))
        self.smoothRta.setText(_translate("MainWindow", "Smooth?"))
        self.chartTabs.setTabText(self.chartTabs.indexOf(self.rtaTab), _translate("MainWindow", "RTA"))
        self.chartTabs.setTabText(self.chartTabs.indexOf(self.spectrogramTab), _translate("MainWindow", "Spectrogram"))
        self.configHeaderLabel.setText(_translate("MainWindow", "Target"))
        self.accelerometerLabel.setText(_translate("MainWindow", "Accelerometer"))
        self.targetAccelEnabled.setText(_translate("MainWindow", "Enabled?"))
        self.targetAccelSens.setItemText(0, _translate("MainWindow", "2"))
        self.targetAccelSens.setItemText(1, _translate("MainWindow", "4"))
        self.targetAccelSens.setItemText(2, _translate("MainWindow", "8"))
        self.targetAccelSens.setItemText(3, _translate("MainWindow", "16"))
        self.gyroLabel.setText(_translate("MainWindow", "Gyro"))
        self.targetGyroEnabled.setText(_translate("MainWindow", "Enabled?"))
        self.targetGyroSens.setItemText(0, _translate("MainWindow", "250"))
        self.targetGyroSens.setItemText(1, _translate("MainWindow", "500"))
        self.targetGyroSens.setItemText(2, _translate("MainWindow", "1000"))
        self.targetGyroSens.setItemText(3, _translate("MainWindow", "2000"))
        self.targetBatchSizeLabel.setText(_translate("MainWindow", "Batch Size"))
        self.resetTargetButton.setText(_translate("MainWindow", "..."))
        self.applyTargetButton.setText(_translate("MainWindow", "..."))
        self.targetSampleRate.setSuffix(_translate("MainWindow", " Hz"))
        self.targetSampleRateLabel.setText(_translate("MainWindow", "Sample Rate"))
        self.recordersHeaderLabel.setText(_translate("MainWindow", "Recorders"))
        self.addRecorderButton.setText(_translate("MainWindow", "Add New"))
        self.saveRecordersButton.setText(_translate("MainWindow", "Save"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Preferences.setText(_translate("MainWindow", "&Preferences"))
        self.action_Preferences.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionShow_Logs.setText(_translate("MainWindow", "Show &Logs"))
        self.actionShow_Logs.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionRelease_Notes.setText(_translate("MainWindow", "Release &Notes"))
        self.actionSave_Chart.setText(_translate("MainWindow", "Save &Chart"))
        self.actionSave_Chart.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExport_Wav.setText(_translate("MainWindow", "Export &Wav"))
        self.actionExport_Wav.setShortcut(_translate("MainWindow", "Ctrl+W"))
from pyqtgraph import GraphicsLayoutWidget
from qvibe import PlotWidgetForSpectrum, PlotWidgetWithDateAxis
