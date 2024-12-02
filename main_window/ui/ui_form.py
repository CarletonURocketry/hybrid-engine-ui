# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
from . import rc_resources

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1288, 892)
        icon = QIcon()
        icon.addFile(u"logos/better_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 15, 20, 20)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.telemetryTab = QWidget()
        self.telemetryTab.setObjectName(u"telemetryTab")
        self.telemetryTab.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.telemetryTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.controlLayout = QHBoxLayout()
        self.controlLayout.setObjectName(u"controlLayout")
        self.controlLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.logoLabel = QLabel(self.telemetryTab)
        self.logoLabel.setObjectName(u"logoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)
        self.logoLabel.setMinimumSize(QSize(127, 90))
        self.logoLabel.setMaximumSize(QSize(127, 90))
        self.logoLabel.setPixmap(QPixmap(u":/images/logos/logoandtexttransparentsmol.png"))
        self.logoLabel.setScaledContents(True)

        self.controlLayout.addWidget(self.logoLabel)

        self.connectionLayout_2 = QVBoxLayout()
        self.connectionLayout_2.setObjectName(u"connectionLayout_2")
        self.addressLayout_10 = QHBoxLayout()
        self.addressLayout_10.setSpacing(1)
        self.addressLayout_10.setObjectName(u"addressLayout_10")
        self.udpIpAddressLabel_10 = QLabel(self.telemetryTab)
        self.udpIpAddressLabel_10.setObjectName(u"udpIpAddressLabel_10")

        self.addressLayout_10.addWidget(self.udpIpAddressLabel_10)

        self.udpIpAddressInput_10 = QLineEdit(self.telemetryTab)
        self.udpIpAddressInput_10.setObjectName(u"udpIpAddressInput_10")
        self.udpIpAddressInput_10.setStyleSheet(u"")

        self.addressLayout_10.addWidget(self.udpIpAddressInput_10)


        self.connectionLayout_2.addLayout(self.addressLayout_10)

        self.portLayout_10 = QHBoxLayout()
        self.portLayout_10.setSpacing(6)
        self.portLayout_10.setObjectName(u"portLayout_10")
        self.portLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.udpPortLabel_10 = QLabel(self.telemetryTab)
        self.udpPortLabel_10.setObjectName(u"udpPortLabel_10")
        self.udpPortLabel_10.setMinimumSize(QSize(85, 0))

        self.portLayout_10.addWidget(self.udpPortLabel_10)

        self.udpPortInput_10 = QLineEdit(self.telemetryTab)
        self.udpPortInput_10.setObjectName(u"udpPortInput_10")
        self.udpPortInput_10.setStyleSheet(u"")

        self.portLayout_10.addWidget(self.udpPortInput_10)


        self.connectionLayout_2.addLayout(self.portLayout_10)

        self.interfaceLayout_10 = QHBoxLayout()
        self.interfaceLayout_10.setObjectName(u"interfaceLayout_10")
        self.interfaceAddressLabel_10 = QLabel(self.telemetryTab)
        self.interfaceAddressLabel_10.setObjectName(u"interfaceAddressLabel_10")

        self.interfaceLayout_10.addWidget(self.interfaceAddressLabel_10)

        self.interfaceAddressDropdown_10 = QComboBox(self.telemetryTab)
        self.interfaceAddressDropdown_10.setObjectName(u"interfaceAddressDropdown_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.interfaceAddressDropdown_10.sizePolicy().hasHeightForWidth())
        self.interfaceAddressDropdown_10.setSizePolicy(sizePolicy1)

        self.interfaceLayout_10.addWidget(self.interfaceAddressDropdown_10)


        self.connectionLayout_2.addLayout(self.interfaceLayout_10)

        self.udpConnectButton_10 = QPushButton(self.telemetryTab)
        self.udpConnectButton_10.setObjectName(u"udpConnectButton_10")
        self.udpConnectButton_10.setMaximumSize(QSize(1000, 16777215))
        self.udpConnectButton_10.setStyleSheet(u"")

        self.connectionLayout_2.addWidget(self.udpConnectButton_10)

        self.openFileButton = QPushButton(self.telemetryTab)
        self.openFileButton.setObjectName(u"openFileButton")

        self.connectionLayout_2.addWidget(self.openFileButton)


        self.controlLayout.addLayout(self.connectionLayout_2)

        self.logLayout = QVBoxLayout()
        self.logLayout.setSpacing(6)
        self.logLayout.setObjectName(u"logLayout")
        self.logOutput = QTextBrowser(self.telemetryTab)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setMaximumSize(QSize(16777215, 110))
        self.logOutput.setStyleSheet(u"")

        self.logLayout.addWidget(self.logOutput)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.recordingToggleButton = QRadioButton(self.telemetryTab)
        self.recordingToggleButton.setObjectName(u"recordingToggleButton")

        self.horizontalLayout_2.addWidget(self.recordingToggleButton)

        self.exporter = QPushButton(self.telemetryTab)
        self.exporter.setObjectName(u"exporter")

        self.horizontalLayout_2.addWidget(self.exporter)


        self.logLayout.addLayout(self.horizontalLayout_2)

        self.logLayout.setStretch(0, 1)

        self.controlLayout.addLayout(self.logLayout)

        self.valveStatusLayout = QFormLayout()
        self.valveStatusLayout.setObjectName(u"valveStatusLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.xv5 = QLabel(self.telemetryTab)
        self.xv5.setObjectName(u"xv5")
        font = QFont()
        font.setPointSize(12)
        self.xv5.setFont(font)

        self.gridLayout_2.addWidget(self.xv5, 2, 2, 1, 1)

        self.xv8State = QLabel(self.telemetryTab)
        self.xv8State.setObjectName(u"xv8State")
        self.xv8State.setMinimumSize(QSize(50, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.xv8State.setFont(font1)
        self.xv8State.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv8State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv8State, 3, 3, 1, 1)

        self.quickDisconnect = QLabel(self.telemetryTab)
        self.quickDisconnect.setObjectName(u"quickDisconnect")
        self.quickDisconnect.setMinimumSize(QSize(80, 23))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.quickDisconnect.setFont(font2)

        self.gridLayout_2.addWidget(self.quickDisconnect, 0, 0, 1, 1)

        self.xv6State = QLabel(self.telemetryTab)
        self.xv6State.setObjectName(u"xv6State")
        self.xv6State.setFont(font1)
        self.xv6State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv6State, 2, 5, 1, 1)

        self.xv3 = QLabel(self.telemetryTab)
        self.xv3.setObjectName(u"xv3")
        self.xv3.setFont(font)

        self.gridLayout_2.addWidget(self.xv3, 1, 4, 1, 1)

        self.xv11 = QLabel(self.telemetryTab)
        self.xv11.setObjectName(u"xv11")
        self.xv11.setFont(font)

        self.gridLayout_2.addWidget(self.xv11, 4, 2, 1, 1)

        self.xv7State = QLabel(self.telemetryTab)
        self.xv7State.setObjectName(u"xv7State")
        self.xv7State.setMinimumSize(QSize(50, 0))
        self.xv7State.setFont(font1)
        self.xv7State.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv7State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv7State, 3, 1, 1, 1)

        self.xv1State = QLabel(self.telemetryTab)
        self.xv1State.setObjectName(u"xv1State")
        self.xv1State.setFont(font1)
        self.xv1State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv1State, 1, 1, 1, 1)

        self.xv1 = QLabel(self.telemetryTab)
        self.xv1.setObjectName(u"xv1")
        self.xv1.setMinimumSize(QSize(80, 23))
        self.xv1.setFont(font2)

        self.gridLayout_2.addWidget(self.xv1, 1, 0, 1, 1)

        self.xv4State = QLabel(self.telemetryTab)
        self.xv4State.setObjectName(u"xv4State")
        self.xv4State.setMinimumSize(QSize(50, 0))
        self.xv4State.setFont(font1)
        self.xv4State.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv4State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv4State, 2, 1, 1, 1)

        self.xv5State = QLabel(self.telemetryTab)
        self.xv5State.setObjectName(u"xv5State")
        self.xv5State.setFont(font1)
        self.xv5State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv5State, 2, 3, 1, 1)

        self.igniter = QLabel(self.telemetryTab)
        self.igniter.setObjectName(u"igniter")
        self.igniter.setFont(font)

        self.gridLayout_2.addWidget(self.igniter, 0, 4, 1, 1)

        self.xv11State = QLabel(self.telemetryTab)
        self.xv11State.setObjectName(u"xv11State")
        self.xv11State.setFont(font1)
        self.xv11State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv11State, 4, 3, 1, 1)

        self.igniterState = QLabel(self.telemetryTab)
        self.igniterState.setObjectName(u"igniterState")
        self.igniterState.setFont(font1)
        self.igniterState.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.igniterState, 0, 5, 1, 1)

        self.xv6 = QLabel(self.telemetryTab)
        self.xv6.setObjectName(u"xv6")
        self.xv6.setFont(font)

        self.gridLayout_2.addWidget(self.xv6, 2, 4, 1, 1)

        self.xv12 = QLabel(self.telemetryTab)
        self.xv12.setObjectName(u"xv12")
        self.xv12.setFont(font)

        self.gridLayout_2.addWidget(self.xv12, 4, 4, 1, 1)

        self.quickDisconnectState = QLabel(self.telemetryTab)
        self.quickDisconnectState.setObjectName(u"quickDisconnectState")
        self.quickDisconnectState.setMinimumSize(QSize(50, 0))
        self.quickDisconnectState.setFont(font1)
        self.quickDisconnectState.setAutoFillBackground(False)
        self.quickDisconnectState.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.quickDisconnectState.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.quickDisconnectState, 0, 1, 1, 1)

        self.cv1 = QLabel(self.telemetryTab)
        self.cv1.setObjectName(u"cv1")
        self.cv1.setMinimumSize(QSize(80, 0))
        self.cv1.setFont(font2)
        self.cv1.setIndent(-1)

        self.gridLayout_2.addWidget(self.cv1, 0, 2, 1, 1)

        self.xv4 = QLabel(self.telemetryTab)
        self.xv4.setObjectName(u"xv4")
        self.xv4.setFont(font)

        self.gridLayout_2.addWidget(self.xv4, 2, 0, 1, 1)

        self.xv10State = QLabel(self.telemetryTab)
        self.xv10State.setObjectName(u"xv10State")
        self.xv10State.setFont(font1)
        self.xv10State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv10State, 4, 1, 1, 1)

        self.xv9State = QLabel(self.telemetryTab)
        self.xv9State.setObjectName(u"xv9State")
        self.xv9State.setFont(font1)
        self.xv9State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv9State, 3, 5, 1, 1)

        self.xv3State = QLabel(self.telemetryTab)
        self.xv3State.setObjectName(u"xv3State")
        self.xv3State.setFont(font1)
        self.xv3State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv3State, 1, 5, 1, 1)

        self.xv10 = QLabel(self.telemetryTab)
        self.xv10.setObjectName(u"xv10")
        self.xv10.setFont(font)

        self.gridLayout_2.addWidget(self.xv10, 4, 0, 1, 1)

        self.xv2State = QLabel(self.telemetryTab)
        self.xv2State.setObjectName(u"xv2State")
        self.xv2State.setMinimumSize(QSize(50, 0))
        self.xv2State.setFont(font1)
        self.xv2State.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv2State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv2State, 1, 3, 1, 1)

        self.cv1State = QLabel(self.telemetryTab)
        self.cv1State.setObjectName(u"cv1State")
        self.cv1State.setMinimumSize(QSize(50, 0))
        self.cv1State.setFont(font1)
        self.cv1State.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.cv1State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.cv1State, 0, 3, 1, 1)

        self.xv2 = QLabel(self.telemetryTab)
        self.xv2.setObjectName(u"xv2")
        self.xv2.setMinimumSize(QSize(80, 0))
        self.xv2.setFont(font2)
        self.xv2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.xv2.setIndent(10)

        self.gridLayout_2.addWidget(self.xv2, 1, 2, 1, 1)

        self.xv7 = QLabel(self.telemetryTab)
        self.xv7.setObjectName(u"xv7")
        self.xv7.setMinimumSize(QSize(80, 23))
        self.xv7.setFont(font2)

        self.gridLayout_2.addWidget(self.xv7, 3, 0, 1, 1)

        self.xv12State = QLabel(self.telemetryTab)
        self.xv12State.setObjectName(u"xv12State")
        self.xv12State.setFont(font1)
        self.xv12State.setStyleSheet(u"background-color: rgb(255, 80, 80);")

        self.gridLayout_2.addWidget(self.xv12State, 4, 5, 1, 1)

        self.xv9 = QLabel(self.telemetryTab)
        self.xv9.setObjectName(u"xv9")
        self.xv9.setFont(font)

        self.gridLayout_2.addWidget(self.xv9, 3, 4, 1, 1)

        self.xv8 = QLabel(self.telemetryTab)
        self.xv8.setObjectName(u"xv8")
        self.xv8.setMinimumSize(QSize(80, 0))
        self.xv8.setFont(font2)
        self.xv8.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.xv8.setIndent(10)

        self.gridLayout_2.addWidget(self.xv8, 3, 2, 1, 1)


        self.valveStatusLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout_2)


        self.controlLayout.addLayout(self.valveStatusLayout)

        self.controlLayout.setStretch(0, 3)
        self.controlLayout.setStretch(1, 2)
        self.controlLayout.setStretch(2, 4)

        self.verticalLayout.addLayout(self.controlLayout)

        self.plotLayout = QGridLayout()
        self.plotLayout.setSpacing(20)
        self.plotLayout.setObjectName(u"plotLayout")
        self.pressurePlot = PlotWidget(self.telemetryTab)
        self.pressurePlot.setObjectName(u"pressurePlot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pressurePlot.sizePolicy().hasHeightForWidth())
        self.pressurePlot.setSizePolicy(sizePolicy2)
        self.pressurePlot.setAutoFillBackground(False)
        brush = QBrush(QColor(240, 240, 240, 255))
        brush.setStyle(Qt.SolidPattern)
        self.pressurePlot.setBackgroundBrush(brush)

        self.plotLayout.addWidget(self.pressurePlot, 0, 0, 1, 1)

        self.temperaturePlot = PlotWidget(self.telemetryTab)
        self.temperaturePlot.setObjectName(u"temperaturePlot")
        self.temperaturePlot.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.temperaturePlot.setForegroundBrush(brush1)

        self.plotLayout.addWidget(self.temperaturePlot, 0, 1, 1, 1)

        self.engineThrustPlot = PlotWidget(self.telemetryTab)
        self.engineThrustPlot.setObjectName(u"engineThrustPlot")
        self.engineThrustPlot.setBackgroundBrush(brush)

        self.plotLayout.addWidget(self.engineThrustPlot, 1, 1, 1, 1)

        self.tankMassPlot = PlotWidget(self.telemetryTab)
        self.tankMassPlot.setObjectName(u"tankMassPlot")
        self.tankMassPlot.setBackgroundBrush(brush)

        self.plotLayout.addWidget(self.tankMassPlot, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.plotLayout)

        self.tabWidget.addTab(self.telemetryTab, "")
        self.configurationTab = QWidget()
        self.configurationTab.setObjectName(u"configurationTab")
        self.configurationTab.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.configurationTab.setAutoFillBackground(True)
        self.formLayout = QFormLayout(self.configurationTab)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(450, 0, 450, 10)
        self.connectionLayout = QVBoxLayout()
        self.connectionLayout.setObjectName(u"connectionLayout")
        self.multicastConfigLabel = QLabel(self.configurationTab)
        self.multicastConfigLabel.setObjectName(u"multicastConfigLabel")
        font3 = QFont()
        font3.setBold(True)
        self.multicastConfigLabel.setFont(font3)
        self.multicastConfigLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.connectionLayout.addWidget(self.multicastConfigLabel)

        self.addressLayout = QHBoxLayout()
        self.addressLayout.setObjectName(u"addressLayout")
        self.udpIpAddressLabel = QLabel(self.configurationTab)
        self.udpIpAddressLabel.setObjectName(u"udpIpAddressLabel")

        self.addressLayout.addWidget(self.udpIpAddressLabel)

        self.udpIpAddressInput = QLineEdit(self.configurationTab)
        self.udpIpAddressInput.setObjectName(u"udpIpAddressInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.udpIpAddressInput.sizePolicy().hasHeightForWidth())
        self.udpIpAddressInput.setSizePolicy(sizePolicy3)

        self.addressLayout.addWidget(self.udpIpAddressInput)


        self.connectionLayout.addLayout(self.addressLayout)

        self.portLayout = QHBoxLayout()
        self.portLayout.setObjectName(u"portLayout")
        self.udpPortLabel = QLabel(self.configurationTab)
        self.udpPortLabel.setObjectName(u"udpPortLabel")
        self.udpPortLabel.setMinimumSize(QSize(85, 0))

        self.portLayout.addWidget(self.udpPortLabel)

        self.udpPortInput = QLineEdit(self.configurationTab)
        self.udpPortInput.setObjectName(u"udpPortInput")
        sizePolicy3.setHeightForWidth(self.udpPortInput.sizePolicy().hasHeightForWidth())
        self.udpPortInput.setSizePolicy(sizePolicy3)
        self.udpPortInput.setStyleSheet(u"")

        self.portLayout.addWidget(self.udpPortInput)


        self.connectionLayout.addLayout(self.portLayout)

        self.interfaceLayout = QHBoxLayout()
        self.interfaceLayout.setObjectName(u"interfaceLayout")
        self.interfaceAddressLabel = QLabel(self.configurationTab)
        self.interfaceAddressLabel.setObjectName(u"interfaceAddressLabel")

        self.interfaceLayout.addWidget(self.interfaceAddressLabel)

        self.interfaceAddressDropdown = QComboBox(self.configurationTab)
        self.interfaceAddressDropdown.setObjectName(u"interfaceAddressDropdown")

        self.interfaceLayout.addWidget(self.interfaceAddressDropdown)


        self.connectionLayout.addLayout(self.interfaceLayout)

        self.udpConnectButton = QPushButton(self.configurationTab)
        self.udpConnectButton.setObjectName(u"udpConnectButton")
        self.udpConnectButton.setStyleSheet(u"")

        self.connectionLayout.addWidget(self.udpConnectButton)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.connectionLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer)

        self.serialLayout_2 = QVBoxLayout()
        self.serialLayout_2.setObjectName(u"serialLayout_2")
        self.serialConfigLabel = QLabel(self.configurationTab)
        self.serialConfigLabel.setObjectName(u"serialConfigLabel")
        self.serialConfigLabel.setFont(font3)
        self.serialConfigLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.serialLayout_2.addWidget(self.serialConfigLabel)

        self.serialLayout = QHBoxLayout()
        self.serialLayout.setObjectName(u"serialLayout")
        self.serialPortLabel = QLabel(self.configurationTab)
        self.serialPortLabel.setObjectName(u"serialPortLabel")

        self.serialLayout.addWidget(self.serialPortLabel)

        self.serialPortDropdown = QComboBox(self.configurationTab)
        self.serialPortDropdown.setObjectName(u"serialPortDropdown")

        self.serialLayout.addWidget(self.serialPortDropdown)


        self.serialLayout_2.addLayout(self.serialLayout)

        self.serialConnectButton = QPushButton(self.configurationTab)
        self.serialConnectButton.setObjectName(u"serialConnectButton")
        self.serialConnectButton.setStyleSheet(u"")

        self.serialLayout_2.addWidget(self.serialConnectButton)


        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.serialLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pressureThresholdLayot = QVBoxLayout()
        self.pressureThresholdLayot.setObjectName(u"pressureThresholdLayot")
        self.pressureThresholdLabel = QLabel(self.configurationTab)
        self.pressureThresholdLabel.setObjectName(u"pressureThresholdLabel")

        self.pressureThresholdLayot.addWidget(self.pressureThresholdLabel)

        self.pressureThresholdList = QListWidget(self.configurationTab)
        self.pressureThresholdList.setObjectName(u"pressureThresholdList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pressureThresholdList.sizePolicy().hasHeightForWidth())
        self.pressureThresholdList.setSizePolicy(sizePolicy4)
        self.pressureThresholdList.setMaximumSize(QSize(16777215, 75))

        self.pressureThresholdLayot.addWidget(self.pressureThresholdList)

        self.pressureThresholdInput = QLineEdit(self.configurationTab)
        self.pressureThresholdInput.setObjectName(u"pressureThresholdInput")
        sizePolicy1.setHeightForWidth(self.pressureThresholdInput.sizePolicy().hasHeightForWidth())
        self.pressureThresholdInput.setSizePolicy(sizePolicy1)

        self.pressureThresholdLayot.addWidget(self.pressureThresholdInput)

        self.pressureThresholdButton = QPushButton(self.configurationTab)
        self.pressureThresholdButton.setObjectName(u"pressureThresholdButton")
        sizePolicy1.setHeightForWidth(self.pressureThresholdButton.sizePolicy().hasHeightForWidth())
        self.pressureThresholdButton.setSizePolicy(sizePolicy1)

        self.pressureThresholdLayot.addWidget(self.pressureThresholdButton)


        self.gridLayout.addLayout(self.pressureThresholdLayot, 1, 0, 1, 1)

        self.engineThrustThreshold = QVBoxLayout()
        self.engineThrustThreshold.setObjectName(u"engineThrustThreshold")
        self.engineThrustThresholdLabel = QLabel(self.configurationTab)
        self.engineThrustThresholdLabel.setObjectName(u"engineThrustThresholdLabel")

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdLabel)

        self.engineThrustThresholdList = QListWidget(self.configurationTab)
        self.engineThrustThresholdList.setObjectName(u"engineThrustThresholdList")
        sizePolicy1.setHeightForWidth(self.engineThrustThresholdList.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdList.setSizePolicy(sizePolicy1)
        self.engineThrustThresholdList.setMaximumSize(QSize(16777215, 75))

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdList)

        self.engineThrustThresholdInput = QLineEdit(self.configurationTab)
        self.engineThrustThresholdInput.setObjectName(u"engineThrustThresholdInput")
        sizePolicy1.setHeightForWidth(self.engineThrustThresholdInput.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdInput.setSizePolicy(sizePolicy1)

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdInput)

        self.engineThrustThresholdButton = QPushButton(self.configurationTab)
        self.engineThrustThresholdButton.setObjectName(u"engineThrustThresholdButton")
        sizePolicy1.setHeightForWidth(self.engineThrustThresholdButton.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdButton.setSizePolicy(sizePolicy1)

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdButton)


        self.gridLayout.addLayout(self.engineThrustThreshold, 2, 1, 1, 1)

        self.temperatureThresholdLayout = QVBoxLayout()
        self.temperatureThresholdLayout.setObjectName(u"temperatureThresholdLayout")
        self.temperatureThresholdLabel = QLabel(self.configurationTab)
        self.temperatureThresholdLabel.setObjectName(u"temperatureThresholdLabel")

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdLabel)

        self.temperatureThresholdList = QListWidget(self.configurationTab)
        self.temperatureThresholdList.setObjectName(u"temperatureThresholdList")
        sizePolicy1.setHeightForWidth(self.temperatureThresholdList.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdList.setSizePolicy(sizePolicy1)
        self.temperatureThresholdList.setMaximumSize(QSize(16777215, 75))

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdList)

        self.temperatureThresholdInput = QLineEdit(self.configurationTab)
        self.temperatureThresholdInput.setObjectName(u"temperatureThresholdInput")
        sizePolicy1.setHeightForWidth(self.temperatureThresholdInput.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdInput.setSizePolicy(sizePolicy1)

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdInput)

        self.temperatureThresholdButton = QPushButton(self.configurationTab)
        self.temperatureThresholdButton.setObjectName(u"temperatureThresholdButton")
        sizePolicy1.setHeightForWidth(self.temperatureThresholdButton.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdButton.setSizePolicy(sizePolicy1)

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdButton)


        self.gridLayout.addLayout(self.temperatureThresholdLayout, 1, 1, 1, 1)

        self.tankMassThresholdLayout = QVBoxLayout()
        self.tankMassThresholdLayout.setObjectName(u"tankMassThresholdLayout")
        self.tankMassThresholdLabel = QLabel(self.configurationTab)
        self.tankMassThresholdLabel.setObjectName(u"tankMassThresholdLabel")

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdLabel)

        self.tankMassThresholdList = QListWidget(self.configurationTab)
        self.tankMassThresholdList.setObjectName(u"tankMassThresholdList")
        sizePolicy1.setHeightForWidth(self.tankMassThresholdList.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdList.setSizePolicy(sizePolicy1)
        self.tankMassThresholdList.setMaximumSize(QSize(16777215, 75))

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdList)

        self.tankMassThresholdInput = QLineEdit(self.configurationTab)
        self.tankMassThresholdInput.setObjectName(u"tankMassThresholdInput")
        sizePolicy1.setHeightForWidth(self.tankMassThresholdInput.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdInput.setSizePolicy(sizePolicy1)

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdInput)

        self.tankMassThresholdButton = QPushButton(self.configurationTab)
        self.tankMassThresholdButton.setObjectName(u"tankMassThresholdButton")
        sizePolicy1.setHeightForWidth(self.tankMassThresholdButton.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdButton.setSizePolicy(sizePolicy1)

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdButton)


        self.gridLayout.addLayout(self.tankMassThresholdLayout, 2, 0, 1, 1)

        self.graphThresholdLabel = QLabel(self.configurationTab)
        self.graphThresholdLabel.setObjectName(u"graphThresholdLabel")
        self.graphThresholdLabel.setFont(font3)
        self.graphThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.graphThresholdLabel, 0, 0, 1, 2)


        self.formLayout.setLayout(4, QFormLayout.SpanningRole, self.gridLayout)

        self.saveConfigButton = QPushButton(self.configurationTab)
        self.saveConfigButton.setObjectName(u"saveConfigButton")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.saveConfigButton)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.tabWidget.addTab(self.configurationTab, "")
        self.pAndIdTab = QWidget()
        self.pAndIdTab.setObjectName(u"pAndIdTab")
        self.pid_image = QLabel(self.pAndIdTab)
        self.pid_image.setObjectName(u"pid_image")
        self.pid_image.setGeometry(QRect(0, 10, 1261, 691))
        self.pid_image.setPixmap(QPixmap(u":/images/logos/PID hybrid.jpg"))
        self.pid_image.setScaledContents(True)
        self.cv1State_tabpid = QLabel(self.pAndIdTab)
        self.cv1State_tabpid.setObjectName(u"cv1State_tabpid")
        self.cv1State_tabpid.setGeometry(QRect(940, 390, 74, 37))
        self.cv1State_tabpid.setMinimumSize(QSize(50, 0))
        self.cv1State_tabpid.setFont(font1)
        self.cv1State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.cv1State_tabpid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.xv1State_tabpid = QLabel(self.pAndIdTab)
        self.xv1State_tabpid.setObjectName(u"xv1State_tabpid")
        self.xv1State_tabpid.setGeometry(QRect(280, 420, 74, 37))
        self.xv1State_tabpid.setFont(font1)
        self.xv1State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv1State_tabpid.setIndent(8)
        self.xv2State_tabpid = QLabel(self.pAndIdTab)
        self.xv2State_tabpid.setObjectName(u"xv2State_tabpid")
        self.xv2State_tabpid.setGeometry(QRect(400, 290, 74, 37))
        self.xv2State_tabpid.setMinimumSize(QSize(50, 0))
        self.xv2State_tabpid.setFont(font1)
        self.xv2State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv2State_tabpid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.xv3State_tabpid = QLabel(self.pAndIdTab)
        self.xv3State_tabpid.setObjectName(u"xv3State_tabpid")
        self.xv3State_tabpid.setGeometry(QRect(500, 510, 74, 37))
        self.xv3State_tabpid.setFont(font1)
        self.xv3State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv3State_tabpid.setIndent(8)
        self.xv4State_tabpid = QLabel(self.pAndIdTab)
        self.xv4State_tabpid.setObjectName(u"xv4State_tabpid")
        self.xv4State_tabpid.setGeometry(QRect(730, 130, 74, 36))
        self.xv4State_tabpid.setMinimumSize(QSize(50, 0))
        self.xv4State_tabpid.setFont(font1)
        self.xv4State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv4State_tabpid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.pAndIdTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.logoLabel.setText("")
