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
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

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
        brush = QBrush(QColor(73, 38, 177, 255))
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
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 191, 111))
        self.label.setPixmap(QPixmap(u":/images/logo"))
        self.label.setScaledContents(True)
        self.simButton = QPushButton(Widget)
        self.simButton.setObjectName(u"simButton")
        self.simButton.setGeometry(QRect(230, 50, 101, 24))
        self.engineThrustPlot = PlotWidget(Widget)
        self.engineThrustPlot.setObjectName(u"engineThrustPlot")
        self.engineThrustPlot.setGeometry(QRect(660, 460, 611, 311))
        self.quickWidget = QQuickWidget(Widget)
        self.quickWidget.setObjectName(u"quickWidget")
        self.quickWidget.setGeometry(QRect(460, 50, 300, 200))
        self.quickWidget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hybrid Engine Ground System UI", None))
        self.label.setText("")
        self.simButton.setText(QCoreApplication.translate("Widget", u"Start/Stop sim", None))
    # retranslateUi

