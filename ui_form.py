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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget
import rc_resources

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1288, 757)
        icon = QIcon()
        icon.addFile(u"logos/better_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 15, 20, 20)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
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
        self.logoLabel.setPixmap(QPixmap(u":/images/logo"))
        self.logoLabel.setScaledContents(True)

        self.controlLayout.addWidget(self.logoLabel)

        self.connectionLayout = QVBoxLayout()
        self.connectionLayout.setObjectName(u"connectionLayout")
        self.addressLayout = QHBoxLayout()
        self.addressLayout.setSpacing(1)
        self.addressLayout.setObjectName(u"addressLayout")
        self.udpIpAddressLabel = QLabel(self.telemetryTab)
        self.udpIpAddressLabel.setObjectName(u"udpIpAddressLabel")

        self.addressLayout.addWidget(self.udpIpAddressLabel)

        self.udpIpAddressInput = QLineEdit(self.telemetryTab)
        self.udpIpAddressInput.setObjectName(u"udpIpAddressInput")
        self.udpIpAddressInput.setStyleSheet(u"")

        self.addressLayout.addWidget(self.udpIpAddressInput)


        self.connectionLayout.addLayout(self.addressLayout)

        self.portLayout = QHBoxLayout()
        self.portLayout.setSpacing(6)
        self.portLayout.setObjectName(u"portLayout")
        self.portLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.udpPortLabel = QLabel(self.telemetryTab)
        self.udpPortLabel.setObjectName(u"udpPortLabel")
        self.udpPortLabel.setMinimumSize(QSize(85, 0))

        self.portLayout.addWidget(self.udpPortLabel)

        self.udpPortInput = QLineEdit(self.telemetryTab)
        self.udpPortInput.setObjectName(u"udpPortInput")
        self.udpPortInput.setStyleSheet(u"")

        self.portLayout.addWidget(self.udpPortInput)


        self.connectionLayout.addLayout(self.portLayout)

        self.udpConnectButton = QPushButton(self.telemetryTab)
        self.udpConnectButton.setObjectName(u"udpConnectButton")
        self.udpConnectButton.setMaximumSize(QSize(1000, 16777215))
        self.udpConnectButton.setStyleSheet(u"")

        self.connectionLayout.addWidget(self.udpConnectButton)


        self.controlLayout.addLayout(self.connectionLayout)

        self.logLayout = QVBoxLayout()
        self.logLayout.setObjectName(u"logLayout")
        self.logOutput = QTextBrowser(self.telemetryTab)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setMaximumSize(QSize(16777215, 110))
        self.logOutput.setStyleSheet(u"")

        self.logLayout.addWidget(self.logOutput)


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
        self.xv7State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv7State, 3, 1, 1, 1)

        self.xv1State = QLabel(self.telemetryTab)
        self.xv1State.setObjectName(u"xv1State")
        self.xv1State.setFont(font1)

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
        self.xv4State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv4State, 2, 1, 1, 1)

        self.xv5State = QLabel(self.telemetryTab)
        self.xv5State.setObjectName(u"xv5State")
        self.xv5State.setFont(font1)

        self.gridLayout_2.addWidget(self.xv5State, 2, 3, 1, 1)

        self.igniter = QLabel(self.telemetryTab)
        self.igniter.setObjectName(u"igniter")
        self.igniter.setFont(font)

        self.gridLayout_2.addWidget(self.igniter, 0, 4, 1, 1)

        self.xv11State = QLabel(self.telemetryTab)
        self.xv11State.setObjectName(u"xv11State")
        self.xv11State.setFont(font1)

        self.gridLayout_2.addWidget(self.xv11State, 4, 3, 1, 1)

        self.igniterState = QLabel(self.telemetryTab)
        self.igniterState.setObjectName(u"igniterState")
        self.igniterState.setFont(font1)

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
        self.quickDisconnectState.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.quickDisconnectState, 0, 1, 1, 1)

        self.cv1 = QLabel(self.telemetryTab)
        self.cv1.setObjectName(u"cv1")
        self.cv1.setMinimumSize(QSize(80, 0))
        self.cv1.setFont(font2)
        self.cv1.setIndent(10)

        self.gridLayout_2.addWidget(self.cv1, 0, 2, 1, 1)

        self.xv4 = QLabel(self.telemetryTab)
        self.xv4.setObjectName(u"xv4")
        self.xv4.setFont(font)

        self.gridLayout_2.addWidget(self.xv4, 2, 0, 1, 1)

        self.xv10State = QLabel(self.telemetryTab)
        self.xv10State.setObjectName(u"xv10State")
        self.xv10State.setFont(font1)

        self.gridLayout_2.addWidget(self.xv10State, 4, 1, 1, 1)

        self.xv9State = QLabel(self.telemetryTab)
        self.xv9State.setObjectName(u"xv9State")
        self.xv9State.setFont(font1)

        self.gridLayout_2.addWidget(self.xv9State, 3, 5, 1, 1)

        self.xv3State = QLabel(self.telemetryTab)
        self.xv3State.setObjectName(u"xv3State")
        self.xv3State.setFont(font1)

        self.gridLayout_2.addWidget(self.xv3State, 1, 5, 1, 1)

        self.xv10 = QLabel(self.telemetryTab)
        self.xv10.setObjectName(u"xv10")
        self.xv10.setFont(font)

        self.gridLayout_2.addWidget(self.xv10, 4, 0, 1, 1)

        self.xv2State = QLabel(self.telemetryTab)
        self.xv2State.setObjectName(u"xv2State")
        self.xv2State.setMinimumSize(QSize(50, 0))
        self.xv2State.setFont(font1)
        self.xv2State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv6State, 2, 5, 1, 1)

        self.xv3 = QLabel(Widget)
        self.xv3.setObjectName(u"xv3")
        self.xv3.setFont(font)

        self.gridLayout_2.addWidget(self.xv3, 1, 4, 1, 1)

        self.xv11 = QLabel(Widget)
        self.xv11.setObjectName(u"xv11")
        self.xv11.setFont(font)

        self.gridLayout_2.addWidget(self.xv11, 4, 2, 1, 1)

        self.xv7State = QLabel(Widget)
        self.xv7State.setObjectName(u"xv7State")
        self.xv7State.setMinimumSize(QSize(50, 0))
        self.xv7State.setFont(font1)
        self.xv7State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv7State, 3, 1, 1, 1)

        self.xv1State = QLabel(Widget)
        self.xv1State.setObjectName(u"xv1State")
        self.xv1State.setFont(font1)

        self.gridLayout_2.addWidget(self.xv1State, 1, 1, 1, 1)

        self.xv1 = QLabel(Widget)
        self.xv1.setObjectName(u"xv1")
        self.xv1.setMinimumSize(QSize(80, 23))
        self.xv1.setFont(font2)

        self.gridLayout_2.addWidget(self.xv1, 1, 0, 1, 1)

        self.cv1State = QLabel(self.telemetryTab)
        self.cv1State.setObjectName(u"cv1State")
        self.cv1State.setMinimumSize(QSize(50, 0))
        self.cv1State.setFont(font1)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pressurePlot.sizePolicy().hasHeightForWidth())
        self.pressurePlot.setSizePolicy(sizePolicy1)

        self.plotLayout.addWidget(self.pressurePlot, 0, 0, 1, 1)

        self.temperaturePlot = PlotWidget(self.telemetryTab)
        self.temperaturePlot.setObjectName(u"temperaturePlot")
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.temperaturePlot.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.temperaturePlot.setForegroundBrush(brush1)

        self.plotLayout.addWidget(self.temperaturePlot, 0, 1, 1, 1)

        self.engineThrustPlot = PlotWidget(self.telemetryTab)
        self.engineThrustPlot.setObjectName(u"engineThrustPlot")

        self.plotLayout.addWidget(self.engineThrustPlot, 1, 1, 1, 1)

        self.tankMassPlot = PlotWidget(self.telemetryTab)
        self.tankMassPlot.setObjectName(u"tankMassPlot")

        self.plotLayout.addWidget(self.engineThrustPlot, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.plotLayout)

        self.tabWidget.addTab(self.telemetryTab, "")
        self.pAndIdTab = QWidget()
        self.pAndIdTab.setObjectName(u"pAndIdTab")
        self.tabWidget.addTab(self.pAndIdTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.logoLabel.setText("")
        self.udpIpAddressLabel.setText(QCoreApplication.translate("Widget", u"MG IPv4 address: ", None))
        self.udpPortLabel.setText(QCoreApplication.translate("Widget", u"MG port: ", None))
        self.udpConnectButton.setText(QCoreApplication.translate("Widget", u"Create UDP connection", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pAndIdTab), QCoreApplication.translate("Widget", u"P&&ID", None))
    # retranslateUi

