# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pid_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_PIDWindow(object):
    def setupUi(self, PIDWindow):
        if not PIDWindow.objectName():
            PIDWindow.setObjectName(u"PIDWindow")
        PIDWindow.resize(763, 643)
        self.pidDiagramLabel = QLabel(PIDWindow)
        self.pidDiagramLabel.setObjectName(u"pidDiagramLabel")
        self.pidDiagramLabel.setGeometry(QRect(10, 10, 741, 621))
        self.pidDiagramLabel.setPixmap(QPixmap(u":/diagrams/diagrams/PID_hybrid_readings_trimmed.jpg"))
        self.pidDiagramLabel.setScaledContents(True)
        self.p1ValLabel = QLabel(PIDWindow)
        self.p1ValLabel.setObjectName(u"p1ValLabel")
        self.p1ValLabel.setGeometry(QRect(393, 69, 51, 51))
        self.p1ValLabel.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p1Label = QLabel(PIDWindow)
        self.p1Label.setObjectName(u"p1Label")
        self.p1Label.setGeometry(QRect(368, 84, 49, 16))
        self.p1Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p2ValLabel = QLabel(PIDWindow)
        self.p2ValLabel.setObjectName(u"p2ValLabel")
        self.p2ValLabel.setGeometry(QRect(563, 438, 51, 51))
        self.p2ValLabel.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p2Label = QLabel(PIDWindow)
        self.p2Label.setObjectName(u"p2Label")
        self.p2Label.setGeometry(QRect(538, 453, 49, 16))
        self.p2Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p3ValLabel = QLabel(PIDWindow)
        self.p3ValLabel.setObjectName(u"p3ValLabel")
        self.p3ValLabel.setGeometry(QRect(218, 432, 51, 51))
        self.p3ValLabel.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p3Label = QLabel(PIDWindow)
        self.p3Label.setObjectName(u"p3Label")
        self.p3Label.setGeometry(QRect(193, 448, 49, 16))
        self.p3Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.t1ValLabel = QLabel(PIDWindow)
        self.t1ValLabel.setObjectName(u"t1ValLabel")
        self.t1ValLabel.setGeometry(QRect(601, 275, 51, 51))
        self.t1ValLabel.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.t1Label = QLabel(PIDWindow)
        self.t1Label.setObjectName(u"t1Label")
        self.t1Label.setGeometry(QRect(574, 282, 49, 16))
        self.t1Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p1ValLabel_2 = QLabel(PIDWindow)
        self.p1ValLabel_2.setObjectName(u"p1ValLabel_2")
        self.p1ValLabel_2.setGeometry(QRect(151, 433, 51, 51))
        self.p1ValLabel_2.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")
        self.p1Label_2 = QLabel(PIDWindow)
        self.p1Label_2.setObjectName(u"p1Label_2")
        self.p1Label_2.setGeometry(QRect(122, 448, 49, 16))
        self.p1Label_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")

        self.retranslateUi(PIDWindow)

        QMetaObject.connectSlotsByName(PIDWindow)
    # setupUi

    def retranslateUi(self, PIDWindow):
        PIDWindow.setWindowTitle(QCoreApplication.translate("PIDWindow", u"Hybrid PID Diagram", None))
        self.pidDiagramLabel.setText("")
        self.p1ValLabel.setText(QCoreApplication.translate("PIDWindow", u"0000 psi", None))
        self.p1Label.setText(QCoreApplication.translate("PIDWindow", u"P1:", None))
        self.p2ValLabel.setText(QCoreApplication.translate("PIDWindow", u"0000 psi", None))
        self.p2Label.setText(QCoreApplication.translate("PIDWindow", u"P2:", None))
        self.p3ValLabel.setText(QCoreApplication.translate("PIDWindow", u"0000 psi", None))
        self.p3Label.setText(QCoreApplication.translate("PIDWindow", u"P3:", None))
        self.t1ValLabel.setText(QCoreApplication.translate("PIDWindow", u"0000 \u00b0C", None))
        self.t1Label.setText(QCoreApplication.translate("PIDWindow", u"T1:", None))
        self.p1ValLabel_2.setText(QCoreApplication.translate("PIDWindow", u"0000 \u00b0C", None))
        self.p1Label_2.setText(QCoreApplication.translate("PIDWindow", u"T2:", None))
    # retranslateUi

