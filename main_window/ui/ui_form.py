# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
from . import rc_resources

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1569, 925)
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
        self.logoLabel.setMinimumSize(QSize(150, 106))
        self.logoLabel.setMaximumSize(QSize(127, 90))
        self.logoLabel.setPixmap(QPixmap(u":/images/logos/logo_avionics_pro_transparent.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.logoLabel)

        self.showPIDButton = QPushButton(self.telemetryTab)
        self.showPIDButton.setObjectName(u"showPIDButton")

        self.mainLayout.addWidget(self.showPIDButton)

        self.saveCsvButton = QPushButton(self.telemetryTab)
        self.saveCsvButton.setObjectName(u"saveCsvButton")

        self.mainLayout.addWidget(self.saveCsvButton)

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

        self.statesLayout = QVBoxLayout()
        self.statesLayout.setObjectName(u"statesLayout")
        self.connectionAndStateLayout = QVBoxLayout()
        self.connectionAndStateLayout.setObjectName(u"connectionAndStateLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.udpConnLabelsLayout = QHBoxLayout()
        self.udpConnLabelsLayout.setObjectName(u"udpConnLabelsLayout")
        self.udpConnLabel = QLabel(self.telemetryTab)
        self.udpConnLabel.setObjectName(u"udpConnLabel")
        font = QFont()
        font.setPointSize(14)
        self.udpConnLabel.setFont(font)

        self.udpConnLabelsLayout.addWidget(self.udpConnLabel)

        self.udpConnStatusLabel = QLabel(self.telemetryTab)
        self.udpConnStatusLabel.setObjectName(u"udpConnStatusLabel")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setWeight(QFont.DemiBold)
        self.udpConnStatusLabel.setFont(font1)
        self.udpConnStatusLabel.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.udpConnStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.udpConnLabelsLayout.addWidget(self.udpConnStatusLabel)


        self.horizontalLayout_6.addLayout(self.udpConnLabelsLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ccConnLabel = QLabel(self.telemetryTab)
        self.ccConnLabel.setObjectName(u"ccConnLabel")
        self.ccConnLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.ccConnLabel)

        self.ccConnStatusLabel = QLabel(self.telemetryTab)
        self.ccConnStatusLabel.setObjectName(u"ccConnStatusLabel")
        self.ccConnStatusLabel.setFont(font1)
        self.ccConnStatusLabel.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.ccConnStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.ccConnStatusLabel)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.serialConnLabelsLayout = QHBoxLayout()
        self.serialConnLabelsLayout.setObjectName(u"serialConnLabelsLayout")
        self.serialConnLabel = QLabel(self.telemetryTab)
        self.serialConnLabel.setObjectName(u"serialConnLabel")
        self.serialConnLabel.setFont(font)

        self.serialConnLabelsLayout.addWidget(self.serialConnLabel)

        self.serialConnStatusLabel = QLabel(self.telemetryTab)
        self.serialConnStatusLabel.setObjectName(u"serialConnStatusLabel")
        self.serialConnStatusLabel.setFont(font1)
        self.serialConnStatusLabel.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.serialConnStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.serialConnLabelsLayout.addWidget(self.serialConnStatusLabel)


        self.horizontalLayout_6.addLayout(self.serialConnLabelsLayout)


        self.connectionAndStateLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.armingStateLabelsLayout = QHBoxLayout()
        self.armingStateLabelsLayout.setObjectName(u"armingStateLabelsLayout")
        self.armingStateLabel = QLabel(self.telemetryTab)
        self.armingStateLabel.setObjectName(u"armingStateLabel")
        self.armingStateLabel.setFont(font)

        self.armingStateLabelsLayout.addWidget(self.armingStateLabel)

        self.armingStateValueLabel = QLabel(self.telemetryTab)
        self.armingStateValueLabel.setObjectName(u"armingStateValueLabel")
        self.armingStateValueLabel.setFont(font1)
        self.armingStateValueLabel.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.armingStateValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.armingStateLabelsLayout.addWidget(self.armingStateValueLabel)


        self.horizontalLayout_5.addLayout(self.armingStateLabelsLayout)

        self.continuityLabelsLayout = QHBoxLayout()
        self.continuityLabelsLayout.setObjectName(u"continuityLabelsLayout")
        self.continuityLabel = QLabel(self.telemetryTab)
        self.continuityLabel.setObjectName(u"continuityLabel")
        self.continuityLabel.setFont(font)

        self.continuityLabelsLayout.addWidget(self.continuityLabel)

        self.continuityValueLabel = QLabel(self.telemetryTab)
        self.continuityValueLabel.setObjectName(u"continuityValueLabel")
        self.continuityValueLabel.setFont(font1)
        self.continuityValueLabel.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.continuityValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.continuityLabelsLayout.addWidget(self.continuityValueLabel)


        self.horizontalLayout_5.addLayout(self.continuityLabelsLayout)


        self.connectionAndStateLayout.addLayout(self.horizontalLayout_5)


        self.statesLayout.addLayout(self.connectionAndStateLayout)

        self.valveGrid = QGridLayout()
        self.valveGrid.setObjectName(u"valveGrid")

        self.statesLayout.addLayout(self.valveGrid)


        self.controlLayout.addLayout(self.statesLayout)

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
        self.connectionTab = QWidget()
        self.connectionTab.setObjectName(u"connectionTab")
        self.connectionTab.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.connectionTab.setAutoFillBackground(True)
        self.formLayout = QFormLayout(self.connectionTab)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(450, 0, 450, 10)
        self.connectionLayout = QVBoxLayout()
        self.connectionLayout.setSpacing(10)
        self.connectionLayout.setObjectName(u"connectionLayout")
        self.multicastConfigLabel = QLabel(self.connectionTab)
        self.multicastConfigLabel.setObjectName(u"multicastConfigLabel")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.multicastConfigLabel.setFont(font2)
        self.multicastConfigLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.connectionLayout.addWidget(self.multicastConfigLabel)

        self.addressLayout = QHBoxLayout()
        self.addressLayout.setObjectName(u"addressLayout")
        self.udpIpAddressLabel = QLabel(self.connectionTab)
        self.udpIpAddressLabel.setObjectName(u"udpIpAddressLabel")

        self.addressLayout.addWidget(self.udpIpAddressLabel)

        self.udpIpAddressInput = QLineEdit(self.connectionTab)
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
        self.udpPortLabel = QLabel(self.connectionTab)
        self.udpPortLabel.setObjectName(u"udpPortLabel")
        self.udpPortLabel.setMinimumSize(QSize(85, 0))

        self.portLayout.addWidget(self.udpPortLabel)

        self.udpPortInput = QLineEdit(self.connectionTab)
        self.udpPortInput.setObjectName(u"udpPortInput")
        sizePolicy2.setHeightForWidth(self.udpPortInput.sizePolicy().hasHeightForWidth())
        self.udpPortInput.setSizePolicy(sizePolicy2)
        self.udpPortInput.setStyleSheet(u"")

        self.portLayout.addWidget(self.udpPortInput)


        self.connectionLayout.addLayout(self.portLayout)

        self.udpConnectButton = QPushButton(self.connectionTab)
        self.udpConnectButton.setObjectName(u"udpConnectButton")
        self.udpConnectButton.setStyleSheet(u"")

        self.connectionLayout.addWidget(self.udpConnectButton)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.connectionLayout)

        self.serialLayout = QVBoxLayout()
        self.serialLayout.setSpacing(10)
        self.serialLayout.setObjectName(u"serialLayout")
        self.serialConfigLabel = QLabel(self.connectionTab)
        self.serialConfigLabel.setObjectName(u"serialConfigLabel")
        self.serialConfigLabel.setFont(font2)
        self.serialConfigLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.serialLayout.addWidget(self.serialConfigLabel)

        self.serialPortSelectLayout = QHBoxLayout()
        self.serialPortSelectLayout.setObjectName(u"serialPortSelectLayout")
        self.serialPortLabel = QLabel(self.connectionTab)
        self.serialPortLabel.setObjectName(u"serialPortLabel")

        self.serialPortSelectLayout.addWidget(self.serialPortLabel)

        self.serialPortDropdown = QComboBox(self.connectionTab)
        self.serialPortDropdown.setObjectName(u"serialPortDropdown")

        self.serialPortSelectLayout.addWidget(self.serialPortDropdown)


        self.serialLayout.addLayout(self.serialPortSelectLayout)

        self.serialBaudRateLayout = QHBoxLayout()
        self.serialBaudRateLayout.setObjectName(u"serialBaudRateLayout")
        self.baudRateLabel = QLabel(self.connectionTab)
        self.baudRateLabel.setObjectName(u"baudRateLabel")

        self.serialBaudRateLayout.addWidget(self.baudRateLabel)

        self.baudRateDropdown = QComboBox(self.connectionTab)
        self.baudRateDropdown.setObjectName(u"baudRateDropdown")

        self.serialBaudRateLayout.addWidget(self.baudRateDropdown)


        self.serialLayout.addLayout(self.serialBaudRateLayout)

        self.serialConnectLayout = QHBoxLayout()
        self.serialConnectLayout.setObjectName(u"serialConnectLayout")
        self.serialConnectButton = QPushButton(self.connectionTab)
        self.serialConnectButton.setObjectName(u"serialConnectButton")
        self.serialConnectButton.setStyleSheet(u"")

        self.serialConnectLayout.addWidget(self.serialConnectButton)

        self.serialRefreshButton = QPushButton(self.connectionTab)
        self.serialRefreshButton.setObjectName(u"serialRefreshButton")

        self.serialConnectLayout.addWidget(self.serialRefreshButton)

        self.serialConnectLayout.setStretch(0, 100)

        self.serialLayout.addLayout(self.serialConnectLayout)


        self.formLayout.setLayout(1, QFormLayout.SpanningRole, self.serialLayout)

        self.saveConnConfigButton = QPushButton(self.connectionTab)
        self.saveConnConfigButton.setObjectName(u"saveConnConfigButton")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.saveConnConfigButton)

        self.tabWidget.addTab(self.connectionTab, "")
        self.displayOptionsTab = QWidget()
        self.displayOptionsTab.setObjectName(u"displayOptionsTab")
        self.displayOptionsTab.setAutoFillBackground(True)
        self.formLayout_2 = QFormLayout(self.displayOptionsTab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setContentsMargins(400, -1, 400, -1)
        self.sensorDisplayOptionsLayout = QVBoxLayout()
        self.sensorDisplayOptionsLayout.setSpacing(10)
        self.sensorDisplayOptionsLayout.setObjectName(u"sensorDisplayOptionsLayout")
        self.sensorDisplayOptionsLabel = QLabel(self.displayOptionsTab)
        self.sensorDisplayOptionsLabel.setObjectName(u"sensorDisplayOptionsLabel")
        self.sensorDisplayOptionsLabel.setFont(font2)
        self.sensorDisplayOptionsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sensorDisplayOptionsLayout.addWidget(self.sensorDisplayOptionsLabel)

        self.numPointsAverageLayout = QHBoxLayout()
        self.numPointsAverageLayout.setObjectName(u"numPointsAverageLayout")
        self.numPointsAverageLabel = QLabel(self.displayOptionsTab)
        self.numPointsAverageLabel.setObjectName(u"numPointsAverageLabel")
        self.numPointsAverageLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.numPointsAverageLayout.addWidget(self.numPointsAverageLabel)

        self.numPointsAverageInput = QSpinBox(self.displayOptionsTab)
        self.numPointsAverageInput.setObjectName(u"numPointsAverageInput")
        self.numPointsAverageInput.setValue(20)

        self.numPointsAverageLayout.addWidget(self.numPointsAverageInput)


        self.sensorDisplayOptionsLayout.addLayout(self.numPointsAverageLayout)

        self.defaultOpenValvesLayout = QVBoxLayout()
        self.defaultOpenValvesLayout.setObjectName(u"defaultOpenValvesLayout")
        self.defaultOpenValveslabel = QLabel(self.displayOptionsTab)
        self.defaultOpenValveslabel.setObjectName(u"defaultOpenValveslabel")
        self.defaultOpenValveslabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.defaultOpenValvesLayout.addWidget(self.defaultOpenValveslabel)

        self.defaultOpenValvesList = QListWidget(self.displayOptionsTab)
        self.defaultOpenValvesList.setObjectName(u"defaultOpenValvesList")

        self.defaultOpenValvesLayout.addWidget(self.defaultOpenValvesList)

        self.defaultOpenValvesInput = QLineEdit(self.displayOptionsTab)
        self.defaultOpenValvesInput.setObjectName(u"defaultOpenValvesInput")

        self.defaultOpenValvesLayout.addWidget(self.defaultOpenValvesInput)

        self.defaultOpenValvesButton = QPushButton(self.displayOptionsTab)
        self.defaultOpenValvesButton.setObjectName(u"defaultOpenValvesButton")

        self.defaultOpenValvesLayout.addWidget(self.defaultOpenValvesButton)


        self.sensorDisplayOptionsLayout.addLayout(self.defaultOpenValvesLayout)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.sensorDisplayOptionsLayout)

        self.graphOptionsLayout = QVBoxLayout()
        self.graphOptionsLayout.setSpacing(15)
        self.graphOptionsLayout.setObjectName(u"graphOptionsLayout")
        self.graphOptionsLabel = QLabel(self.displayOptionsTab)
        self.graphOptionsLabel.setObjectName(u"graphOptionsLabel")
        self.graphOptionsLabel.setFont(font2)
        self.graphOptionsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.graphOptionsLayout.addWidget(self.graphOptionsLabel)

        self.graphOptionsLayout_2 = QGridLayout()
        self.graphOptionsLayout_2.setObjectName(u"graphOptionsLayout_2")
        self.tankMassThresholdLayout = QVBoxLayout()
        self.tankMassThresholdLayout.setSpacing(4)
        self.tankMassThresholdLayout.setObjectName(u"tankMassThresholdLayout")
        self.tankMassThresholdLabel = QLabel(self.displayOptionsTab)
        self.tankMassThresholdLabel.setObjectName(u"tankMassThresholdLabel")
        font3 = QFont()
        font3.setBold(True)
        self.tankMassThresholdLabel.setFont(font3)
        self.tankMassThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdLabel)

        self.tankMassDataDisplayLabel = QLabel(self.displayOptionsTab)
        self.tankMassDataDisplayLabel.setObjectName(u"tankMassDataDisplayLabel")
        font4 = QFont()
        font4.setUnderline(True)
        self.tankMassDataDisplayLabel.setFont(font4)

        self.tankMassThresholdLayout.addWidget(self.tankMassDataDisplayLabel)

        self.tankMassDataDisplayLayout = QHBoxLayout()
        self.tankMassDataDisplayLayout.setObjectName(u"tankMassDataDisplayLayout")
        self.tankMassLastXPointsRB = QRadioButton(self.displayOptionsTab)
        self.tankMassDisplayButtonGroup = QButtonGroup(Widget)
        self.tankMassDisplayButtonGroup.setObjectName(u"tankMassDisplayButtonGroup")
        self.tankMassDisplayButtonGroup.addButton(self.tankMassLastXPointsRB)
        self.tankMassLastXPointsRB.setObjectName(u"tankMassLastXPointsRB")
        font5 = QFont()
        font5.setPointSize(8)
        self.tankMassLastXPointsRB.setFont(font5)
        self.tankMassLastXPointsRB.setStyleSheet(u"margin: 1px 2px")

        self.tankMassDataDisplayLayout.addWidget(self.tankMassLastXPointsRB)

        self.tankMassLastXSecsRB = QRadioButton(self.displayOptionsTab)
        self.tankMassDisplayButtonGroup.addButton(self.tankMassLastXSecsRB)
        self.tankMassLastXSecsRB.setObjectName(u"tankMassLastXSecsRB")
        self.tankMassLastXSecsRB.setFont(font5)
        self.tankMassLastXSecsRB.setStyleSheet(u"margin: 1px 2px")

        self.tankMassDataDisplayLayout.addWidget(self.tankMassLastXSecsRB)

        self.tankMassXLabel = QLabel(self.displayOptionsTab)
        self.tankMassXLabel.setObjectName(u"tankMassXLabel")
        self.tankMassXLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tankMassDataDisplayLayout.addWidget(self.tankMassXLabel)

        self.tankMassXSB = QSpinBox(self.displayOptionsTab)
        self.tankMassXSB.setObjectName(u"tankMassXSB")
        self.tankMassXSB.setMinimum(1)
        self.tankMassXSB.setMaximum(200)

        self.tankMassDataDisplayLayout.addWidget(self.tankMassXSB)


        self.tankMassThresholdLayout.addLayout(self.tankMassDataDisplayLayout)

        self.tankMassThresholdList = QListWidget(self.displayOptionsTab)
        self.tankMassThresholdList.setObjectName(u"tankMassThresholdList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tankMassThresholdList.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdList.setSizePolicy(sizePolicy3)
        self.tankMassThresholdList.setMaximumSize(QSize(16777215, 75))

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdList)

        self.tankMassThresholdInput = QLineEdit(self.displayOptionsTab)
        self.tankMassThresholdInput.setObjectName(u"tankMassThresholdInput")
        sizePolicy3.setHeightForWidth(self.tankMassThresholdInput.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdInput.setSizePolicy(sizePolicy3)

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdInput)

        self.tankMassThresholdButton = QPushButton(self.displayOptionsTab)
        self.tankMassThresholdButton.setObjectName(u"tankMassThresholdButton")
        sizePolicy3.setHeightForWidth(self.tankMassThresholdButton.sizePolicy().hasHeightForWidth())
        self.tankMassThresholdButton.setSizePolicy(sizePolicy3)

        self.tankMassThresholdLayout.addWidget(self.tankMassThresholdButton)


        self.graphOptionsLayout_2.addLayout(self.tankMassThresholdLayout, 1, 0, 1, 1)

        self.engineThrustThreshold = QVBoxLayout()
        self.engineThrustThreshold.setSpacing(4)
        self.engineThrustThreshold.setObjectName(u"engineThrustThreshold")
        self.engineThrustThresholdLabel = QLabel(self.displayOptionsTab)
        self.engineThrustThresholdLabel.setObjectName(u"engineThrustThresholdLabel")
        self.engineThrustThresholdLabel.setFont(font3)
        self.engineThrustThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdLabel)

        self.engineThrustDataDisplayLabel = QLabel(self.displayOptionsTab)
        self.engineThrustDataDisplayLabel.setObjectName(u"engineThrustDataDisplayLabel")
        self.engineThrustDataDisplayLabel.setFont(font4)

        self.engineThrustThreshold.addWidget(self.engineThrustDataDisplayLabel)

        self.engineThrustDataDisplayLayout = QHBoxLayout()
        self.engineThrustDataDisplayLayout.setObjectName(u"engineThrustDataDisplayLayout")
        self.engineThrustLastXPointsRB = QRadioButton(self.displayOptionsTab)
        self.engineThrustDisplayButtonGroup = QButtonGroup(Widget)
        self.engineThrustDisplayButtonGroup.setObjectName(u"engineThrustDisplayButtonGroup")
        self.engineThrustDisplayButtonGroup.addButton(self.engineThrustLastXPointsRB)
        self.engineThrustLastXPointsRB.setObjectName(u"engineThrustLastXPointsRB")
        self.engineThrustLastXPointsRB.setFont(font5)
        self.engineThrustLastXPointsRB.setStyleSheet(u"margin: 1px 2px")

        self.engineThrustDataDisplayLayout.addWidget(self.engineThrustLastXPointsRB)

        self.engineThrustLastXSecsRB = QRadioButton(self.displayOptionsTab)
        self.engineThrustDisplayButtonGroup.addButton(self.engineThrustLastXSecsRB)
        self.engineThrustLastXSecsRB.setObjectName(u"engineThrustLastXSecsRB")
        self.engineThrustLastXSecsRB.setFont(font5)
        self.engineThrustLastXSecsRB.setStyleSheet(u"margin: 1px 2px")

        self.engineThrustDataDisplayLayout.addWidget(self.engineThrustLastXSecsRB)

        self.engineThrustXLabel = QLabel(self.displayOptionsTab)
        self.engineThrustXLabel.setObjectName(u"engineThrustXLabel")
        self.engineThrustXLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.engineThrustDataDisplayLayout.addWidget(self.engineThrustXLabel)

        self.engineThrustXSB = QSpinBox(self.displayOptionsTab)
        self.engineThrustXSB.setObjectName(u"engineThrustXSB")
        self.engineThrustXSB.setMinimum(1)
        self.engineThrustXSB.setMaximum(200)

        self.engineThrustDataDisplayLayout.addWidget(self.engineThrustXSB)


        self.engineThrustThreshold.addLayout(self.engineThrustDataDisplayLayout)

        self.engineThrustThresholdList = QListWidget(self.displayOptionsTab)
        self.engineThrustThresholdList.setObjectName(u"engineThrustThresholdList")
        sizePolicy3.setHeightForWidth(self.engineThrustThresholdList.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdList.setSizePolicy(sizePolicy3)
        self.engineThrustThresholdList.setMaximumSize(QSize(16777215, 75))

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdList)

        self.engineThrustThresholdInput = QLineEdit(self.displayOptionsTab)
        self.engineThrustThresholdInput.setObjectName(u"engineThrustThresholdInput")
        sizePolicy3.setHeightForWidth(self.engineThrustThresholdInput.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdInput.setSizePolicy(sizePolicy3)

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdInput)

        self.engineThrustThresholdButton = QPushButton(self.displayOptionsTab)
        self.engineThrustThresholdButton.setObjectName(u"engineThrustThresholdButton")
        sizePolicy3.setHeightForWidth(self.engineThrustThresholdButton.sizePolicy().hasHeightForWidth())
        self.engineThrustThresholdButton.setSizePolicy(sizePolicy3)

        self.engineThrustThreshold.addWidget(self.engineThrustThresholdButton)


        self.graphOptionsLayout_2.addLayout(self.engineThrustThreshold, 1, 1, 1, 1)

        self.temperatureGraphOptionsLayout = QVBoxLayout()
        self.temperatureGraphOptionsLayout.setSpacing(4)
        self.temperatureGraphOptionsLayout.setObjectName(u"temperatureGraphOptionsLayout")
        self.temperatureThresholdLabel = QLabel(self.displayOptionsTab)
        self.temperatureThresholdLabel.setObjectName(u"temperatureThresholdLabel")
        self.temperatureThresholdLabel.setFont(font3)
        self.temperatureThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.temperatureGraphOptionsLayout.addWidget(self.temperatureThresholdLabel)

        self.temperatureDataDisplayLabel = QLabel(self.displayOptionsTab)
        self.temperatureDataDisplayLabel.setObjectName(u"temperatureDataDisplayLabel")
        self.temperatureDataDisplayLabel.setFont(font4)

        self.temperatureGraphOptionsLayout.addWidget(self.temperatureDataDisplayLabel)

        self.temperatureDataDisplayLayout = QHBoxLayout()
        self.temperatureDataDisplayLayout.setObjectName(u"temperatureDataDisplayLayout")
        self.temperatureDataDisplayLayout.setContentsMargins(-1, -1, -1, 3)
        self.temperatureLastXPointsRB = QRadioButton(self.displayOptionsTab)
        self.temperatureDisplayButtonGroup = QButtonGroup(Widget)
        self.temperatureDisplayButtonGroup.setObjectName(u"temperatureDisplayButtonGroup")
        self.temperatureDisplayButtonGroup.addButton(self.temperatureLastXPointsRB)
        self.temperatureLastXPointsRB.setObjectName(u"temperatureLastXPointsRB")
        self.temperatureLastXPointsRB.setFont(font5)
        self.temperatureLastXPointsRB.setStyleSheet(u"margin: 1px 2px")

        self.temperatureDataDisplayLayout.addWidget(self.temperatureLastXPointsRB)

        self.temperatureLastXSecsRB = QRadioButton(self.displayOptionsTab)
        self.temperatureDisplayButtonGroup.addButton(self.temperatureLastXSecsRB)
        self.temperatureLastXSecsRB.setObjectName(u"temperatureLastXSecsRB")
        self.temperatureLastXSecsRB.setFont(font5)
        self.temperatureLastXSecsRB.setStyleSheet(u"margin: 1px 2px")

        self.temperatureDataDisplayLayout.addWidget(self.temperatureLastXSecsRB)

        self.temperatureXLabel = QLabel(self.displayOptionsTab)
        self.temperatureXLabel.setObjectName(u"temperatureXLabel")
        self.temperatureXLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.temperatureDataDisplayLayout.addWidget(self.temperatureXLabel)

        self.temperatureXSB = QSpinBox(self.displayOptionsTab)
        self.temperatureXSB.setObjectName(u"temperatureXSB")
        self.temperatureXSB.setMinimum(1)
        self.temperatureXSB.setMaximum(200)

        self.temperatureDataDisplayLayout.addWidget(self.temperatureXSB)


        self.temperatureGraphOptionsLayout.addLayout(self.temperatureDataDisplayLayout)

        self.temperatureThresholdList = QListWidget(self.displayOptionsTab)
        self.temperatureThresholdList.setObjectName(u"temperatureThresholdList")
        sizePolicy3.setHeightForWidth(self.temperatureThresholdList.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdList.setSizePolicy(sizePolicy3)
        self.temperatureThresholdList.setMaximumSize(QSize(16777215, 75))

        self.temperatureGraphOptionsLayout.addWidget(self.temperatureThresholdList)

        self.temperatureThresholdInput = QLineEdit(self.displayOptionsTab)
        self.temperatureThresholdInput.setObjectName(u"temperatureThresholdInput")
        sizePolicy3.setHeightForWidth(self.temperatureThresholdInput.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdInput.setSizePolicy(sizePolicy3)

        self.temperatureGraphOptionsLayout.addWidget(self.temperatureThresholdInput)

        self.temperatureThresholdButton = QPushButton(self.displayOptionsTab)
        self.temperatureThresholdButton.setObjectName(u"temperatureThresholdButton")
        sizePolicy3.setHeightForWidth(self.temperatureThresholdButton.sizePolicy().hasHeightForWidth())
        self.temperatureThresholdButton.setSizePolicy(sizePolicy3)

        self.temperatureGraphOptionsLayout.addWidget(self.temperatureThresholdButton)


        self.graphOptionsLayout_2.addLayout(self.temperatureGraphOptionsLayout, 0, 1, 1, 1)

        self.pressureGraphOptionsLayout = QVBoxLayout()
        self.pressureGraphOptionsLayout.setSpacing(4)
        self.pressureGraphOptionsLayout.setObjectName(u"pressureGraphOptionsLayout")
        self.pressureThresholdLabel = QLabel(self.displayOptionsTab)
        self.pressureThresholdLabel.setObjectName(u"pressureThresholdLabel")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.pressureThresholdLabel.setFont(font6)
        self.pressureThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pressureGraphOptionsLayout.addWidget(self.pressureThresholdLabel)

        self.pressureDataDisplayLabel = QLabel(self.displayOptionsTab)
        self.pressureDataDisplayLabel.setObjectName(u"pressureDataDisplayLabel")
        font7 = QFont()
        font7.setItalic(False)
        font7.setUnderline(True)
        self.pressureDataDisplayLabel.setFont(font7)

        self.pressureGraphOptionsLayout.addWidget(self.pressureDataDisplayLabel)

        self.pressureDataDisplayLayout = QHBoxLayout()
        self.pressureDataDisplayLayout.setObjectName(u"pressureDataDisplayLayout")
        self.pressureDataDisplayLayout.setContentsMargins(-1, -1, -1, 3)
        self.pressureLastXPointsRB = QRadioButton(self.displayOptionsTab)
        self.pressureDisplayButtonGroup = QButtonGroup(Widget)
        self.pressureDisplayButtonGroup.setObjectName(u"pressureDisplayButtonGroup")
        self.pressureDisplayButtonGroup.addButton(self.pressureLastXPointsRB)
        self.pressureLastXPointsRB.setObjectName(u"pressureLastXPointsRB")
        self.pressureLastXPointsRB.setFont(font5)
        self.pressureLastXPointsRB.setStyleSheet(u"margin: 1px 2px")

        self.pressureDataDisplayLayout.addWidget(self.pressureLastXPointsRB)

        self.pressureLastXSecsRB = QRadioButton(self.displayOptionsTab)
        self.pressureDisplayButtonGroup.addButton(self.pressureLastXSecsRB)
        self.pressureLastXSecsRB.setObjectName(u"pressureLastXSecsRB")
        self.pressureLastXSecsRB.setFont(font5)
        self.pressureLastXSecsRB.setStyleSheet(u"margin: 1px 2px")

        self.pressureDataDisplayLayout.addWidget(self.pressureLastXSecsRB)

        self.pressureXLabel = QLabel(self.displayOptionsTab)
        self.pressureXLabel.setObjectName(u"pressureXLabel")
        self.pressureXLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.pressureDataDisplayLayout.addWidget(self.pressureXLabel)

        self.pressureXSB = QSpinBox(self.displayOptionsTab)
        self.pressureXSB.setObjectName(u"pressureXSB")
        self.pressureXSB.setMinimum(1)
        self.pressureXSB.setMaximum(200)

        self.pressureDataDisplayLayout.addWidget(self.pressureXSB)


        self.pressureGraphOptionsLayout.addLayout(self.pressureDataDisplayLayout)

        self.pressureThresholdList = QListWidget(self.displayOptionsTab)
        self.pressureThresholdList.setObjectName(u"pressureThresholdList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pressureThresholdList.sizePolicy().hasHeightForWidth())
        self.pressureThresholdList.setSizePolicy(sizePolicy4)
        self.pressureThresholdList.setMaximumSize(QSize(16777215, 75))

        self.pressureGraphOptionsLayout.addWidget(self.pressureThresholdList)

        self.pressureThresholdInput = QLineEdit(self.displayOptionsTab)
        self.pressureThresholdInput.setObjectName(u"pressureThresholdInput")
        sizePolicy3.setHeightForWidth(self.pressureThresholdInput.sizePolicy().hasHeightForWidth())
        self.pressureThresholdInput.setSizePolicy(sizePolicy3)

        self.pressureGraphOptionsLayout.addWidget(self.pressureThresholdInput)

        self.pressureThresholdButton = QPushButton(self.displayOptionsTab)
        self.pressureThresholdButton.setObjectName(u"pressureThresholdButton")
        sizePolicy3.setHeightForWidth(self.pressureThresholdButton.sizePolicy().hasHeightForWidth())
        self.pressureThresholdButton.setSizePolicy(sizePolicy3)

        self.pressureGraphOptionsLayout.addWidget(self.pressureThresholdButton)


        self.graphOptionsLayout_2.addLayout(self.pressureGraphOptionsLayout, 0, 0, 1, 1)


        self.graphOptionsLayout.addLayout(self.graphOptionsLayout_2)


        self.formLayout_2.setLayout(1, QFormLayout.SpanningRole, self.graphOptionsLayout)

        self.saveDisplayConfigButton = QPushButton(self.displayOptionsTab)
        self.saveDisplayConfigButton.setObjectName(u"saveDisplayConfigButton")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.saveDisplayConfigButton)

        self.tabWidget.addTab(self.displayOptionsTab, "")
        self.logTab = QWidget()
        self.logTab.setObjectName(u"logTab")
        self.logTab.setAutoFillBackground(True)
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
#if QT_CONFIG(tooltip)
        Widget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.logoLabel.setText("")
        self.showPIDButton.setText(QCoreApplication.translate("Widget", u"Open PID window", None))
        self.saveCsvButton.setText(QCoreApplication.translate("Widget", u"Save current CSV data", None))
        self.openFileButton.setText(QCoreApplication.translate("Widget", u"Open raw data file", None))
        self.recordingToggleButton.setText(QCoreApplication.translate("Widget", u"Recording raw data", None))
        self.udpConnLabel.setText(QCoreApplication.translate("Widget", u"Pad server:", None))
        self.udpConnStatusLabel.setText(QCoreApplication.translate("Widget", u"Not connected", None))
        self.ccConnLabel.setText(QCoreApplication.translate("Widget", u"Control client:", None))
        self.ccConnStatusLabel.setText(QCoreApplication.translate("Widget", u"Not connected", None))
#if QT_CONFIG(tooltip)
        self.serialConnLabel.setToolTip(QCoreApplication.translate("Widget", u"Deprecated", None))
#endif // QT_CONFIG(tooltip)
        self.serialConnLabel.setText(QCoreApplication.translate("Widget", u"Serial:", None))
        self.serialConnStatusLabel.setText(QCoreApplication.translate("Widget", u"Not connected", None))
        self.armingStateLabel.setText(QCoreApplication.translate("Widget", u"Arming state:", None))
        self.armingStateValueLabel.setText(QCoreApplication.translate("Widget", u"N/A", None))
        self.continuityLabel.setText(QCoreApplication.translate("Widget", u"Continuity State:", None))
        self.continuityValueLabel.setText(QCoreApplication.translate("Widget", u"N/A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.telemetryTab), QCoreApplication.translate("Widget", u"Telemetry", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.telemetryTab), QCoreApplication.translate("Widget", u"Main telemetry view", None))
#endif // QT_CONFIG(tooltip)
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
        self.serialPortLabel.setToolTip(QCoreApplication.translate("Widget", u"Serial device identifier", None))
#endif // QT_CONFIG(tooltip)
        self.serialPortLabel.setText(QCoreApplication.translate("Widget", u"Serial port:", None))
#if QT_CONFIG(tooltip)
        self.baudRateLabel.setToolTip(QCoreApplication.translate("Widget", u"Baud rate of serial device", None))
#endif // QT_CONFIG(tooltip)
        self.baudRateLabel.setText(QCoreApplication.translate("Widget", u"Baud rate:", None))
        self.serialConnectButton.setText(QCoreApplication.translate("Widget", u"Connect to serial port", None))
        self.serialRefreshButton.setText(QCoreApplication.translate("Widget", u"Refresh", None))
        self.saveConnConfigButton.setText(QCoreApplication.translate("Widget", u"Save default connection configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.connectionTab), QCoreApplication.translate("Widget", u"Connection", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.connectionTab), QCoreApplication.translate("Widget", u"Setup multicat or serial connection", None))
#endif // QT_CONFIG(tooltip)
        self.sensorDisplayOptionsLabel.setText(QCoreApplication.translate("Widget", u"Sensors & valves display options", None))
#if QT_CONFIG(tooltip)
        self.numPointsAverageLabel.setToolTip(QCoreApplication.translate("Widget", u"Number of most recent measurements to use when calculating an average", None))
#endif // QT_CONFIG(tooltip)
        self.numPointsAverageLabel.setText(QCoreApplication.translate("Widget", u"# points used for average", None))
        self.defaultOpenValveslabel.setText(QCoreApplication.translate("Widget", u"Valves open by default", None))
        self.defaultOpenValvesButton.setText(QCoreApplication.translate("Widget", u"Add/remove valve", None))
        self.graphOptionsLabel.setText(QCoreApplication.translate("Widget", u"Graph options", None))
        self.tankMassThresholdLabel.setText(QCoreApplication.translate("Widget", u"Tank Mass", None))
        self.tankMassDataDisplayLabel.setText(QCoreApplication.translate("Widget", u"Data display mode:", None))
        self.tankMassLastXPointsRB.setText(QCoreApplication.translate("Widget", u"Last X points", None))
        self.tankMassLastXPointsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"POINTS", None))
        self.tankMassLastXSecsRB.setText(QCoreApplication.translate("Widget", u"Points in last X seconds", None))
        self.tankMassLastXSecsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"SECONDS", None))
        self.tankMassXLabel.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.tankMassThresholdButton.setText(QCoreApplication.translate("Widget", u"Add/remove threshold marker", None))
        self.engineThrustThresholdLabel.setText(QCoreApplication.translate("Widget", u"Engine Thrust", None))
        self.engineThrustDataDisplayLabel.setText(QCoreApplication.translate("Widget", u"Data display mode:", None))
        self.engineThrustLastXPointsRB.setText(QCoreApplication.translate("Widget", u"Last X points", None))
        self.engineThrustLastXPointsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"POINTS", None))
        self.engineThrustLastXSecsRB.setText(QCoreApplication.translate("Widget", u"Points in last X seconds", None))
        self.engineThrustLastXSecsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"SECONDS", None))
        self.engineThrustXLabel.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.engineThrustThresholdButton.setText(QCoreApplication.translate("Widget", u"Add/remove threshold marker", None))
        self.temperatureThresholdLabel.setText(QCoreApplication.translate("Widget", u"Temperature", None))
        self.temperatureDataDisplayLabel.setText(QCoreApplication.translate("Widget", u"Data display mode:", None))
        self.temperatureLastXPointsRB.setText(QCoreApplication.translate("Widget", u"Last X packets", None))
        self.temperatureLastXPointsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"POINTS", None))
        self.temperatureLastXSecsRB.setText(QCoreApplication.translate("Widget", u"Packets in last X seconds", None))
        self.temperatureLastXSecsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"SECONDS", None))
        self.temperatureXLabel.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.temperatureThresholdButton.setText(QCoreApplication.translate("Widget", u"Add/remove threshold marker", None))
        self.pressureThresholdLabel.setText(QCoreApplication.translate("Widget", u"Pressure", None))
        self.pressureDataDisplayLabel.setText(QCoreApplication.translate("Widget", u"Data display mode:", None))
        self.pressureLastXPointsRB.setText(QCoreApplication.translate("Widget", u"Last X points", None))
        self.pressureLastXPointsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"POINTS", None))
        self.pressureLastXSecsRB.setText(QCoreApplication.translate("Widget", u"Points in last X seconds", None))
        self.pressureLastXSecsRB.setProperty(u"type", QCoreApplication.translate("Widget", u"SECONDS", None))
        self.pressureXLabel.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.pressureXSB.setSuffix("")
        self.pressureThresholdButton.setText(QCoreApplication.translate("Widget", u"Add/remove threshold marker", None))
        self.saveDisplayConfigButton.setText(QCoreApplication.translate("Widget", u"Save default display configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.displayOptionsTab), QCoreApplication.translate("Widget", u"Display Configuration", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.displayOptionsTab), QCoreApplication.translate("Widget", u"Configure display and system options", None))
#endif // QT_CONFIG(tooltip)
        self.exporter.setText(QCoreApplication.translate("Widget", u"Export to File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), QCoreApplication.translate("Widget", u"Log", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.logTab), QCoreApplication.translate("Widget", u"Logs", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

