# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

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
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 15, 20, 20)
        self.controlLayout = QGridLayout()
        self.controlLayout.setObjectName(u"controlLayout")
        self.connectionLayout = QVBoxLayout()
        self.connectionLayout.setObjectName(u"connectionLayout")
        self.addressLayout = QHBoxLayout()
        self.addressLayout.setSpacing(1)
        self.addressLayout.setObjectName(u"addressLayout")
        self.udpIpAddressLabel = QLabel(Widget)
        self.udpIpAddressLabel.setObjectName(u"udpIpAddressLabel")

        self.addressLayout.addWidget(self.udpIpAddressLabel)

        self.udpIpAddressInput = QLineEdit(Widget)
        self.udpIpAddressInput.setObjectName(u"udpIpAddressInput")

        self.addressLayout.addWidget(self.udpIpAddressInput)


        self.connectionLayout.addLayout(self.addressLayout)

        self.portLayout = QHBoxLayout()
        self.portLayout.setSpacing(6)
        self.portLayout.setObjectName(u"portLayout")
        self.portLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.udpPortLabel = QLabel(Widget)
        self.udpPortLabel.setObjectName(u"udpPortLabel")
        self.udpPortLabel.setMinimumSize(QSize(89, 0))

        self.portLayout.addWidget(self.udpPortLabel)

        self.udpPortInput = QLineEdit(Widget)
        self.udpPortInput.setObjectName(u"udpPortInput")

        self.portLayout.addWidget(self.udpPortInput)


        self.connectionLayout.addLayout(self.portLayout)

        self.udpConnectButton = QPushButton(Widget)
        self.udpConnectButton.setObjectName(u"udpConnectButton")
        self.udpConnectButton.setMaximumSize(QSize(1000, 16777215))

        self.connectionLayout.addWidget(self.udpConnectButton)


        self.controlLayout.addLayout(self.connectionLayout, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.xv2 = QLabel(Widget)
        self.xv2.setObjectName(u"xv2")
        self.xv2.setMinimumSize(QSize(80, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.xv2.setFont(font)
        self.xv2.setIndent(10)

        self.gridLayout_2.addWidget(self.xv2, 1, 2, 1, 1)

        self.xv1 = QLabel(Widget)
        self.xv1.setObjectName(u"xv1")
        self.xv1.setMinimumSize(QSize(80, 23))
        self.xv1.setFont(font)

        self.gridLayout_2.addWidget(self.xv1, 1, 0, 1, 1)

        self.xv3State = QLabel(Widget)
        self.xv3State.setObjectName(u"xv3State")
        self.xv3State.setMinimumSize(QSize(50, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.xv3State.setFont(font1)
        self.xv3State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv3State, 2, 1, 1, 1)

        self.cv1State = QLabel(Widget)
        self.cv1State.setObjectName(u"cv1State")
        self.cv1State.setMinimumSize(QSize(50, 0))
        self.cv1State.setFont(font1)
        self.cv1State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.cv1State, 0, 3, 1, 1)

        self.cv1 = QLabel(Widget)
        self.cv1.setObjectName(u"cv1")
        self.cv1.setMinimumSize(QSize(80, 0))
        self.cv1.setFont(font)
        self.cv1.setIndent(10)

        self.gridLayout_2.addWidget(self.cv1, 0, 2, 1, 1)

        self.quickDisconect = QLabel(Widget)
        self.quickDisconect.setObjectName(u"quickDisconect")
        self.quickDisconect.setMinimumSize(QSize(80, 23))
        self.quickDisconect.setFont(font)

        self.gridLayout_2.addWidget(self.quickDisconect, 0, 0, 1, 1)

        self.xv2State = QLabel(Widget)
        self.xv2State.setObjectName(u"xv2State")
        self.xv2State.setMinimumSize(QSize(50, 0))
        self.xv2State.setFont(font1)
        self.xv2State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv2State, 1, 3, 1, 1)

        self.xv4State = QLabel(Widget)
        self.xv4State.setObjectName(u"xv4State")
        self.xv4State.setMinimumSize(QSize(50, 0))
        self.xv4State.setFont(font1)
        self.xv4State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv4State, 2, 3, 1, 1)

        self.xv3 = QLabel(Widget)
        self.xv3.setObjectName(u"xv3")
        self.xv3.setMinimumSize(QSize(80, 23))
        self.xv3.setFont(font)

        self.gridLayout_2.addWidget(self.xv3, 2, 0, 1, 1)

        self.quickDisconectState = QLabel(Widget)
        self.quickDisconectState.setObjectName(u"quickDisconectState")
        self.quickDisconectState.setMinimumSize(QSize(50, 0))
        self.quickDisconectState.setFont(font1)
        self.quickDisconectState.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.quickDisconectState, 0, 1, 1, 1)

        self.xv1State = QLabel(Widget)
        self.xv1State.setObjectName(u"xv1State")
        self.xv1State.setMinimumSize(QSize(50, 0))
        self.xv1State.setFont(font1)
        self.xv1State.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.xv1State, 1, 1, 1, 1)

        self.xv4 = QLabel(Widget)
        self.xv4.setObjectName(u"xv4")
        self.xv4.setMinimumSize(QSize(80, 0))
        self.xv4.setFont(font)
        self.xv4.setIndent(10)

        self.gridLayout_2.addWidget(self.xv4, 2, 2, 1, 1)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.gridLayout_2)


        self.horizontalLayout_3.addLayout(self.formLayout_2)


        self.controlLayout.addLayout(self.horizontalLayout_3, 0, 4, 1, 1)

        self.logOutput = QTextBrowser(Widget)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setMaximumSize(QSize(350, 87))

        self.controlLayout.addWidget(self.logOutput, 0, 3, 1, 1)

        self.simButton = QPushButton(Widget)
        self.simButton.setObjectName(u"simButton")

        self.controlLayout.addWidget(self.simButton, 0, 6, 1, 1)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(127, 90))
        self.label.setMaximumSize(QSize(127, 90))
        self.label.setPixmap(QPixmap(u":/images/logo"))
        self.label.setScaledContents(True)

        self.controlLayout.addWidget(self.label, 0, 0, 1, 1)

        self.controlLayout.setColumnStretch(0, 3)

        self.verticalLayout.addLayout(self.controlLayout)

        self.plotLayout = QGridLayout()
        self.plotLayout.setSpacing(20)
        self.plotLayout.setObjectName(u"plotLayout")
        self.tankMassPlot = PlotWidget(Widget)
        self.tankMassPlot.setObjectName(u"tankMassPlot")

        self.plotLayout.addWidget(self.tankMassPlot, 1, 0, 1, 1)

        self.temperaturePlot = PlotWidget(Widget)
        self.temperaturePlot.setObjectName(u"temperaturePlot")
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.temperaturePlot.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.temperaturePlot.setForegroundBrush(brush1)

        self.plotLayout.addWidget(self.temperaturePlot, 0, 1, 1, 1)

        self.pressurePlot = PlotWidget(Widget)
        self.pressurePlot.setObjectName(u"pressurePlot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pressurePlot.sizePolicy().hasHeightForWidth())
        self.pressurePlot.setSizePolicy(sizePolicy1)

        self.plotLayout.addWidget(self.pressurePlot, 0, 0, 1, 1)

        self.engineThrustPlot = PlotWidget(Widget)
        self.engineThrustPlot.setObjectName(u"engineThrustPlot")

        self.plotLayout.addWidget(self.engineThrustPlot, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.plotLayout)

        self.verticalLayout.setStretch(1, 14)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.udpIpAddressLabel.setText(QCoreApplication.translate("Widget", u"MG IPv4 address: ", None))
        self.udpPortLabel.setText(QCoreApplication.translate("Widget", u"MG port: ", None))
        self.udpConnectButton.setText(QCoreApplication.translate("Widget", u"Create UDP connection", None))
        self.xv2.setText(QCoreApplication.translate("Widget", u"XV-2", None))
        self.xv1.setText(QCoreApplication.translate("Widget", u"XV-1", None))
        self.xv3State.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.cv1State.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.cv1.setText(QCoreApplication.translate("Widget", u"Fire Valve", None))
        self.quickDisconect.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">Quick Disconect</span></p></body></html>", None))
        self.xv2State.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.xv4State.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.xv3.setText(QCoreApplication.translate("Widget", u"XV-3", None))
        self.quickDisconectState.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.xv1State.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.xv4.setText(QCoreApplication.translate("Widget", u"XV-4", None))
        self.simButton.setText(QCoreApplication.translate("Widget", u"Start/Stop sim", None))
        self.label.setText("")
    # retranslateUi

