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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

from pyqtgraph import PlotWidget
import rc_resources

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1291, 787)
        icon = QIcon()
        icon.addFile(u"logos/better_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.temperaturePlot = PlotWidget(Widget)
        self.temperaturePlot.setObjectName(u"temperaturePlot")
        self.temperaturePlot.setGeometry(QRect(660, 130, 611, 311))
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.temperaturePlot.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.temperaturePlot.setForegroundBrush(brush1)
        self.pressurePlot = PlotWidget(Widget)
        self.pressurePlot.setObjectName(u"pressurePlot")
        self.pressurePlot.setGeometry(QRect(20, 130, 611, 311))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressurePlot.sizePolicy().hasHeightForWidth())
        self.pressurePlot.setSizePolicy(sizePolicy)
        self.tankMassPlot = PlotWidget(Widget)
        self.tankMassPlot.setObjectName(u"tankMassPlot")
        self.tankMassPlot.setGeometry(QRect(20, 460, 611, 311))
        self.logoLabel = QLabel(Widget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(0, 0, 191, 111))
        self.logoLabel.setPixmap(QPixmap(u":/images/logo"))
        self.logoLabel.setScaledContents(True)
        self.simButton = QPushButton(Widget)
        self.simButton.setObjectName(u"simButton")
        self.simButton.setGeometry(QRect(1150, 20, 121, 24))
        self.engineThrustPlot = PlotWidget(Widget)
        self.engineThrustPlot.setObjectName(u"engineThrustPlot")
        self.engineThrustPlot.setGeometry(QRect(660, 460, 611, 311))
        self.tcpIpAddressInput = QLineEdit(Widget)
        self.tcpIpAddressInput.setObjectName(u"tcpIpAddressInput")
        self.tcpIpAddressInput.setGeometry(QRect(306, 50, 131, 24))
        self.tcpConnectButton = QPushButton(Widget)
        self.tcpConnectButton.setObjectName(u"tcpConnectButton")
        self.tcpConnectButton.setGeometry(QRect(210, 20, 227, 24))
        self.tcpIpAddressLabel = QLabel(Widget)
        self.tcpIpAddressLabel.setObjectName(u"tcpIpAddressLabel")
        self.tcpIpAddressLabel.setGeometry(QRect(210, 55, 101, 16))
        self.tcpPortInput = QLineEdit(Widget)
        self.tcpPortInput.setObjectName(u"tcpPortInput")
        self.tcpPortInput.setGeometry(QRect(306, 85, 131, 24))
        self.tcpPortLabel = QLabel(Widget)
        self.tcpPortLabel.setObjectName(u"tcpPortLabel")
        self.tcpPortLabel.setGeometry(QRect(210, 90, 101, 16))
        self.logOutput = QTextBrowser(Widget)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setGeometry(QRect(690, 20, 441, 91))
        self.udpPortLabel = QLabel(Widget)
        self.udpPortLabel.setObjectName(u"udpPortLabel")
        self.udpPortLabel.setGeometry(QRect(450, 90, 101, 16))
        self.udpPortInput = QLineEdit(Widget)
        self.udpPortInput.setObjectName(u"udpPortInput")
        self.udpPortInput.setGeometry(QRect(546, 85, 131, 24))
        self.udpIpAddressInput = QLineEdit(Widget)
        self.udpIpAddressInput.setObjectName(u"udpIpAddressInput")
        self.udpIpAddressInput.setGeometry(QRect(546, 50, 131, 24))
        self.udpConnectButton = QPushButton(Widget)
        self.udpConnectButton.setObjectName(u"udpConnectButton")
        self.udpConnectButton.setGeometry(QRect(450, 20, 227, 24))
        self.udpIpAddressLabel = QLabel(Widget)
        self.udpIpAddressLabel.setObjectName(u"udpIpAddressLabel")
        self.udpIpAddressLabel.setGeometry(QRect(450, 55, 101, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.logoLabel.setText("")
        self.simButton.setText(QCoreApplication.translate("Widget", u"Start/Stop sim", None))
        self.tcpConnectButton.setText(QCoreApplication.translate("Widget", u"Create TCP connection", None))
        self.tcpIpAddressLabel.setText(QCoreApplication.translate("Widget", u"Pad IPv4 address: ", None))
        self.tcpPortLabel.setText(QCoreApplication.translate("Widget", u"Pad port: ", None))
        self.udpPortLabel.setText(QCoreApplication.translate("Widget", u"MG port: ", None))
        self.udpConnectButton.setText(QCoreApplication.translate("Widget", u"Create UDP connection", None))
        self.udpIpAddressLabel.setText(QCoreApplication.translate("Widget", u"MG IPv4 address: ", None))
    # retranslateUi

