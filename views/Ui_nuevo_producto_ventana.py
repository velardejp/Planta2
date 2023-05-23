# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevo_producto_ventana.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ventana_nuevo_producto(object):
    def setupUi(self, ventana_nuevo_producto):
        if not ventana_nuevo_producto.objectName():
            ventana_nuevo_producto.setObjectName(u"ventana_nuevo_producto")
        ventana_nuevo_producto.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ventana_nuevo_producto)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(ventana_nuevo_producto)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.backgroundcolor_frame = QFrame(self.central_frame)
        self.backgroundcolor_frame.setObjectName(u"backgroundcolor_frame")
        self.backgroundcolor_frame.setStyleSheet(u"background-color: rgb(29, 53, 87);")
        self.backgroundcolor_frame.setFrameShape(QFrame.StyledPanel)
        self.backgroundcolor_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.backgroundcolor_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.backgroundcolor_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nombre_nuevo_prod = QLineEdit(self.frame)
        self.nombre_nuevo_prod.setObjectName(u"nombre_nuevo_prod")
        self.nombre_nuevo_prod.setGeometry(QRect(90, 60, 211, 41))
        self.nombre_nuevo_prod.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #457B9D;\n"
"        border-radius: 15px;\n"
"        padding: 5px;\n"
"        background-color: white;\n"
"        color: black;\n"
"        font-size: 16px;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border: 2px solid #34eb4f;\n"
"    }")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 151, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"        color: #ffffff;            /* Color del texto */\n"
"        \n"
"        border: 2px solid #457B9D; /* Color del borde */\n"
"        border-radius: 5px;        /* Radio del borde (para bordes redondeados) */\n"
"        padding: 5px;              /* Espacio interior alrededor del texto */\n"
"        font-size: 14px;           /* Tama\u00f1o del texto */\n"
"    }")
        self.kilos_radiobutton = QRadioButton(self.frame)
        self.kilos_radiobutton.setObjectName(u"kilos_radiobutton")
        self.kilos_radiobutton.setGeometry(QRect(60, 140, 131, 20))
        self.kilos_radiobutton.setStyleSheet(u"QRadioButton {\n"
"        font-size: 16px;\n"
"        color: white;\n"
"    }\n"
"    QRadioButton::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"    }")
        self.litros_radiobutton = QRadioButton(self.frame)
        self.litros_radiobutton.setObjectName(u"litros_radiobutton")
        self.litros_radiobutton.setGeometry(QRect(200, 140, 121, 20))
        self.litros_radiobutton.setStyleSheet(u"QRadioButton {\n"
"        font-size: 16px;\n"
"        color: white;\n"
"    }\n"
"    QRadioButton::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"    }\n"
"  ")
        self.submit_nuevoproducto_button = QPushButton(self.frame)
        self.submit_nuevoproducto_button.setObjectName(u"submit_nuevoproducto_button")
        self.submit_nuevoproducto_button.setGeometry(QRect(120, 200, 131, 41))
        self.submit_nuevoproducto_button.setStyleSheet(u" QPushButton {\n"
"        background-color: #457B9D;\n"
"        color: #F1FAEE;\n"
"        border: 2px solid #1D3557;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        font-size: 14px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #1D3557;\n"
"        border: 2px solid #457B9D;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D3557;\n"
"        border: 2px solid #457B9D;\n"
"        padding-left: 7px;  /* Para dar un efecto de \"presi\u00f3n\" */\n"
"    }")

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(ventana_nuevo_producto)

        QMetaObject.connectSlotsByName(ventana_nuevo_producto)
    # setupUi

    def retranslateUi(self, ventana_nuevo_producto):
        ventana_nuevo_producto.setWindowTitle(QCoreApplication.translate("ventana_nuevo_producto", u"Form", None))
        self.label.setText(QCoreApplication.translate("ventana_nuevo_producto", u"Nombre", None))
        self.kilos_radiobutton.setText(QCoreApplication.translate("ventana_nuevo_producto", u"Kilogramos", None))
        self.litros_radiobutton.setText(QCoreApplication.translate("ventana_nuevo_producto", u"Litros", None))
        self.submit_nuevoproducto_button.setText(QCoreApplication.translate("ventana_nuevo_producto", u"Agregar", None))
    # retranslateUi

