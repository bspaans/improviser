# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'improviser.ui'
#
# Created: Fri Jan 30 04:14:40 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 627)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, 1, 1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Tabs = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tabs.sizePolicy().hasHeightForWidth())
        self.Tabs.setSizePolicy(sizePolicy)
        self.Tabs.setMinimumSize(QtCore.QSize(550, 325))
        self.Tabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.Tabs.setElideMode(QtCore.Qt.ElideLeft)
        self.Tabs.setObjectName("Tabs")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, -1, 0, -1)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.projectname = QtGui.QLineEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectname.sizePolicy().hasHeightForWidth())
        self.projectname.setSizePolicy(sizePolicy)
        self.projectname.setMinimumSize(QtCore.QSize(300, 0))
        self.projectname.setObjectName("projectname")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.projectname)
        self.label_12 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_12)
        self.author = QtGui.QLineEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.author.sizePolicy().hasHeightForWidth())
        self.author.setSizePolicy(sizePolicy)
        self.author.setMinimumSize(QtCore.QSize(150, 0))
        self.author.setObjectName("author")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.author)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Tabs.addTab(self.tab, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout = QtGui.QGridLayout(self.tab_5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtGui.QLabel(self.tab_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.movement = QtGui.QComboBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movement.sizePolicy().hasHeightForWidth())
        self.movement.setSizePolicy(sizePolicy)
        self.movement.setObjectName("movement")
        self.gridLayout.addWidget(self.movement, 0, 2, 1, 2)
        self.label_5 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.loop = QtGui.QSpinBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loop.sizePolicy().hasHeightForWidth())
        self.loop.setSizePolicy(sizePolicy)
        self.loop.setMinimumSize(QtCore.QSize(84, 0))
        self.loop.setMaximum(10000)
        self.loop.setProperty("value", QtCore.QVariant(1))
        self.loop.setObjectName("loop")
        self.gridLayout.addWidget(self.loop, 1, 2, 1, 1)
        self.loopslide = QtGui.QSlider(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loopslide.sizePolicy().hasHeightForWidth())
        self.loopslide.setSizePolicy(sizePolicy)
        self.loopslide.setPageStep(10)
        self.loopslide.setProperty("value", QtCore.QVariant(1))
        self.loopslide.setOrientation(QtCore.Qt.Horizontal)
        self.loopslide.setObjectName("loopslide")
        self.gridLayout.addWidget(self.loopslide, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 1)
        self.resolution = QtGui.QComboBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resolution.sizePolicy().hasHeightForWidth())
        self.resolution.setSizePolicy(sizePolicy)
        self.resolution.setMinimumSize(QtCore.QSize(84, 0))
        self.resolution.setObjectName("resolution")
        self.gridLayout.addWidget(self.resolution, 1, 6, 1, 1)
        self.label = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.bpm = QtGui.QSpinBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bpm.sizePolicy().hasHeightForWidth())
        self.bpm.setSizePolicy(sizePolicy)
        self.bpm.setMinimumSize(QtCore.QSize(84, 0))
        self.bpm.setMinimum(1)
        self.bpm.setMaximum(1000)
        self.bpm.setProperty("value", QtCore.QVariant(120))
        self.bpm.setObjectName("bpm")
        self.gridLayout.addWidget(self.bpm, 2, 2, 1, 1)
        self.bpmslide = QtGui.QSlider(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bpmslide.sizePolicy().hasHeightForWidth())
        self.bpmslide.setSizePolicy(sizePolicy)
        self.bpmslide.setPageStep(10)
        self.bpmslide.setProperty("value", QtCore.QVariant(50))
        self.bpmslide.setOrientation(QtCore.Qt.Horizontal)
        self.bpmslide.setObjectName("bpmslide")
        self.gridLayout.addWidget(self.bpmslide, 2, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 5, 1, 1)
        self.key = QtGui.QComboBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key.sizePolicy().hasHeightForWidth())
        self.key.setSizePolicy(sizePolicy)
        self.key.setMinimumSize(QtCore.QSize(84, 0))
        self.key.setObjectName("key")
        self.gridLayout.addWidget(self.key, 2, 6, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.wildness = QtGui.QDoubleSpinBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wildness.sizePolicy().hasHeightForWidth())
        self.wildness.setSizePolicy(sizePolicy)
        self.wildness.setMinimumSize(QtCore.QSize(84, 0))
        self.wildness.setDecimals(5)
        self.wildness.setMaximum(100.0)
        self.wildness.setSingleStep(0.025)
        self.wildness.setProperty("value", QtCore.QVariant(0.5))
        self.wildness.setObjectName("wildness")
        self.gridLayout.addWidget(self.wildness, 3, 2, 1, 1)
        self.wildslide = QtGui.QSlider(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wildslide.sizePolicy().hasHeightForWidth())
        self.wildslide.setSizePolicy(sizePolicy)
        self.wildslide.setProperty("value", QtCore.QVariant(1))
        self.wildslide.setOrientation(QtCore.Qt.Horizontal)
        self.wildslide.setObjectName("wildslide")
        self.gridLayout.addWidget(self.wildslide, 3, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 5, 1, 1)
        self.duration = QtGui.QSpinBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.duration.sizePolicy().hasHeightForWidth())
        self.duration.setSizePolicy(sizePolicy)
        self.duration.setMinimumSize(QtCore.QSize(84, 0))
        self.duration.setMinimum(1)
        self.duration.setMaximum(1000)
        self.duration.setProperty("value", QtCore.QVariant(1))
        self.duration.setObjectName("duration")
        self.gridLayout.addWidget(self.duration, 3, 6, 1, 1)
        self.swing = QtGui.QCheckBox(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swing.sizePolicy().hasHeightForWidth())
        self.swing.setSizePolicy(sizePolicy)
        self.swing.setObjectName("swing")
        self.gridLayout.addWidget(self.swing, 4, 6, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(60, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 7, 1, 1)
        self.Tabs.addTab(self.tab_5, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.blocks = QtGui.QListWidget(self.tab_3)
        self.blocks.setObjectName("blocks")
        self.horizontalLayout_3.addWidget(self.blocks)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addblockbutton = QtGui.QPushButton(self.tab_3)
        self.addblockbutton.setObjectName("addblockbutton")
        self.verticalLayout_3.addWidget(self.addblockbutton)
        self.removeblock = QtGui.QPushButton(self.tab_3)
        self.removeblock.setEnabled(True)
        self.removeblock.setObjectName("removeblock")
        self.verticalLayout_3.addWidget(self.removeblock)
        self.editblock = QtGui.QPushButton(self.tab_3)
        self.editblock.setEnabled(True)
        self.editblock.setObjectName("editblock")
        self.verticalLayout_3.addWidget(self.editblock)
        self.clearblocks = QtGui.QPushButton(self.tab_3)
        self.clearblocks.setObjectName("clearblocks")
        self.verticalLayout_3.addWidget(self.clearblocks)
        self.copyblock = QtGui.QPushButton(self.tab_3)
        self.copyblock.setObjectName("copyblock")
        self.verticalLayout_3.addWidget(self.copyblock)
        self.upblock = QtGui.QPushButton(self.tab_3)
        self.upblock.setObjectName("upblock")
        self.verticalLayout_3.addWidget(self.upblock)
        self.downblock = QtGui.QPushButton(self.tab_3)
        self.downblock.setObjectName("downblock")
        self.verticalLayout_3.addWidget(self.downblock)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.Tabs.addTab(self.tab_3, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.instruments = QtGui.QListWidget(self.tab_2)
        self.instruments.setObjectName("instruments")
        self.horizontalLayout_4.addWidget(self.instruments)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.addinstrumentbutton = QtGui.QPushButton(self.tab_2)
        self.addinstrumentbutton.setObjectName("addinstrumentbutton")
        self.verticalLayout_4.addWidget(self.addinstrumentbutton)
        self.removeinstrument = QtGui.QPushButton(self.tab_2)
        self.removeinstrument.setEnabled(True)
        self.removeinstrument.setObjectName("removeinstrument")
        self.verticalLayout_4.addWidget(self.removeinstrument)
        self.editinstrument = QtGui.QPushButton(self.tab_2)
        self.editinstrument.setEnabled(True)
        self.editinstrument.setObjectName("editinstrument")
        self.verticalLayout_4.addWidget(self.editinstrument)
        self.clearinstruments = QtGui.QPushButton(self.tab_2)
        self.clearinstruments.setObjectName("clearinstruments")
        self.verticalLayout_4.addWidget(self.clearinstruments)
        self.copyinstrument = QtGui.QPushButton(self.tab_2)
        self.copyinstrument.setObjectName("copyinstrument")
        self.verticalLayout_4.addWidget(self.copyinstrument)
        self.upinstrument = QtGui.QPushButton(self.tab_2)
        self.upinstrument.setObjectName("upinstrument")
        self.verticalLayout_4.addWidget(self.upinstrument)
        self.downinstrument = QtGui.QPushButton(self.tab_2)
        self.downinstrument.setObjectName("downinstrument")
        self.verticalLayout_4.addWidget(self.downinstrument)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.Tabs.addTab(self.tab_2, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressions = QtGui.QListWidget(self.tab_4)
        self.progressions.setObjectName("progressions")
        self.horizontalLayout_5.addWidget(self.progressions)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.addprogressionbutton = QtGui.QPushButton(self.tab_4)
        self.addprogressionbutton.setObjectName("addprogressionbutton")
        self.verticalLayout_5.addWidget(self.addprogressionbutton)
        self.removeprogression = QtGui.QPushButton(self.tab_4)
        self.removeprogression.setEnabled(True)
        self.removeprogression.setObjectName("removeprogression")
        self.verticalLayout_5.addWidget(self.removeprogression)
        self.editprogression = QtGui.QPushButton(self.tab_4)
        self.editprogression.setEnabled(True)
        self.editprogression.setObjectName("editprogression")
        self.verticalLayout_5.addWidget(self.editprogression)
        self.clearprogressions = QtGui.QPushButton(self.tab_4)
        self.clearprogressions.setObjectName("clearprogressions")
        self.verticalLayout_5.addWidget(self.clearprogressions)
        self.copyprogression = QtGui.QPushButton(self.tab_4)
        self.copyprogression.setObjectName("copyprogression")
        self.verticalLayout_5.addWidget(self.copyprogression)
        self.upprogression = QtGui.QPushButton(self.tab_4)
        self.upprogression.setObjectName("upprogression")
        self.verticalLayout_5.addWidget(self.upprogression)
        self.downprogression = QtGui.QPushButton(self.tab_4)
        self.downprogression.setObjectName("downprogression")
        self.verticalLayout_5.addWidget(self.downprogression)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.Tabs.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.Tabs)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startbutton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startbutton.sizePolicy().hasHeightForWidth())
        self.startbutton.setSizePolicy(sizePolicy)
        self.startbutton.setObjectName("startbutton")
        self.horizontalLayout.addWidget(self.startbutton)
        self.stopbutton = QtGui.QPushButton(self.centralwidget)
        self.stopbutton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopbutton.sizePolicy().hasHeightForWidth())
        self.stopbutton.setSizePolicy(sizePolicy)
        self.stopbutton.setObjectName("stopbutton")
        self.horizontalLayout.addWidget(self.stopbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuImport = QtGui.QMenu(self.menu_File)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtGui.QMenu(self.menu_File)
        self.menuExport.setObjectName("menuExport")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menuUpload = QtGui.QMenu(self.menubar)
        self.menuUpload.setObjectName("menuUpload")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Load = QtGui.QAction(MainWindow)
        self.action_Load.setMenuRole(QtGui.QAction.ApplicationSpecificRole)
        self.action_Load.setObjectName("action_Load")
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.action_Help = QtGui.QAction(MainWindow)
        self.action_Help.setObjectName("action_Help")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionS_ave_as = QtGui.QAction(MainWindow)
        self.actionS_ave_as.setObjectName("actionS_ave_as")
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.importprogressions = QtGui.QAction(MainWindow)
        self.importprogressions.setObjectName("importprogressions")
        self.exportprogressions = QtGui.QAction(MainWindow)
        self.exportprogressions.setObjectName("exportprogressions")
        self.uploadsong = QtGui.QAction(MainWindow)
        self.uploadsong.setObjectName("uploadsong")
        self.uploadprogressions = QtGui.QAction(MainWindow)
        self.uploadprogressions.setObjectName("uploadprogressions")
        self.uploadinstruments = QtGui.QAction(MainWindow)
        self.uploadinstruments.setEnabled(True)
        self.uploadinstruments.setObjectName("uploadinstruments")
        self.uploadblocks = QtGui.QAction(MainWindow)
        self.uploadblocks.setEnabled(True)
        self.uploadblocks.setObjectName("uploadblocks")
        self.exportblocks = QtGui.QAction(MainWindow)
        self.exportblocks.setObjectName("exportblocks")
        self.exportinstruments = QtGui.QAction(MainWindow)
        self.exportinstruments.setObjectName("exportinstruments")
        self.importblocks = QtGui.QAction(MainWindow)
        self.importblocks.setObjectName("importblocks")
        self.importinstruments = QtGui.QAction(MainWindow)
        self.importinstruments.setObjectName("importinstruments")
        self.menuImport.addAction(self.importblocks)
        self.menuImport.addAction(self.importinstruments)
        self.menuImport.addAction(self.importprogressions)
        self.menuExport.addAction(self.exportblocks)
        self.menuExport.addAction(self.exportinstruments)
        self.menuExport.addAction(self.exportprogressions)
        self.menu_File.addAction(self.actionNew)
        self.menu_File.addAction(self.action_Load)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionS_ave_as)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menuImport.menuAction())
        self.menu_File.addAction(self.menuExport.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.action_About)
        self.menuUpload.addAction(self.uploadsong)
        self.menuUpload.addAction(self.uploadprogressions)
        self.menuUpload.addAction(self.uploadinstruments)
        self.menuUpload.addAction(self.uploadblocks)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuUpload.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label_4.setBuddy(self.projectname)
        self.label_12.setBuddy(self.author)

        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionE_xit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(self.blocks, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.editblock.click)
        QtCore.QObject.connect(self.progressions, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.editprogression.click)
        QtCore.QObject.connect(self.instruments, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.editinstrument.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.movement, self.loop)
        MainWindow.setTabOrder(self.loop, self.loopslide)
        MainWindow.setTabOrder(self.loopslide, self.bpm)
        MainWindow.setTabOrder(self.bpm, self.bpmslide)
        MainWindow.setTabOrder(self.bpmslide, self.wildness)
        MainWindow.setTabOrder(self.wildness, self.wildslide)
        MainWindow.setTabOrder(self.wildslide, self.resolution)
        MainWindow.setTabOrder(self.resolution, self.key)
        MainWindow.setTabOrder(self.key, self.duration)
        MainWindow.setTabOrder(self.duration, self.swing)
        MainWindow.setTabOrder(self.swing, self.blocks)
        MainWindow.setTabOrder(self.blocks, self.editblock)
        MainWindow.setTabOrder(self.editblock, self.upblock)
        MainWindow.setTabOrder(self.upblock, self.downblock)
        MainWindow.setTabOrder(self.downblock, self.removeblock)
        MainWindow.setTabOrder(self.removeblock, self.clearblocks)
        MainWindow.setTabOrder(self.clearblocks, self.instruments)
        MainWindow.setTabOrder(self.instruments, self.addinstrumentbutton)
        MainWindow.setTabOrder(self.addinstrumentbutton, self.editinstrument)
        MainWindow.setTabOrder(self.editinstrument, self.upinstrument)
        MainWindow.setTabOrder(self.upinstrument, self.downinstrument)
        MainWindow.setTabOrder(self.downinstrument, self.removeinstrument)
        MainWindow.setTabOrder(self.removeinstrument, self.clearinstruments)
        MainWindow.setTabOrder(self.clearinstruments, self.progressions)
        MainWindow.setTabOrder(self.progressions, self.addprogressionbutton)
        MainWindow.setTabOrder(self.addprogressionbutton, self.editprogression)
        MainWindow.setTabOrder(self.editprogression, self.copyprogression)
        MainWindow.setTabOrder(self.copyprogression, self.upprogression)
        MainWindow.setTabOrder(self.upprogression, self.downprogression)
        MainWindow.setTabOrder(self.downprogression, self.clearprogressions)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "qtImproviser - Untitled.imp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Project name", None, QtGui.QApplication.UnicodeUTF8))
        self.projectname.setText(QtGui.QApplication.translate("MainWindow", "Untitled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Global", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setStatusTip(QtGui.QApplication.translate("MainWindow", "The movement dictates the order of the blocks, progressions and instruments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Movement", None, QtGui.QApplication.UnicodeUTF8))
        self.movement.setStatusTip(QtGui.QApplication.translate("MainWindow", "The movement dictates the order of the blocks, progressions and instruments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setStatusTip(QtGui.QApplication.translate("MainWindow", "How many times the movement should be looped", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Loop", None, QtGui.QApplication.UnicodeUTF8))
        self.loop.setStatusTip(QtGui.QApplication.translate("MainWindow", "How many times the movement should be looped", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Default resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Default BPM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Default key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Default wildness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Block duration", None, QtGui.QApplication.UnicodeUTF8))
        self.duration.setStatusTip(QtGui.QApplication.translate("MainWindow", "How many times a block should be played", None, QtGui.QApplication.UnicodeUTF8))
        self.swing.setStatusTip(QtGui.QApplication.translate("MainWindow", "Swing the notes", None, QtGui.QApplication.UnicodeUTF8))
        self.swing.setText(QtGui.QApplication.translate("MainWindow", "Swing", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Movement", None, QtGui.QApplication.UnicodeUTF8))
        self.addblockbutton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeblock.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.editblock.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.clearblocks.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.copyblock.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.upblock.setText(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downblock.setText(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Blocks", None, QtGui.QApplication.UnicodeUTF8))
        self.addinstrumentbutton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeinstrument.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.editinstrument.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.clearinstruments.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.copyinstrument.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.upinstrument.setText(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downinstrument.setText(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Instruments", None, QtGui.QApplication.UnicodeUTF8))
        self.addprogressionbutton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add progression", None, QtGui.QApplication.UnicodeUTF8))
        self.addprogressionbutton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeprogression.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.editprogression.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.clearprogressions.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.copyprogression.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.upprogression.setText(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downprogression.setText(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.startbutton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start generating music", None, QtGui.QApplication.UnicodeUTF8))
        self.startbutton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.stopbutton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop generating music", None, QtGui.QApplication.UnicodeUTF8))
        self.stopbutton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuImport.setTitle(QtGui.QApplication.translate("MainWindow", "&Import", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUpload.setTitle(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load.setText(QtGui.QApplication.translate("MainWindow", "&Load", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load.setToolTip(QtGui.QApplication.translate("MainWindow", "Load a previously saved project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load.setStatusTip(QtGui.QApplication.translate("MainWindow", "Load a previously saved project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Help.setText(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionS_ave_as.setText(QtGui.QApplication.translate("MainWindow", "S&ave as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.importprogressions.setText(QtGui.QApplication.translate("MainWindow", "Progressions (*.prg)", None, QtGui.QApplication.UnicodeUTF8))
        self.exportprogressions.setText(QtGui.QApplication.translate("MainWindow", "Progressions (*.prg)", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadsong.setText(QtGui.QApplication.translate("MainWindow", "Song", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadprogressions.setText(QtGui.QApplication.translate("MainWindow", "Progressions", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadinstruments.setText(QtGui.QApplication.translate("MainWindow", "Instruments", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadblocks.setText(QtGui.QApplication.translate("MainWindow", "Blocks", None, QtGui.QApplication.UnicodeUTF8))
        self.exportblocks.setText(QtGui.QApplication.translate("MainWindow", "Blocks (*.blk)", None, QtGui.QApplication.UnicodeUTF8))
        self.exportinstruments.setText(QtGui.QApplication.translate("MainWindow", "Instruments (*.ins)", None, QtGui.QApplication.UnicodeUTF8))
        self.importblocks.setText(QtGui.QApplication.translate("MainWindow", "Blocks (*.blk)", None, QtGui.QApplication.UnicodeUTF8))
        self.importinstruments.setText(QtGui.QApplication.translate("MainWindow", "Instruments (*.ins)", None, QtGui.QApplication.UnicodeUTF8))

