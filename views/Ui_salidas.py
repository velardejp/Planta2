# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salidas.ui'
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

class Ui_Salidas(object):
    def setupUi(self, Salidas):
        if not Salidas.objectName():
            Salidas.setObjectName(u"Salidas")
        Salidas.resize(885, 499)
        self.verticalLayout = QVBoxLayout(Salidas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_frame = QFrame(Salidas)
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
        self.submit_salida_button = QPushButton(self.content_frame)
        self.submit_salida_button.setObjectName(u"submit_salida_button")
        self.submit_salida_button.setGeometry(QRect(270, 190, 111, 31))
        self.cantidad_salida = QLineEdit(self.content_frame)
        self.cantidad_salida.setObjectName(u"cantidad_salida")
        self.cantidad_salida.setGeometry(QRect(250, 130, 141, 31))
        self.cantidad_salida.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.productos_salida = QComboBox(self.content_frame)
        self.productos_salida.setObjectName(u"productos_salida")
        self.productos_salida.setGeometry(QRect(250, 90, 141, 22))

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(Salidas)

        QMetaObject.connectSlotsByName(Salidas)
    # setupUi

    def retranslateUi(self, Salidas):
        Salidas.setWindowTitle(QCoreApplication.translate("Salidas", u"Form", None))
        self.submit_salida_button.setText(QCoreApplication.translate("Salidas", u"Salida", None))
    # retranslateUi

