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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from pyqtgraph import PlotWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1298, 727)
        self.plot1 = PlotWidget(Widget)
        self.plot1.setObjectName(u"plot1")
        self.plot1.setGeometry(QRect(10, 10, 411, 271))
        self.plot1_2 = PlotWidget(Widget)
        self.plot1_2.setObjectName(u"plot1_2")
        self.plot1_2.setGeometry(QRect(440, 10, 411, 271))
        self.plot1_3 = PlotWidget(Widget)
        self.plot1_3.setObjectName(u"plot1_3")
        self.plot1_3.setGeometry(QRect(870, 10, 411, 271))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
    # retranslateUi

