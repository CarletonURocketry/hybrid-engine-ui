# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pid_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
from . import rc_resources

class Ui_PIDWindow(object):
    def setupUi(self, PIDWindow):
        if not PIDWindow.objectName():
            PIDWindow.setObjectName(u"PIDWindow")
        PIDWindow.resize(915, 665)
        font = QFont()
        font.setPointSize(29)
        PIDWindow.setFont(font)
        self.p1Label = QLabel(PIDWindow)
        self.p1Label.setObjectName(u"p1Label")
        self.p1Label.setGeometry(QRect(202, 349, 49, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.p1Label.setFont(font1)
        self.p1Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p2ValLabel = QLabel(PIDWindow)
        self.p2ValLabel.setObjectName(u"p2ValLabel")
        self.p2ValLabel.setGeometry(QRect(266, 112, 81, 51))
        self.p2ValLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.p2Label = QLabel(PIDWindow)
        self.p2Label.setObjectName(u"p2Label")
        self.p2Label.setGeometry(QRect(234, 127, 49, 20))
        self.p2Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p3ValLabel = QLabel(PIDWindow)
        self.p3ValLabel.setObjectName(u"p3ValLabel")
        self.p3ValLabel.setGeometry(QRect(535, 46, 81, 51))
        self.p3ValLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.p3Label = QLabel(PIDWindow)
        self.p3Label.setObjectName(u"p3Label")
        self.p3Label.setGeometry(QRect(506, 60, 49, 20))
        self.p3Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p4Label = QLabel(PIDWindow)
        self.p4Label.setObjectName(u"p4Label")
        self.p4Label.setGeometry(QRect(588, 411, 49, 16))
        self.p4Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p4ValLabel = QLabel(PIDWindow)
        self.p4ValLabel.setObjectName(u"p4ValLabel")
        self.p4ValLabel.setGeometry(QRect(619, 397, 71, 51))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.p4ValLabel.setFont(font2)
        self.p4ValLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.p1ValLabel = QLabel(PIDWindow)
        self.p1ValLabel.setObjectName(u"p1ValLabel")
        self.p1ValLabel.setGeometry(QRect(230, 354, 111, 41))
        self.p1ValLabel.setFont(font2)
        self.p1ValLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.diagramLabel = QLabel(PIDWindow)
        self.diagramLabel.setObjectName(u"diagramLabel")
        self.diagramLabel.setGeometry(QRect(10, 10, 891, 641))
        self.diagramLabel.setPixmap(QPixmap(u":/diagrams/diagrams/Cold Flow 20-05-2025.png"))
        self.diagramLabel.setScaledContents(True)
        self.diagramLabel.raise_()
        self.p1Label.raise_()
        self.p2ValLabel.raise_()
        self.p2Label.raise_()
        self.p3ValLabel.raise_()
        self.p3Label.raise_()
        self.p4Label.raise_()
        self.p4ValLabel.raise_()
        self.p1ValLabel.raise_()

        self.retranslateUi(PIDWindow)

        QMetaObject.connectSlotsByName(PIDWindow)
    # setupUi

    def retranslateUi(self, PIDWindow):
        PIDWindow.setWindowTitle(QCoreApplication.translate("PIDWindow", u"Hybrid PID Diagram", None))
        self.p1Label.setText(QCoreApplication.translate("PIDWindow", u"P1:", None))
        self.p2ValLabel.setText(QCoreApplication.translate("PIDWindow", u"00.00 psi", None))
        self.p2Label.setText(QCoreApplication.translate("PIDWindow", u"P2:", None))
        self.p3ValLabel.setText(QCoreApplication.translate("PIDWindow", u"00.00 psi", None))
        self.p3Label.setText(QCoreApplication.translate("PIDWindow", u"P3:", None))
        self.p4Label.setText(QCoreApplication.translate("PIDWindow", u"P4:", None))
        self.p4ValLabel.setText(QCoreApplication.translate("PIDWindow", u"00.00 psi", None))
        self.p1ValLabel.setText(QCoreApplication.translate("PIDWindow", u"00.00 psi", None))
        self.diagramLabel.setText("")
    # retranslateUi

