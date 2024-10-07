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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

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
        self.udpConnectButton = QPushButton(Widget)
        self.udpConnectButton.setObjectName(u"udpConnectButton")

        self.connectionLayout.addWidget(self.udpConnectButton)

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

        self.portLayout.addWidget(self.udpPortLabel)

        self.udpPortInput = QLineEdit(Widget)
        self.udpPortInput.setObjectName(u"udpPortInput")

        self.portLayout.addWidget(self.udpPortInput)


        self.connectionLayout.addLayout(self.portLayout)


        self.controlLayout.addLayout(self.connectionLayout, 0, 1, 1, 1)

        self.logOutput = QTextBrowser(Widget)
        self.logOutput.setObjectName(u"logOutput")

        self.controlLayout.addWidget(self.logOutput, 0, 2, 1, 1)

        self.simButton = QPushButton(Widget)
        self.simButton.setObjectName(u"simButton")

        self.controlLayout.addWidget(self.simButton, 0, 3, 1, 1)

        self.graphicsView = QGraphicsView(Widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)
        self.graphicsView.setRenderHints(QPainter.RenderHint.SmoothPixmapTransform)
        self.graphicsView.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)

        self.controlLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.controlLayout.setColumnStretch(0, 3)
        self.controlLayout.setColumnStretch(1, 4)
        self.controlLayout.setColumnStretch(2, 14)
        self.controlLayout.setColumnStretch(3, 2)

        self.verticalLayout.addLayout(self.controlLayout)

        self.plotLayout = QGridLayout()
        self.plotLayout.setSpacing(20)
        self.plotLayout.setObjectName(u"plotLayout")
        self.temperaturePlot = PlotWidget(Widget)
        self.temperaturePlot.setObjectName(u"temperaturePlot")
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.temperaturePlot.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.temperaturePlot.setForegroundBrush(brush1)

        self.plotLayout.addWidget(self.temperaturePlot, 0, 1, 1, 1)

        self.engineThrustPlot = PlotWidget(Widget)
        self.engineThrustPlot.setObjectName(u"engineThrustPlot")

        self.plotLayout.addWidget(self.engineThrustPlot, 1, 1, 1, 1)

        self.pressurePlot = PlotWidget(Widget)
        self.pressurePlot.setObjectName(u"pressurePlot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressurePlot.sizePolicy().hasHeightForWidth())
        self.pressurePlot.setSizePolicy(sizePolicy)

        self.plotLayout.addWidget(self.pressurePlot, 0, 0, 1, 1)

        self.tankMassPlot = PlotWidget(Widget)
        self.tankMassPlot.setObjectName(u"tankMassPlot")

        self.plotLayout.addWidget(self.tankMassPlot, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.plotLayout)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 14)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.udpConnectButton.setText(QCoreApplication.translate("Widget", u"Create UDP connection", None))
        self.udpIpAddressLabel.setText(QCoreApplication.translate("Widget", u"MG IPv4 address: ", None))
        self.udpPortLabel.setText(QCoreApplication.translate("Widget", u"MG port: ", None))
        self.simButton.setText(QCoreApplication.translate("Widget", u"Start/Stop sim", None))
    # retranslateUi

