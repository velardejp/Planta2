# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entradas.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Entradas(object):
    def setupUi(self, Entradas):
        if not Entradas.objectName():
            Entradas.setObjectName(u"Entradas")
        Entradas.resize(885, 499)
        self.verticalLayout = QVBoxLayout(Entradas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_frame = QFrame(Entradas)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.central_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.submit_entrada = QPushButton(self.content_frame)
        self.submit_entrada.setObjectName(u"submit_entrada")
        self.submit_entrada.setGeometry(QRect(270, 190, 111, 31))
        self.cantidad_entrada = QLineEdit(self.content_frame)
        self.cantidad_entrada.setObjectName(u"cantidad_entrada")
        self.cantidad_entrada.setGeometry(QRect(250, 130, 141, 31))
        self.cantidad_entrada.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox = QComboBox(self.content_frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(250, 90, 141, 22))

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(Entradas)

        QMetaObject.connectSlotsByName(Entradas)
    # setupUi

    def retranslateUi(self, Entradas):
        Entradas.setWindowTitle(QCoreApplication.translate("Entradas", u"Form", None))
        self.submit_entrada.setText(QCoreApplication.translate("Entradas", u"Entrada", None))
    # retranslateUi