#if QT_CONFIG(tooltip)
        self.udpIpAddressLabel_10.setToolTip(QCoreApplication.translate("Widget", u"Address of multicast group", None))
#endif // QT_CONFIG(tooltip)
        self.udpIpAddressLabel_10.setText(QCoreApplication.translate("Widget", u"MCast IPv4 address*: ", None))
#if QT_CONFIG(tooltip)
        self.udpPortLabel_10.setToolTip(QCoreApplication.translate("Widget", u"Port of multicast group", None))
#endif // QT_CONFIG(tooltip)
        self.udpPortLabel_10.setText(QCoreApplication.translate("Widget", u"MCast port*: ", None))
#if QT_CONFIG(tooltip)
        self.interfaceAddressLabel_10.setToolTip(QCoreApplication.translate("Widget", u"Enter ipconfig in terminal to see interfaces", None))
#endif // QT_CONFIG(tooltip)
        self.interfaceAddressLabel_10.setText(QCoreApplication.translate("Widget", u"Interface address:", None))
        self.udpConnectButton_10.setText(QCoreApplication.translate("Widget", u"Create UDP connection", None))
        self.openFileButton.setText(QCoreApplication.translate("Widget", u"Open previous data", None))
        self.recordingToggleButton.setText(QCoreApplication.translate("Widget", u"Recording", None))
        self.exporter.setText(QCoreApplication.translate("Widget", u"Export to File", None))
        self.xv5.setText(QCoreApplication.translate("Widget", u"XV-5", None))
        self.xv8State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.quickDisconnect.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Quick Disconnect</p></body></html>", None))
        self.xv6State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv3.setText(QCoreApplication.translate("Widget", u"XV-3", None))
        self.xv11.setText(QCoreApplication.translate("Widget", u"XV-11", None))
        self.xv7State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv1State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv1.setText(QCoreApplication.translate("Widget", u"XV-1", None))
        self.xv4State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv5State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.igniter.setText(QCoreApplication.translate("Widget", u"Igniter", None))
        self.xv11State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.igniterState.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv6.setText(QCoreApplication.translate("Widget", u"XV-6", None))
        self.xv12.setText(QCoreApplication.translate("Widget", u"XV-12", None))
        self.quickDisconnectState.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.cv1.setText(QCoreApplication.translate("Widget", u"Fire Valve", None))
        self.xv4.setText(QCoreApplication.translate("Widget", u"XV-4", None))
        self.xv10State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv9State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv3State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv10.setText(QCoreApplication.translate("Widget", u"XV-10", None))
        self.xv2State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.cv1State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv2.setText(QCoreApplication.translate("Widget", u"XV-2", None))
        self.xv7.setText(QCoreApplication.translate("Widget", u"XV-7", None))
        self.xv12State.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv9.setText(QCoreApplication.translate("Widget", u"XV-9", None))
        self.xv8.setText(QCoreApplication.translate("Widget", u"XV-8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.telemetryTab), QCoreApplication.translate("Widget", u"Telemetry", None))
        self.multicastConfigLabel.setText(QCoreApplication.translate("Widget", u"Multicast configuration", None))
#if QT_CONFIG(tooltip)
        self.udpIpAddressLabel.setToolTip(QCoreApplication.translate("Widget", u"Address of multicast group", None))
#endif // QT_CONFIG(tooltip)
        self.udpIpAddressLabel.setText(QCoreApplication.translate("Widget", u"MCast IPv4 address*: ", None))
#if QT_CONFIG(tooltip)
        self.udpPortLabel.setToolTip(QCoreApplication.translate("Widget", u"Port of multicast group", None))
#endif // QT_CONFIG(tooltip)
        self.udpPortLabel.setText(QCoreApplication.translate("Widget", u"MCast port*: ", None))
#if QT_CONFIG(tooltip)
        self.interfaceAddressLabel.setToolTip(QCoreApplication.translate("Widget", u"Enter ipconfig in terminal to see interfaces", None))
#endif // QT_CONFIG(tooltip)
        self.interfaceAddressLabel.setText(QCoreApplication.translate("Widget", u"Interface address:", None))
        self.udpConnectButton.setText(QCoreApplication.translate("Widget", u"Join multicast group", None))
        self.serialConfigLabel.setText(QCoreApplication.translate("Widget", u"Serial configuration", None))
#if QT_CONFIG(tooltip)
        self.serialPortLabel.setToolTip(QCoreApplication.translate("Widget", u"Enter ipconfig in terminal to see interfaces", None))
#endif // QT_CONFIG(tooltip)
        self.serialPortLabel.setText(QCoreApplication.translate("Widget", u"Serial port:", None))
        self.serialConnectButton.setText(QCoreApplication.translate("Widget", u"Connect to serial port", None))
        self.pressureThresholdLabel.setText(QCoreApplication.translate("Widget", u"Pressure", None))
        self.pressureThresholdButton.setText(QCoreApplication.translate("Widget", u"Add threshold marker", None))
        self.engineThrustThresholdLabel.setText(QCoreApplication.translate("Widget", u"Engine Thrust", None))
        self.engineThrustThresholdButton.setText(QCoreApplication.translate("Widget", u"Add threshold marker", None))
        self.temperatureThresholdLabel.setText(QCoreApplication.translate("Widget", u"Temperature", None))
        self.temperatureThresholdButton.setText(QCoreApplication.translate("Widget", u"Add threshold marker", None))
        self.tankMassThresholdLabel.setText(QCoreApplication.translate("Widget", u"Tank Mass", None))
        self.tankMassThresholdButton.setText(QCoreApplication.translate("Widget", u"Add threshold marker", None))
        self.graphThresholdLabel.setText(QCoreApplication.translate("Widget", u"Graph threshold lines", None))
        self.saveConfigButton.setText(QCoreApplication.translate("Widget", u"Save configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configurationTab), QCoreApplication.translate("Widget", u"Configuration", None))
        self.pid_image.setText("")
        self.cv1State_tabpid.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv1State_tabpid.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv2State_tabpid.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv3State_tabpid.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.xv4State_tabpid.setText(QCoreApplication.translate("Widget", u"CLOSED", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pAndIdTab), QCoreApplication.translate("Widget", u"P&&ID", None))
    # retranslateUi

