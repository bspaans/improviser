# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'improviser/qtGUI/upload.ui'
#
# Created: Fri Jan 30 06:53:40 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_uploadDialog(object):
    def setupUi(self, uploadDialog):
        uploadDialog.setObjectName("uploadDialog")
        uploadDialog.resize(371, 186)
        uploadDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(uploadDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.uploadname = QtGui.QLineEdit(uploadDialog)
        self.uploadname.setGeometry(QtCore.QRect(110, 20, 251, 23))
        self.uploadname.setObjectName("uploadname")
        self.uploaddescription = QtGui.QPlainTextEdit(uploadDialog)
        self.uploaddescription.setGeometry(QtCore.QRect(110, 60, 251, 71))
        self.uploaddescription.setObjectName("uploaddescription")
        self.label_2 = QtGui.QLabel(uploadDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 56, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(uploadDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 71, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(uploadDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), uploadDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(uploadDialog)

    def retranslateUi(self, uploadDialog):
        uploadDialog.setWindowTitle(QtGui.QApplication.translate("uploadDialog", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("uploadDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("uploadDialog", "Description", None, QtGui.QApplication.UnicodeUTF8))

