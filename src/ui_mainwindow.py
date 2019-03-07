# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../forms/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 425)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/applicationIcon128"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.driveListContainer = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driveListContainer.sizePolicy().hasHeightForWidth())
        self.driveListContainer.setSizePolicy(sizePolicy)
        self.driveListContainer.setMinimumSize(QtCore.QSize(100, 0))
        self.driveListContainer.setObjectName("driveListContainer")
        self.driveListLayout = QtWidgets.QVBoxLayout(self.driveListContainer)
        self.driveListLayout.setContentsMargins(0, 0, 0, 0)
        self.driveListLayout.setObjectName("driveListLayout")
        self.driveListLabel = QtWidgets.QLabel(self.driveListContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driveListLabel.sizePolicy().hasHeightForWidth())
        self.driveListLabel.setSizePolicy(sizePolicy)
        self.driveListLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.driveListLabel.setObjectName("driveListLabel")
        self.driveListLayout.addWidget(self.driveListLabel)
        self.driveList = QtWidgets.QListView(self.driveListContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driveList.sizePolicy().hasHeightForWidth())
        self.driveList.setSizePolicy(sizePolicy)
        self.driveList.setMinimumSize(QtCore.QSize(0, 0))
        self.driveList.setBaseSize(QtCore.QSize(0, 0))
        self.driveList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.driveList.setProperty("showDropIndicator", False)
        self.driveList.setIconSize(QtCore.QSize(24, 24))
        self.driveList.setObjectName("driveList")
        self.driveListLayout.addWidget(self.driveList)
        self.terminalLogContainer = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminalLogContainer.sizePolicy().hasHeightForWidth())
        self.terminalLogContainer.setSizePolicy(sizePolicy)
        self.terminalLogContainer.setMinimumSize(QtCore.QSize(250, 0))
        self.terminalLogContainer.setObjectName("terminalLogContainer")
        self.terminalListLayout = QtWidgets.QVBoxLayout(self.terminalLogContainer)
        self.terminalListLayout.setContentsMargins(0, 0, 0, 0)
        self.terminalListLayout.setSpacing(6)
        self.terminalListLayout.setObjectName("terminalListLayout")
        self.terminalLogLabel = QtWidgets.QLabel(self.terminalLogContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminalLogLabel.sizePolicy().hasHeightForWidth())
        self.terminalLogLabel.setSizePolicy(sizePolicy)
        self.terminalLogLabel.setObjectName("terminalLogLabel")
        self.terminalListLayout.addWidget(self.terminalLogLabel)
        self.terminalLogWindow = QtWidgets.QPlainTextEdit(self.terminalLogContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminalLogWindow.sizePolicy().hasHeightForWidth())
        self.terminalLogWindow.setSizePolicy(sizePolicy)
        self.terminalLogWindow.setMinimumSize(QtCore.QSize(250, 0))
        self.terminalLogWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.terminalLogWindow.setDocumentTitle("")
        self.terminalLogWindow.setUndoRedoEnabled(False)
        self.terminalLogWindow.setReadOnly(True)
        self.terminalLogWindow.setPlainText("")
        self.terminalLogWindow.setObjectName("terminalLogWindow")
        self.terminalListLayout.addWidget(self.terminalLogWindow)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 676, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuDrive = QtWidgets.QMenu(self.menuBar)
        self.menuDrive.setObjectName("menuDrive")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/refresh"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon1)
        self.actionRefresh.setWhatsThis("")
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionWriteDatabase = QtWidgets.QAction(MainWindow)
        self.actionWriteDatabase.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/write"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWriteDatabase.setIcon(icon2)
        self.actionWriteDatabase.setObjectName("actionWriteDatabase")
        self.actionViewDatabase = QtWidgets.QAction(MainWindow)
        self.actionViewDatabase.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewDatabase.setIcon(icon3)
        self.actionViewDatabase.setObjectName("actionViewDatabase")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/info"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClearLog = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/clear"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearLog.setIcon(icon5)
        self.actionClearLog.setObjectName("actionClearLog")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/actions/preferences"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon6)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionViewOnGithub = QtWidgets.QAction(MainWindow)
        self.actionViewOnGithub.setObjectName("actionViewOnGithub")
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionWriteDatabase)
        self.toolBar.addAction(self.actionViewDatabase)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClearLog)
        self.menuDrive.addAction(self.actionWriteDatabase)
        self.menuDrive.addAction(self.actionRefresh)
        self.menuDrive.addAction(self.actionViewDatabase)
        self.menuDrive.addSeparator()
        self.menuDrive.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionClearLog)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionViewOnGithub)
        self.menuBar.addAction(self.menuDrive.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.driveListLabel.setBuddy(self.driveList)
        self.terminalLogLabel.setBuddy(self.terminalLogWindow)

        self.retranslateUi(MainWindow)
        self.actionRefresh.triggered.connect(MainWindow.refreshActionTriggered)
        self.actionViewDatabase.triggered.connect(MainWindow.viewDatabaseActionTriggered)
        self.terminalLogWindow.customContextMenuRequested['QPoint'].connect(MainWindow.terminalLogCustomContextMenuRequested)
        self.actionClearLog.triggered.connect(MainWindow.clearLogActionTriggered)
        self.actionWriteDatabase.triggered.connect(MainWindow.writeDatabaseActionTriggered)
        self.actionAbout.triggered.connect(MainWindow.aboutActionTriggered)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionViewOnGithub.triggered.connect(MainWindow.viewOnGithubActionTriggered)
        self.actionPreferences.triggered.connect(MainWindow.preferencesActionTriggered)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kenwood Database Generator"))
        self.driveListLabel.setText(_translate("MainWindow", "&USB Drives"))
        self.terminalLogLabel.setText(_translate("MainWindow", "Terminal &Output"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuDrive.setTitle(_translate("MainWindow", "&Drive"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionRefresh.setText(_translate("MainWindow", "&Refresh"))
        self.actionRefresh.setToolTip(_translate("MainWindow", "Refresh Drive List"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionWriteDatabase.setText(_translate("MainWindow", "&Write Database"))
        self.actionWriteDatabase.setToolTip(_translate("MainWindow", "Write Database to Drive"))
        self.actionWriteDatabase.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionViewDatabase.setText(_translate("MainWindow", "&View Database"))
        self.actionViewDatabase.setIconText(_translate("MainWindow", "View"))
        self.actionViewDatabase.setToolTip(_translate("MainWindow", "View Database on Drive"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionClearLog.setText(_translate("MainWindow", "C&lear Output"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPreferences.setText(_translate("MainWindow", "&Preferences..."))
        self.actionPreferences.setIconText(_translate("MainWindow", "Preferences..."))
        self.actionPreferences.setToolTip(_translate("MainWindow", "Edit Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionViewOnGithub.setText(_translate("MainWindow", "&View Repository on Github"))
        self.actionViewOnGithub.setIconText(_translate("MainWindow", "View on Github"))


import appresources_rc
