# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName("preferencesDialog")
        preferencesDialog.resize(642, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(preferencesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.panes = QtWidgets.QVBoxLayout()
        self.panes.setObjectName("panes")
        self.userLayout = QtWidgets.QGridLayout()
        self.userLayout.setObjectName("userLayout")
        self.wavSaveDir = QtWidgets.QLineEdit(preferencesDialog)
        self.wavSaveDir.setReadOnly(True)
        self.wavSaveDir.setObjectName("wavSaveDir")
        self.userLayout.addWidget(self.wavSaveDir, 1, 1, 1, 1)
        self.wavSaveDirLabel = QtWidgets.QLabel(preferencesDialog)
        self.wavSaveDirLabel.setObjectName("wavSaveDirLabel")
        self.userLayout.addWidget(self.wavSaveDirLabel, 1, 0, 1, 1)
        self.wavSaveDirPicker = QtWidgets.QToolButton(preferencesDialog)
        self.wavSaveDirPicker.setObjectName("wavSaveDirPicker")
        self.userLayout.addWidget(self.wavSaveDirPicker, 1, 2, 1, 1)
        self.userLayoutLabel = QtWidgets.QLabel(preferencesDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.userLayoutLabel.setFont(font)
        self.userLayoutLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.userLayoutLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.userLayoutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userLayoutLabel.setObjectName("userLayoutLabel")
        self.userLayout.addWidget(self.userLayoutLabel, 0, 0, 1, 3)
        self.panes.addLayout(self.userLayout)
        self.analysisPane = QtWidgets.QGridLayout()
        self.analysisPane.setObjectName("analysisPane")
        self.zScaleLabel = QtWidgets.QLabel(preferencesDialog)
        self.zScaleLabel.setObjectName("zScaleLabel")
        self.analysisPane.addWidget(self.zScaleLabel, 1, 4, 1, 1)
        self.xScale = QtWidgets.QDoubleSpinBox(preferencesDialog)
        self.xScale.setObjectName("xScale")
        self.analysisPane.addWidget(self.xScale, 1, 1, 1, 1)
        self.magMin = QtWidgets.QSpinBox(preferencesDialog)
        self.magMin.setMaximum(150)
        self.magMin.setObjectName("magMin")
        self.analysisPane.addWidget(self.magMin, 2, 1, 1, 1)
        self.xScaleLabel = QtWidgets.QLabel(preferencesDialog)
        self.xScaleLabel.setObjectName("xScaleLabel")
        self.analysisPane.addWidget(self.xScaleLabel, 1, 0, 1, 1)
        self.analysisLayoutLabel = QtWidgets.QLabel(preferencesDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.analysisLayoutLabel.setFont(font)
        self.analysisLayoutLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.analysisLayoutLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.analysisLayoutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.analysisLayoutLabel.setObjectName("analysisLayoutLabel")
        self.analysisPane.addWidget(self.analysisLayoutLabel, 0, 0, 1, 6)
        self.magMaxLabel = QtWidgets.QLabel(preferencesDialog)
        self.magMaxLabel.setObjectName("magMaxLabel")
        self.analysisPane.addWidget(self.magMaxLabel, 2, 2, 1, 1)
        self.yScale = QtWidgets.QDoubleSpinBox(preferencesDialog)
        self.yScale.setObjectName("yScale")
        self.analysisPane.addWidget(self.yScale, 1, 3, 1, 1)
        self.zScale = QtWidgets.QDoubleSpinBox(preferencesDialog)
        self.zScale.setObjectName("zScale")
        self.analysisPane.addWidget(self.zScale, 1, 5, 1, 1)
        self.yScaleLabel = QtWidgets.QLabel(preferencesDialog)
        self.yScaleLabel.setObjectName("yScaleLabel")
        self.analysisPane.addWidget(self.yScaleLabel, 1, 2, 1, 1)
        self.maxMinLabel = QtWidgets.QLabel(preferencesDialog)
        self.maxMinLabel.setObjectName("maxMinLabel")
        self.analysisPane.addWidget(self.maxMinLabel, 2, 0, 1, 1)
        self.magMax = QtWidgets.QSpinBox(preferencesDialog)
        self.magMax.setMaximum(150)
        self.magMax.setProperty("value", 150)
        self.magMax.setObjectName("magMax")
        self.analysisPane.addWidget(self.magMax, 2, 3, 1, 1)
        self.freqMinLabel = QtWidgets.QLabel(preferencesDialog)
        self.freqMinLabel.setObjectName("freqMinLabel")
        self.analysisPane.addWidget(self.freqMinLabel, 3, 0, 1, 1)
        self.freqMaxLabel = QtWidgets.QLabel(preferencesDialog)
        self.freqMaxLabel.setObjectName("freqMaxLabel")
        self.analysisPane.addWidget(self.freqMaxLabel, 3, 2, 1, 1)
        self.freqMin = QtWidgets.QSpinBox(preferencesDialog)
        self.freqMin.setMinimum(1)
        self.freqMin.setMaximum(1000)
        self.freqMin.setObjectName("freqMin")
        self.analysisPane.addWidget(self.freqMin, 3, 1, 1, 1)
        self.freqMax = QtWidgets.QSpinBox(preferencesDialog)
        self.freqMax.setMinimum(1)
        self.freqMax.setMaximum(1000)
        self.freqMax.setProperty("value", 125)
        self.freqMax.setObjectName("freqMax")
        self.analysisPane.addWidget(self.freqMax, 3, 3, 1, 1)
        self.panes.addLayout(self.analysisPane)
        self.systemPane = QtWidgets.QGridLayout()
        self.systemPane.setObjectName("systemPane")
        self.checkForUpdates = QtWidgets.QCheckBox(preferencesDialog)
        self.checkForUpdates.setChecked(True)
        self.checkForUpdates.setObjectName("checkForUpdates")
        self.systemPane.addWidget(self.checkForUpdates, 1, 0, 1, 1)
        self.checkForBetaUpdates = QtWidgets.QCheckBox(preferencesDialog)
        self.checkForBetaUpdates.setObjectName("checkForBetaUpdates")
        self.systemPane.addWidget(self.checkForBetaUpdates, 1, 1, 1, 1)
        self.systemLayoutLabel = QtWidgets.QLabel(preferencesDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.systemLayoutLabel.setFont(font)
        self.systemLayoutLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.systemLayoutLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.systemLayoutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.systemLayoutLabel.setObjectName("systemLayoutLabel")
        self.systemPane.addWidget(self.systemLayoutLabel, 0, 0, 1, 2)
        self.panes.addLayout(self.systemPane)
        self.verticalLayout.addLayout(self.panes)
        self.buttonBox = QtWidgets.QDialogButtonBox(preferencesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(preferencesDialog)
        self.buttonBox.accepted.connect(preferencesDialog.accept)
        self.buttonBox.rejected.connect(preferencesDialog.reject)
        self.wavSaveDirPicker.clicked.connect(preferencesDialog.pick_save_dir)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        preferencesDialog.setWindowTitle(_translate("preferencesDialog", "Preferences"))
        self.wavSaveDirLabel.setText(_translate("preferencesDialog", "Save Directory"))
        self.wavSaveDirPicker.setText(_translate("preferencesDialog", "..."))
        self.userLayoutLabel.setText(_translate("preferencesDialog", "User Preferences"))
        self.zScaleLabel.setText(_translate("preferencesDialog", "z Scale"))
        self.xScale.setSuffix(_translate("preferencesDialog", " x"))
        self.magMin.setSuffix(_translate("preferencesDialog", " dB"))
        self.xScaleLabel.setText(_translate("preferencesDialog", "x Scale"))
        self.analysisLayoutLabel.setText(_translate("preferencesDialog", "Analysis"))
        self.magMaxLabel.setText(_translate("preferencesDialog", "Max"))
        self.yScale.setSuffix(_translate("preferencesDialog", " x"))
        self.zScale.setSuffix(_translate("preferencesDialog", " x"))
        self.yScaleLabel.setText(_translate("preferencesDialog", "y Scale"))
        self.maxMinLabel.setText(_translate("preferencesDialog", "Magnitude Min"))
        self.magMax.setSuffix(_translate("preferencesDialog", " dB"))
        self.freqMinLabel.setText(_translate("preferencesDialog", "Frequency Min"))
        self.freqMaxLabel.setText(_translate("preferencesDialog", "Max"))
        self.freqMin.setSuffix(_translate("preferencesDialog", " Hz"))
        self.freqMax.setSuffix(_translate("preferencesDialog", " Hz"))
        self.checkForUpdates.setText(_translate("preferencesDialog", "Check for Updates on startup?"))
        self.checkForBetaUpdates.setText(_translate("preferencesDialog", "Include Beta Versions?"))
        self.systemLayoutLabel.setText(_translate("preferencesDialog", "System"))
