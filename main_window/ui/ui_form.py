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
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget
from . import rc_resources

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1320, 892)
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
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
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

        self.mainLayout.addWidget(self.logoLabel)

        self.showPIDButton = QPushButton(self.telemetryTab)
        self.showPIDButton.setObjectName(u"showPIDButton")

        self.mainLayout.addWidget(self.showPIDButton)

        self.openFileButton = QPushButton(self.telemetryTab)
        self.openFileButton.setObjectName(u"openFileButton")

        self.mainLayout.addWidget(self.openFileButton)

        self.recordingToggleButton = QRadioButton(self.telemetryTab)
        self.recordingToggleButton.setObjectName(u"recordingToggleButton")

        self.mainLayout.addWidget(self.recordingToggleButton)


        self.controlLayout.addLayout(self.mainLayout)

        self.sensorLayout = QGridLayout()
        self.sensorLayout.setObjectName(u"sensorLayout")

        self.controlLayout.addLayout(self.sensorLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.udpConnLabel = QLabel(self.telemetryTab)
        self.udpConnLabel.setObjectName(u"udpConnLabel")
        font = QFont()
        font.setPointSize(14)
        self.udpConnLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.udpConnLabel)

        self.udpConnStatusLabel = QLabel(self.telemetryTab)
        self.udpConnStatusLabel.setObjectName(u"udpConnStatusLabel")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setWeight(QFont.DemiBold)
        self.udpConnStatusLabel.setFont(font1)
        self.udpConnStatusLabel.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.udpConnStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.udpConnStatusLabel)

        self.serialConnLabel = QLabel(self.telemetryTab)
        self.serialConnLabel.setObjectName(u"serialConnLabel")
        self.serialConnLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.serialConnLabel)

        self.serialConnStatusLabel = QLabel(self.telemetryTab)
        self.serialConnStatusLabel.setObjectName(u"serialConnStatusLabel")
        self.serialConnStatusLabel.setFont(font1)
        self.serialConnStatusLabel.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.serialConnStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.serialConnStatusLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.valveGrid = QGridLayout()
        self.valveGrid.setObjectName(u"valveGrid")

        self.verticalLayout_3.addLayout(self.valveGrid)


        self.controlLayout.addLayout(self.verticalLayout_3)

        self.controlLayout.setStretch(0, 2)
        self.controlLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.controlLayout)

        self.plotLayout = QGridLayout()
        self.plotLayout.setSpacing(20)
        self.plotLayout.setObjectName(u"plotLayout")
        self.pressurePlot = PlotWidget(self.telemetryTab)
        self.pressurePlot.setObjectName(u"pressurePlot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pressurePlot.sizePolicy().hasHeightForWidth())
        self.pressurePlot.setSizePolicy(sizePolicy1)
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
        font2 = QFont()
        font2.setBold(True)
        self.multicastConfigLabel.setFont(font2)
        self.multicastConfigLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.connectionLayout.addWidget(self.multicastConfigLabel)

        self.addressLayout = QHBoxLayout()
        self.addressLayout.setObjectName(u"addressLayout")
        self.udpIpAddressLabel = QLabel(self.configurationTab)
        self.udpIpAddressLabel.setObjectName(u"udpIpAddressLabel")

        self.addressLayout.addWidget(self.udpIpAddressLabel)

        self.udpIpAddressInput = QLineEdit(self.configurationTab)
        self.udpIpAddressInput.setObjectName(u"udpIpAddressInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.udpIpAddressInput.sizePolicy().hasHeightForWidth())
        self.udpIpAddressInput.setSizePolicy(sizePolicy2)

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
        sizePolicy2.setHeightForWidth(self.udpPortInput.sizePolicy().hasHeightForWidth())
        self.udpPortInput.setSizePolicy(sizePolicy2)
        self.udpPortInput.setStyleSheet(u"")

        self.portLayout.addWidget(self.udpPortInput)


        self.connectionLayout.addLayout(self.portLayout)

        self.udpConnectButton = QPushButton(self.configurationTab)
        self.udpConnectButton.setObjectName(u"udpConnectButton")
        self.udpConnectButton.setStyleSheet(u"")

        self.connectionLayout.addWidget(self.udpConnectButton)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.connectionLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer)

        self.serialLayout = QVBoxLayout()
        self.serialLayout.setObjectName(u"serialLayout")
        self.serialConfigLabel = QLabel(self.configurationTab)
        self.serialConfigLabel.setObjectName(u"serialConfigLabel")
        self.serialConfigLabel.setFont(font2)
        self.serialConfigLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.serialLayout.addWidget(self.serialConfigLabel)

        self.serialPortSelectLayout = QHBoxLayout()
        self.serialPortSelectLayout.setObjectName(u"serialPortSelectLayout")
        self.serialPortLabel = QLabel(self.configurationTab)
        self.serialPortLabel.setObjectName(u"serialPortLabel")

        self.serialPortSelectLayout.addWidget(self.serialPortLabel)

        self.serialPortDropdown = QComboBox(self.configurationTab)
        self.serialPortDropdown.setObjectName(u"serialPortDropdown")

        self.serialPortSelectLayout.addWidget(self.serialPortDropdown)


        self.serialLayout.addLayout(self.serialPortSelectLayout)

        self.serialBaudRateLayout = QHBoxLayout()
        self.serialBaudRateLayout.setObjectName(u"serialBaudRateLayout")
        self.baudRateLabel = QLabel(self.configurationTab)
        self.baudRateLabel.setObjectName(u"baudRateLabel")

        self.serialBaudRateLayout.addWidget(self.baudRateLabel)

        self.baudRateDropdown = QComboBox(self.configurationTab)
        self.baudRateDropdown.setObjectName(u"baudRateDropdown")

        self.serialBaudRateLayout.addWidget(self.baudRateDropdown)


        self.serialLayout.addLayout(self.serialBaudRateLayout)

        self.serialConnectLayout = QHBoxLayout()
        self.serialConnectLayout.setObjectName(u"serialConnectLayout")
        self.serialConnectButton = QPushButton(self.configurationTab)
        self.serialConnectButton.setObjectName(u"serialConnectButton")
        self.serialConnectButton.setStyleSheet(u"")

        self.serialConnectLayout.addWidget(self.serialConnectButton)

        self.serialRefreshButton = QPushButton(self.configurationTab)
        self.serialRefreshButton.setObjectName(u"serialRefreshButton")

        self.serialConnectLayout.addWidget(self.serialRefreshButton)

        self.serialConnectLayout.setStretch(0, 100)

        self.serialLayout.addLayout(self.serialConnectLayout)


        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.serialLayout)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pressureThresholdList.sizePolicy().hasHeightForWidth())
        self.pressureThresholdList.setSizePolicy(sizePolicy3)
        self.pressureThresholdList.setMaximumSize(QSize(16777215, 75))

        self.pressureThresholdLayot.addWidget(self.pressureThresholdList)

        self.pressureThresholdInput = QLineEdit(self.configurationTab)
        self.pressureThresholdInput.setObjectName(u"pressureThresholdInput")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pressureThresholdInput.sizePolicy().hasHeightForWidth())
        self.pressureThresholdInput.setSizePolicy(sizePolicy4)

        self.pressureThresholdLayot.addWidget(self.pressureThresholdInput)

        self.pressureThresholdButton = QPushButton(self.configurationTab)
        self.pressureThresholdButton.setObjectName(u"pressureThresholdButton")
        sizePolicy4.setHeightForWidth(self.pressureThresholdButton.sizePolicy().hasHeightForWidth())
        self.pressureThresholdButton.setSizePolicy(sizePolicy4)

        self.pressureThresholdLayot.addWidget(self.pressureThresholdButton)


        self.gridLayout.addLayout(self.pressureThresholdLayot, 1, 0, 1, 1)

        self.engineThrustThreshold = QVBoxLayout()
        self.engineThrustThreshold.setObjectName(u"engineThrustThreshold")
        self.engineThrustThresholdLabel = QLabel(self.configurationTab)
        self.engineThrustThresholdLabel.setObjectName(u"engineThrustThresholdLabel")

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdLabel)

        self.engineThrustThresholdList = QListWidget(self.configurationTab)
        self.engineThrustThresholdList.setObjectName(u"engineThrustThresholdList")
        sizePolicy4.setHeightForWidth(self.engineThrustThresholdList.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdList.setSizePolicy(sizePolicy4)
        self.engineThrustThresholdList.setMaximumSize(QSize(16777215, 75))

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdList)

        self.engineThrustThresholdInput = QLineEdit(self.configurationTab)
        self.engineThrustThresholdInput.setObjectName(u"engineThrustThresholdInput")
        sizePolicy4.setHeightForWidth(self.engineThrustThresholdInput.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdInput.setSizePolicy(sizePolicy4)

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdInput)

        self.engineThrustThresholdButton = QPushButton(self.configurationTab)
        self.engineThrustThresholdButton.setObjectName(u"engineThrustThresholdButton")
        sizePolicy4.setHeightForWidth(self.engineThrustThresholdButton.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdButton.setSizePolicy(sizePolicy4)

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdButton)


        self.gridLayout.addLayout(self.engineThrustThreshold, 2, 1, 1, 1)

        self.temperatureThresholdLayout = QVBoxLayout()
        self.temperatureThresholdLayout.setObjectName(u"temperatureThresholdLayout")
        self.temperatureThresholdLabel = QLabel(self.configurationTab)
        self.temperatureThresholdLabel.setObjectName(u"temperatureThresholdLabel")

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdLabel)

        self.temperatureThresholdList = QListWidget(self.configurationTab)
        self.temperatureThresholdList.setObjectName(u"temperatureThresholdList")
        sizePolicy4.setHeightForWidth(self.temperatureThresholdList.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdList.setSizePolicy(sizePolicy4)
        self.temperatureThresholdList.setMaximumSize(QSize(16777215, 75))

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdList)

        self.temperatureThresholdInput = QLineEdit(self.configurationTab)
        self.temperatureThresholdInput.setObjectName(u"temperatureThresholdInput")
        sizePolicy4.setHeightForWidth(self.temperatureThresholdInput.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdInput.setSizePolicy(sizePolicy4)

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdInput)

        self.temperatureThresholdButton = QPushButton(self.configurationTab)
        self.temperatureThresholdButton.setObjectName(u"temperatureThresholdButton")
        sizePolicy4.setHeightForWidth(self.temperatureThresholdButton.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdButton.setSizePolicy(sizePolicy4)

        self.temperatureThresholdLayout.addWidget(self.temperatureThresholdButton)


        self.gridLayout.addLayout(self.temperatureThresholdLayout, 1, 1, 1, 1)

        self.tankMassThresholdLayout = QVBoxLayout()
        self.tankMassThresholdLayout.setObjectName(u"tankMassThresholdLayout")
        self.tankMassThresholdLabel = QLabel(self.configurationTab)
        self.tankMassThresholdLabel.setObjectName(u"tankMassThresholdLabel")

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdLabel)

        self.tankMassThresholdList = QListWidget(self.configurationTab)
        self.tankMassThresholdList.setObjectName(u"tankMassThresholdList")
        sizePolicy4.setHeightForWidth(self.tankMassThresholdList.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdList.setSizePolicy(sizePolicy4)
        self.tankMassThresholdList.setMaximumSize(QSize(16777215, 75))

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdList)

        self.tankMassThresholdInput = QLineEdit(self.configurationTab)
        self.tankMassThresholdInput.setObjectName(u"tankMassThresholdInput")
        sizePolicy4.setHeightForWidth(self.tankMassThresholdInput.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdInput.setSizePolicy(sizePolicy4)

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdInput)

        self.tankMassThresholdButton = QPushButton(self.configurationTab)
        self.tankMassThresholdButton.setObjectName(u"tankMassThresholdButton")
        sizePolicy4.setHeightForWidth(self.tankMassThresholdButton.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdButton.setSizePolicy(sizePolicy4)

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdButton)


        self.gridLayout.addLayout(self.tankMassThresholdLayout, 2, 0, 1, 1)

        self.graphThresholdLabel = QLabel(self.configurationTab)
        self.graphThresholdLabel.setObjectName(u"graphThresholdLabel")
        self.graphThresholdLabel.setFont(font2)
        self.graphThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.graphThresholdLabel, 0, 0, 1, 2)


        self.formLayout.setLayout(4, QFormLayout.SpanningRole, self.gridLayout)

        self.saveConfigButton = QPushButton(self.configurationTab)
        self.saveConfigButton.setObjectName(u"saveConfigButton")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.saveConfigButton)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.tabWidget.addTab(self.configurationTab, "")
        self.logTab = QWidget()
        self.logTab.setObjectName(u"logTab")
        self.verticalLayout_5 = QVBoxLayout(self.logTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logOutput = QTextBrowser(self.logTab)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.logOutput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exporter = QPushButton(self.logTab)
        self.exporter.setObjectName(u"exporter")
        self.exporter.setMinimumSize(QSize(300, 30))
        self.exporter.setMaximumSize(QSize(300, 30))

        self.horizontalLayout.addWidget(self.exporter)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.logTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.logoLabel.setText("")
        self.showPIDButton.setText(QCoreApplication.translate("Widget", u"Show PID ", None))
        self.openFileButton.setText(QCoreApplication.translate("Widget", u"Open previous data", None))
        self.recordingToggleButton.setText(QCoreApplication.translate("Widget", u"Recording", None))
        self.udpConnLabel.setText(QCoreApplication.translate("Widget", u"UDP connection status: ", None))
        self.udpConnStatusLabel.setText(QCoreApplication.translate("Widget", u"Not connected", None))
        self.serialConnLabel.setText(QCoreApplication.translate("Widget", u"Serial connection status:", None))
        self.serialConnStatusLabel.setText(QCoreApplication.translate("Widget", u"Not connected", None))
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
        self.udpConnectButton.setText(QCoreApplication.translate("Widget", u"Join multicast group", None))
        self.serialConfigLabel.setText(QCoreApplication.translate("Widget", u"Serial configuration", None))
#if QT_CONFIG(tooltip)
        self.serialPortLabel.setToolTip(QCoreApplication.translate("Widget", u"Enter ipconfig in terminal to see interfaces", None))
#endif // QT_CONFIG(tooltip)
        self.serialPortLabel.setText(QCoreApplication.translate("Widget", u"Serial port:", None))
        self.baudRateLabel.setText(QCoreApplication.translate("Widget", u"Baud rate:", None))
        self.serialConnectButton.setText(QCoreApplication.translate("Widget", u"Connect to serial port", None))
        self.serialRefreshButton.setText(QCoreApplication.translate("Widget", u"Refresh", None))
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
        self.exporter.setText(QCoreApplication.translate("Widget", u"Export to File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), QCoreApplication.translate("Widget", u"Log", None))
    # retranslateUi

