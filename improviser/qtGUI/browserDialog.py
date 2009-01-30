# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Fri Jan 30 19:55:24 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_browserDialog(object):
    def setupUi(self, browserDialog):
        browserDialog.setObjectName("browserDialog")
        browserDialog.resize(614, 241)
        browserDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(browserDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(browserDialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.authors = QtGui.QListWidget(self.frame)
        self.authors.setObjectName("authors")
        self.horizontalLayout.addWidget(self.authors)
        self.content = QtGui.QListWidget(self.frame)
        self.content.setObjectName("content")
        self.horizontalLayout.addWidget(self.content)
        self.item = QtGui.QListWidget(self.frame)
        self.item.setObjectName("item")
        self.horizontalLayout.addWidget(self.item)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.update = QtGui.QPushButton(browserDialog)
        self.update.setEnabled(True)
        self.update.setObjectName("update")
        self.horizontalLayout_2.addWidget(self.update)
        self.newbutton = QtGui.QPushButton(browserDialog)
        self.newbutton.setObjectName("newbutton")
        self.horizontalLayout_2.addWidget(self.newbutton)
        self.buttonBox = QtGui.QDialogButtonBox(browserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(browserDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), browserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(browserDialog)

    def retranslateUi(self, browserDialog):
        browserDialog.setWindowTitle(QtGui.QApplication.translate("browserDialog", "Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.setSortingEnabled(False)
        self.content.setSortingEnabled(True)
        self.update.setText(QtGui.QApplication.translate("browserDialog", "Check for Updates", None, QtGui.QApplication.UnicodeUTF8))
        self.newbutton.setText(QtGui.QApplication.translate("browserDialog", "New", None, QtGui.QApplication.UnicodeUTF8))

