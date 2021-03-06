# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pcvform.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyCamViewer(object):
    def setupUi(self, PyCamViewer):
        PyCamViewer.setObjectName("PyCamViewer")
        PyCamViewer.resize(596, 534)
        self.centralWidget = QtWidgets.QWidget(PyCamViewer)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageLabel = QtWidgets.QLabel(self.centralWidget)
        self.imageLabel.setMinimumSize(QtCore.QSize(0, 300))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout.addWidget(self.imageLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ipAddress = QtWidgets.QLineEdit(self.groupBox)
        self.ipAddress.setObjectName("ipAddress")
        self.horizontalLayout.addWidget(self.ipAddress)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.port = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port.sizePolicy().hasHeightForWidth())
        self.port.setSizePolicy(sizePolicy)
        self.port.setMinimumSize(QtCore.QSize(100, 0))
        self.port.setMaximumSize(QtCore.QSize(80, 16777215))
        self.port.setInputMethodHints(QtCore.Qt.ImhNone)
        self.port.setMaxLength(5)
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.startServerButton = QtWidgets.QPushButton(self.groupBox)
        self.startServerButton.setCheckable(True)
        self.startServerButton.setObjectName("startServerButton")
        self.horizontalLayout.addWidget(self.startServerButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.streamingButton = QtWidgets.QPushButton(self.groupBox_2)
        self.streamingButton.setCheckable(True)
        self.streamingButton.setObjectName("streamingButton")
        self.horizontalLayout_2.addWidget(self.streamingButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.shutterSlider = QtWidgets.QSlider(self.groupBox_3)
        self.shutterSlider.setMinimum(1)
        self.shutterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.shutterSlider.setObjectName("shutterSlider")
        self.horizontalLayout_3.addWidget(self.shutterSlider)
        self.shutterValue = QtWidgets.QLabel(self.groupBox_3)
        self.shutterValue.setObjectName("shutterValue")
        self.horizontalLayout_3.addWidget(self.shutterValue)
        self.verticalLayout.addWidget(self.groupBox_3)
        PyCamViewer.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(PyCamViewer)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 596, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuPyCamViewer = QtWidgets.QMenu(self.menuBar)
        self.menuPyCamViewer.setObjectName("menuPyCamViewer")
        PyCamViewer.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(PyCamViewer)
        self.mainToolBar.setObjectName("mainToolBar")
        PyCamViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(PyCamViewer)
        self.statusBar.setObjectName("statusBar")
        PyCamViewer.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(PyCamViewer)
        self.actionQuit.setObjectName("actionQuit")
        self.menuPyCamViewer.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuPyCamViewer.menuAction())

        self.retranslateUi(PyCamViewer)
        self.startServerButton.clicked['bool'].connect(PyCamViewer.startServer)
        self.actionQuit.triggered.connect(PyCamViewer.close)
        self.streamingButton.clicked['bool'].connect(PyCamViewer.startStreaming)
        self.shutterSlider.valueChanged['int'].connect(self.shutterValue.setNum)
        self.shutterSlider.valueChanged['int'].connect(PyCamViewer.setShutter)
        QtCore.QMetaObject.connectSlotsByName(PyCamViewer)

    def retranslateUi(self, PyCamViewer):
        _translate = QtCore.QCoreApplication.translate
        PyCamViewer.setWindowTitle(_translate("PyCamViewer", "PyCamViewer"))
        self.imageLabel.setText(_translate("PyCamViewer", "image"))
        self.groupBox.setTitle(_translate("PyCamViewer", "Connect to Camera"))
        self.ipAddress.setPlaceholderText(_translate("PyCamViewer", "IP Address"))
        self.label.setText(_translate("PyCamViewer", ":"))
        self.port.setPlaceholderText(_translate("PyCamViewer", "Port"))
        self.startServerButton.setText(_translate("PyCamViewer", "Connect"))
        self.groupBox_2.setTitle(_translate("PyCamViewer", "Streaming"))
        self.streamingButton.setText(_translate("PyCamViewer", "Start Streaming"))
        self.groupBox_3.setTitle(_translate("PyCamViewer", "Sensor Values"))
        self.label_2.setText(_translate("PyCamViewer", "Shutter:"))
        self.shutterValue.setText(_translate("PyCamViewer", "1"))
        self.menuPyCamViewer.setTitle(_translate("PyCamViewer", "PyCamViewer"))
        self.actionQuit.setText(_translate("PyCamViewer", "Quit"))

