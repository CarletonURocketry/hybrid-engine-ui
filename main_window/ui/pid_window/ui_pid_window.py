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
from . import rc_resources

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(763, 643)
        self.pidDiagramLabel = QLabel(Form)
        self.pidDiagramLabel.setObjectName(u"pidDiagramLabel")
        self.pidDiagramLabel.setGeometry(QRect(10, 10, 741, 621))
        self.pidDiagramLabel.setPixmap(QPixmap(u":/diagrams/diagrams/PID_hybrid_readings_trimmed.jpg"))
        self.pidDiagramLabel.setScaledContents(True)
        self.p1Label = QLabel(Form)
        self.p1Label.setObjectName(u"p1Label")
        self.p1Label.setGeometry(QRect(364, 68, 141, 51))
        self.p1Label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0)")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pidDiagramLabel.setText("")
        self.p1Label.setText(QCoreApplication.translate("Form", u"P1:  0000  psi", None))
    # retranslateUi

