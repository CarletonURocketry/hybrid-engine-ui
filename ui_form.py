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
        self.ipAddressInput = QLineEdit(Widget)
        self.ipAddressInput.setObjectName(u"ipAddressInput")
        self.ipAddressInput.setGeometry(QRect(306, 50, 131, 24))
        self.tcpConnectButton = QPushButton(Widget)
        self.tcpConnectButton.setObjectName(u"tcpConnectButton")
        self.tcpConnectButton.setGeometry(QRect(210, 20, 227, 24))
        self.ipAddressLabel = QLabel(Widget)
        self.ipAddressLabel.setObjectName(u"ipAddressLabel")
        self.ipAddressLabel.setGeometry(QRect(210, 55, 101, 16))
        self.portInput = QLineEdit(Widget)
        self.portInput.setObjectName(u"portInput")
        self.portInput.setGeometry(QRect(306, 85, 131, 24))
        self.portLabel = QLabel(Widget)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setGeometry(QRect(210, 90, 101, 16))
        self.logOutput = QTextBrowser(Widget)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setGeometry(QRect(690, 20, 441, 91))
        self.portLabel_UDP = QLabel(Widget)
        self.portLabel_UDP.setObjectName(u"portLabel_UDP")
        self.portLabel_UDP.setGeometry(QRect(450, 90, 101, 16))
        self.portInput_UDP = QLineEdit(Widget)
        self.portInput_UDP.setObjectName(u"portInput_UDP")
        self.portInput_UDP.setGeometry(QRect(546, 85, 131, 24))
        self.ipAddressInput_UDP = QLineEdit(Widget)
        self.ipAddressInput_UDP.setObjectName(u"ipAddressInput_UDP")
        self.ipAddressInput_UDP.setGeometry(QRect(546, 50, 131, 24))
        self.udpConnectButton = QPushButton(Widget)
        self.udpConnectButton.setObjectName(u"udpConnectButton")
        self.udpConnectButton.setGeometry(QRect(450, 20, 227, 24))
        self.ipAddressLabel_UDP = QLabel(Widget)
        self.ipAddressLabel_UDP.setObjectName(u"ipAddressLabel_UDP")
        self.ipAddressLabel_UDP.setGeometry(QRect(450, 55, 101, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.logoLabel.setText("")
        self.simButton.setText(QCoreApplication.translate("Widget", u"Start/Stop sim", None))
        self.tcpConnectButton.setText(QCoreApplication.translate("Widget", u"Create TCP connection", None))
        self.ipAddressLabel.setText(QCoreApplication.translate("Widget", u"Pad IPv4 address: ", None))
        self.portLabel.setText(QCoreApplication.translate("Widget", u"Pad port: ", None))
        self.portLabel_UDP.setText(QCoreApplication.translate("Widget", u"MG port: ", None))
        self.udpConnectButton.setText(QCoreApplication.translate("Widget", u"Create UDP connection", None))
        self.ipAddressLabel_UDP.setText(QCoreApplication.translate("Widget", u"MG IPv4 address: ", None))
    # retranslateUi

