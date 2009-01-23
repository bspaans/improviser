# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressionbrowser.ui'
#
# Created: Fri Jan 23 14:12:11 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_progressionBrowser(object):
    def setupUi(self, progressionBrowser):
        progressionBrowser.setObjectName("progressionBrowser")
        progressionBrowser.resize(610, 231)
        progressionBrowser.setModal(True)
        self.frame = QtGui.QFrame(progressionBrowser)
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
        self.progressions = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.progressions.setObjectName("progressions")
        self.horizontalLayout.addWidget(self.progressions)
        self.progression = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.progression.setObjectName("progression")
        self.horizontalLayout.addWidget(self.progression)
        self.update = QtGui.QPushButton(progressionBrowser)
        self.update.setGeometry(QtCore.QRect(10, 190, 77, 29))
        self.update.setObjectName("update")
        self.buttonBox = QtGui.QDialogButtonBox(progressionBrowser)
        self.buttonBox.setGeometry(QtCore.QRect(158, 190, 441, 29))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(progressionBrowser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), progressionBrowser.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), progressionBrowser.reject)
        QtCore.QMetaObject.connectSlotsByName(progressionBrowser)

    def retranslateUi(self, progressionBrowser):
        progressionBrowser.setWindowTitle(QtGui.QApplication.translate("progressionBrowser", "Progression Browser", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.authors.isSortingEnabled()
        self.authors.setSortingEnabled(False)
        self.authors.item(0).setText(QtGui.QApplication.translate("progressionBrowser", "Default progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.item(1).setText(QtGui.QApplication.translate("progressionBrowser", "Own progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.item(2).setText(QtGui.QApplication.translate("progressionBrowser", "All progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.setSortingEnabled(__sortingEnabled)
        self.update.setText(QtGui.QApplication.translate("progressionBrowser", "Update", None, QtGui.QApplication.UnicodeUTF8))

