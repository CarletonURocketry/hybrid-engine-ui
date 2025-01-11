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
        self.controlLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(6)
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

        self.openFileButton = QPushButton(self.telemetryTab)
        self.openFileButton.setObjectName(u"openFileButton")

        self.mainLayout.addWidget(self.openFileButton)

        self.recordingToggleButton = QRadioButton(self.telemetryTab)
        self.recordingToggleButton.setObjectName(u"recordingToggleButton")

        self.mainLayout.addWidget(self.recordingToggleButton)


        self.controlLayout.addLayout(self.mainLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.label_3 = QLabel(self.telemetryTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 0))
        font = QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_14 = QLabel(self.telemetryTab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(90, 0))
        self.label_14.setFont(font)

        self.gridLayout_3.addWidget(self.label_14, 4, 2, 1, 1)

        self.label_19 = QLabel(self.telemetryTab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(90, 0))
        self.label_19.setFont(font)

        self.gridLayout_3.addWidget(self.label_19, 3, 3, 1, 1)

        self.label_15 = QLabel(self.telemetryTab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(90, 0))
        self.label_15.setFont(font)

        self.gridLayout_3.addWidget(self.label_15, 3, 2, 1, 1)

        self.label_6 = QLabel(self.telemetryTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(90, 0))
        self.label_6.setFont(font)

        self.gridLayout_3.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_13 = QLabel(self.telemetryTab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(90, 0))
        self.label_13.setFont(font)

        self.gridLayout_3.addWidget(self.label_13, 4, 1, 1, 1)

        self.label = QLabel(self.telemetryTab)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_12 = QLabel(self.telemetryTab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(90, 0))
        self.label_12.setFont(font)

        self.gridLayout_3.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_7 = QLabel(self.telemetryTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(90, 0))
        self.label_7.setFont(font)

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_18 = QLabel(self.telemetryTab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(90, 0))
        self.label_18.setFont(font)

        self.gridLayout_3.addWidget(self.label_18, 2, 3, 1, 1)

        self.label_17 = QLabel(self.telemetryTab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(90, 0))
        self.label_17.setFont(font)

        self.gridLayout_3.addWidget(self.label_17, 1, 3, 1, 1)

        self.label_16 = QLabel(self.telemetryTab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(90, 0))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_16, 0, 3, 1, 1)

        self.label_5 = QLabel(self.telemetryTab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 0))
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_2 = QLabel(self.telemetryTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_8 = QLabel(self.telemetryTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(90, 0))
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_11 = QLabel(self.telemetryTab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(90, 0))
        self.label_11.setFont(font)

        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_4 = QLabel(self.telemetryTab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 0))
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_9 = QLabel(self.telemetryTab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(90, 0))
        self.label_9.setFont(font)

        self.gridLayout_3.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_10 = QLabel(self.telemetryTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(90, 0))
        self.label_10.setFont(font)

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_20 = QLabel(self.telemetryTab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(90, 0))
        self.label_20.setFont(font)

        self.gridLayout_3.addWidget(self.label_20, 4, 3, 1, 1)


        self.controlLayout.addLayout(self.gridLayout_3)

        self.valveStatusLayout = QFormLayout()
        self.valveStatusLayout.setObjectName(u"valveStatusLayout")
        self.valveGrid = QGridLayout()
        self.valveGrid.setObjectName(u"valveGrid")

        self.valveStatusLayout.setLayout(0, QFormLayout.LabelRole, self.valveGrid)


        self.controlLayout.addLayout(self.valveStatusLayout)


        self.verticalLayout.addLayout(self.controlLayout)

        self.plotLayout = QGridLayout()
        self.plotLayout.setSpacing(20)
        self.plotLayout.setObjectName(u"plotLayout")
        self.tankMassPlot = PlotWidget(self.telemetryTab)
        self.tankMassPlot.setObjectName(u"tankMassPlot")
        brush = QBrush(QColor(240, 240, 240, 255))
        brush.setStyle(Qt.SolidPattern)
        self.tankMassPlot.setBackgroundBrush(brush)

        self.plotLayout.addWidget(self.tankMassPlot, 1, 0, 1, 1)

        self.temperaturePlot = PlotWidget(self.telemetryTab)
        self.temperaturePlot.setObjectName(u"temperaturePlot")
        self.temperaturePlot.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.temperaturePlot.setForegroundBrush(brush1)

        self.plotLayout.addWidget(self.temperaturePlot, 0, 1, 1, 1)

        self.pressurePlot = PlotWidget(self.telemetryTab)
        self.pressurePlot.setObjectName(u"pressurePlot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pressurePlot.sizePolicy().hasHeightForWidth())
        self.pressurePlot.setSizePolicy(sizePolicy1)
        self.pressurePlot.setAutoFillBackground(False)
        self.pressurePlot.setBackgroundBrush(brush)

        self.plotLayout.addWidget(self.pressurePlot, 0, 0, 1, 1)

        self.engineThrustPlot = PlotWidget(self.telemetryTab)
        self.engineThrustPlot.setObjectName(u"engineThrustPlot")
        self.engineThrustPlot.setBackgroundBrush(brush)

        self.plotLayout.addWidget(self.engineThrustPlot, 1, 1, 1, 1)


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
        font1 = QFont()
        font1.setBold(True)
        self.multicastConfigLabel.setFont(font1)
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
        self.serialConfigLabel.setFont(font1)
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
        self.graphThresholdLabel.setFont(font1)
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
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.cv1State_tabpid.setFont(font2)
        self.cv1State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.cv1State_tabpid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.xv1State_tabpid = QLabel(self.pAndIdTab)
        self.xv1State_tabpid.setObjectName(u"xv1State_tabpid")
        self.xv1State_tabpid.setGeometry(QRect(280, 420, 74, 37))
        self.xv1State_tabpid.setFont(font2)
        self.xv1State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv1State_tabpid.setIndent(8)
        self.xv2State_tabpid = QLabel(self.pAndIdTab)
        self.xv2State_tabpid.setObjectName(u"xv2State_tabpid")
        self.xv2State_tabpid.setGeometry(QRect(400, 290, 74, 37))
        self.xv2State_tabpid.setMinimumSize(QSize(50, 0))
        self.xv2State_tabpid.setFont(font2)
        self.xv2State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv2State_tabpid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.xv3State_tabpid = QLabel(self.pAndIdTab)
        self.xv3State_tabpid.setObjectName(u"xv3State_tabpid")
        self.xv3State_tabpid.setGeometry(QRect(500, 510, 74, 37))
        self.xv3State_tabpid.setFont(font2)
        self.xv3State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv3State_tabpid.setIndent(8)
        self.xv4State_tabpid = QLabel(self.pAndIdTab)
        self.xv4State_tabpid.setObjectName(u"xv4State_tabpid")
        self.xv4State_tabpid.setGeometry(QRect(730, 130, 74, 36))
        self.xv4State_tabpid.setMinimumSize(QSize(50, 0))
        self.xv4State_tabpid.setFont(font2)
        self.xv4State_tabpid.setStyleSheet(u"background-color: rgb(255, 80, 80);")
        self.xv4State_tabpid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.pAndIdTab, "")
        self.logTab = QWidget()
        self.logTab.setObjectName(u"logTab")
        self.verticalLayout_5 = QVBoxLayout(self.logTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logOutput = QTextBrowser(self.logTab)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setMinimumSize(QSize(1250, 600))
        self.logOutput.setMaximumSize(QSize(1250, 600))
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
        self.openFileButton.setText(QCoreApplication.translate("Widget", u"Open previous data", None))
        self.recordingToggleButton.setText(QCoreApplication.translate("Widget", u"Recording", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
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
        self.exporter.setText(QCoreApplication.translate("Widget", u"Export to File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), QCoreApplication.translate("Widget", u"Log", None))
    # retranslateUi

