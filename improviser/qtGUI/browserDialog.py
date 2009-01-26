# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Mon Jan 26 06:09:42 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_browserDialog(object):
    def setupUi(self, browserDialog):
        browserDialog.setObjectName("browserDialog")
        browserDialog.resize(610, 231)
        browserDialog.setModal(True)
        self.frame = QtGui.QFrame(browserDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 591, 171))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.authors = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.authors.setObjectName("authors")
        QtGui.QListWidgetItem(self.authors)
        QtGui.QListWidgetItem(self.authors)
        QtGui.QListWidgetItem(self.authors)
        self.horizontalLayout.addWidget(self.authors)
        self.content = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.content.setObjectName("content")
        self.horizontalLayout.addWidget(self.content)
        self.item = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.item.setObjectName("item")
        self.horizontalLayout.addWidget(self.item)
        self.update = QtGui.QPushButton(browserDialog)
        self.update.setEnabled(True)
        self.update.setGeometry(QtCore.QRect(10, 190, 131, 29))
        self.update.setObjectName("update")
        self.buttonBox = QtGui.QDialogButtonBox(browserDialog)
        self.buttonBox.setGeometry(QtCore.QRect(158, 190, 441, 29))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(browserDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), browserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(browserDialog)

    def retranslateUi(self, browserDialog):
        browserDialog.setWindowTitle(QtGui.QApplication.translate("browserDialog", "Browser", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.authors.isSortingEnabled()
        self.authors.setSortingEnabled(False)
        self.authors.item(0).setText(QtGui.QApplication.translate("browserDialog", "Default progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.item(1).setText(QtGui.QApplication.translate("browserDialog", "Own progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.item(2).setText(QtGui.QApplication.translate("browserDialog", "All progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.setSortingEnabled(__sortingEnabled)
        self.update.setText(QtGui.QApplication.translate("browserDialog", "Check for Updates", None, QtGui.QApplication.UnicodeUTF8))

