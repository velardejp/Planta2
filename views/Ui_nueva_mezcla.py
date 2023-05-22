# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nueva_mezcla.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_nueva_mezcla_window(object):
    def setupUi(self, nueva_mezcla_window):
        if not nueva_mezcla_window.objectName():
            nueva_mezcla_window.setObjectName(u"nueva_mezcla_window")
        nueva_mezcla_window.resize(291, 235)
        self.verticalLayout = QVBoxLayout(nueva_mezcla_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(nueva_mezcla_window)
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
        self.content_frame = QFrame(self.backgroundcolor_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 111, 41))
        self.label.setStyleSheet(u"QLabel {\n"
"       color: #ffffff;            /* Color del texto */\n"
"       \n"
"       border: 2px solid #457B9D; /* Color del borde */\n"
"        border-radius: 5px;        /* Radio del borde (para bordes redondeados) */\n"
"        padding: 5px;              /* Espacio interior alrededor del texto */\n"
"        font-size: 14px;           /* Tama\\u00f1o del texto */\n"
"    }")
        self.nombre_mezcla = QLineEdit(self.content_frame)
        self.nombre_mezcla.setObjectName(u"nombre_mezcla")
        self.nombre_mezcla.setGeometry(QRect(30, 80, 211, 31))
        self.nombre_mezcla.setStyleSheet(u"QLineEdit {\n"
"		background-color: rgb(255, 255, 255);\n"
"       \n"
"        color: #FFFFFF;\n"
"        border: 2px solid #457B9D;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        border: 2px solid #E63946;\n"
"    }")
        self.submit_mezcla_button = QPushButton(self.content_frame)
        self.submit_mezcla_button.setObjectName(u"submit_mezcla_button")
        self.submit_mezcla_button.setGeometry(QRect(70, 120, 121, 41))
        self.submit_mezcla_button.setStyleSheet(u" QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(nueva_mezcla_window)

        QMetaObject.connectSlotsByName(nueva_mezcla_window)
    # setupUi

    def retranslateUi(self, nueva_mezcla_window):
        nueva_mezcla_window.setWindowTitle(QCoreApplication.translate("nueva_mezcla_window", u"Form", None))
        self.label.setText(QCoreApplication.translate("nueva_mezcla_window", u"Nombre", None))
        self.submit_mezcla_button.setText(QCoreApplication.translate("nueva_mezcla_window", u"Agregar", None))
    # retranslateUi

