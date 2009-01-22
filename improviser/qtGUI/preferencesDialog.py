# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'improviser/qtGUI/preferences.ui'
#
# Created: Wed Jan 21 09:52:55 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName("preferencesDialog")
        preferencesDialog.resize(417, 473)
        preferencesDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(preferencesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 430, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtGui.QGroupBox(preferencesDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 161))
        self.groupBox.setObjectName("groupBox")
        self.no_fluidsynth = QtGui.QCheckBox(self.groupBox)
        self.no_fluidsynth.setGeometry(QtCore.QRect(30, 110, 83, 22))
        self.no_fluidsynth.setObjectName("no_fluidsynth")
        self.browsebutton = QtGui.QPushButton(self.groupBox)
        self.browsebutton.setGeometry(QtCore.QRect(290, 30, 80, 27))
        self.browsebutton.setObjectName("browsebutton")
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 81, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 70, 81, 17))
        self.label_10.setObjectName("label_10")
        self.driver = QtGui.QComboBox(self.groupBox)
        self.driver.setGeometry(QtCore.QRect(130, 70, 231, 22))
        self.driver.setObjectName("driver")
        self.soundfont = QtGui.QLineEdit(self.groupBox)
        self.soundfont.setEnabled(False)
        self.soundfont.setGeometry(QtCore.QRect(130, 30, 151, 23))
        self.soundfont.setObjectName("soundfont")
        self.groupBox_2 = QtGui.QGroupBox(preferencesDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 391, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 120, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 61, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 341, 71))
        self.label_3.setLineWidth(1)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.username = QtGui.QLineEdit(self.groupBox_2)
        self.username.setGeometry(QtCore.QRect(130, 120, 221, 23))
        self.username.setObjectName("username")
        self.password = QtGui.QLineEdit(self.groupBox_2)
        self.password.setGeometry(QtCore.QRect(130, 160, 221, 23))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.nologin = QtGui.QCheckBox(self.groupBox_2)
        self.nologin.setGeometry(QtCore.QRect(20, 200, 83, 22))
        self.nologin.setObjectName("nologin")

        self.retranslateUi(preferencesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), preferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        preferencesDialog.setWindowTitle(QtGui.QApplication.translate("preferencesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("preferencesDialog", "Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.no_fluidsynth.setStatusTip(QtGui.QApplication.translate("preferencesDialog", "Disable audio output. Only write midi file.", None, QtGui.QApplication.UnicodeUTF8))
        self.no_fluidsynth.setText(QtGui.QApplication.translate("preferencesDialog", "No audio", None, QtGui.QApplication.UnicodeUTF8))
        self.browsebutton.setText(QtGui.QApplication.translate("preferencesDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setStatusTip(QtGui.QApplication.translate("preferencesDialog", "The location of the soundfont to use", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("preferencesDialog", "Soundfont", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("preferencesDialog", "Audio driver", None, QtGui.QApplication.UnicodeUTF8))
        self.soundfont.setStatusTip(QtGui.QApplication.translate("preferencesDialog", "The location of the soundfont to use", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("preferencesDialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("preferencesDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("preferencesDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("preferencesDialog", "Login if you want to be able to upload your songs, blocks, instruments and/or progressions to the Improviser site (http://improviser.onderstekop.nl/). Login with a name that hasn\'t been used to register it.", None, QtGui.QApplication.UnicodeUTF8))
        self.nologin.setText(QtGui.QApplication.translate("preferencesDialog", "Don\'t login", None, QtGui.QApplication.UnicodeUTF8))

