# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_salidas.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_exit_window(object):
    def setupUi(self, exit_window):
        if not exit_window.objectName():
            exit_window.setObjectName(u"exit_window")
        exit_window.resize(302, 294)
        self.verticalLayout = QVBoxLayout(exit_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(exit_window)
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
        self.productos_exit = QComboBox(self.content_frame)
        self.productos_exit.setObjectName(u"productos_exit")
        self.productos_exit.setGeometry(QRect(70, 60, 151, 21))
        self.productos_exit.setStyleSheet(u"QComboBox {\n"
"        background-color: #F1FAEE;\n"
"        color: #1D3557;\n"
"        border: 2px solid #457B9D;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        font-size: 14px;\n"
"    }\n"
"    QComboBox::drop-down {\n"
"        border: none;\n"
"    }\n"
"    QComboBox::down-arrow {\n"
"        image: url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-expand-arrow-24.png);\n"
"    }\n"
"    QComboBox QAbstractItemView {\n"
"        border: 2px solid #457B9D;\n"
"        selection-background-color: #457B9D;\n"
"    }")
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 91, 31))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"        color: #ffffff;            /* Color del texto */\n"
"        \n"
"        border: 2px solid #457B9D; /* Color del borde */\n"
"        border-radius: 5px;        /* Radio del borde (para bordes redondeados) */\n"
"        padding: 5px;              /* Espacio interior alrededor del texto */\n"
"        font-size: 14px;           /* Tama\u00f1o del texto */\n"
"    }")
        self.cantidad_exit_spin = QDoubleSpinBox(self.content_frame)
        self.cantidad_exit_spin.setObjectName(u"cantidad_exit_spin")
        self.cantidad_exit_spin.setGeometry(QRect(70, 140, 81, 41))
        self.cantidad_exit_spin.setStyleSheet(u" QDoubleSpinBox {\n"
"        background-color: #F1FAEE;\n"
"        color: #1D3557;\n"
"        border: 2px solid #457B9D;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        font-size: 14px;\n"
"    }\n"
"    QDoubleSpinBox::up-button {\n"
"        width: 20px;\n"
"        border: none;\n"
"        background: #457B9D url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-collapse-arrow-24.png) no-repeat center;\n"
"    }\n"
"    QDoubleSpinBox::down-button {\n"
"        width: 20px;\n"
"        border: none;\n"
"        background: #457B9D url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-expand-arrow-24.png) no-repeat center;\n"
"    }\n"
"    QDoubleSpinBox::up-button:pressed {\n"
"        background: #1D3557 url(path_to_up_arrow) no-repeat center;\n"
"    }\n"
"    QDoubleSpinBox::down-button:pressed {\n"
"        background: #1D3557 url(path_to_down_arrow) no-repeat center;\n"
"    }")
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 100, 91, 31))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"QLabel {\n"
"        color: #ffffff;            /* Color del texto */\n"
"        \n"
"        border: 2px solid #457B9D; /* Color del borde */\n"
"        border-radius: 5px;        /* Radio del borde (para bordes redondeados) */\n"
"        padding: 5px;              /* Espacio interior alrededor del texto */\n"
"        font-size: 14px;           /* Tama\u00f1o del texto */\n"
"    }")
        self.submit_exit_button = QPushButton(self.content_frame)
        self.submit_exit_button.setObjectName(u"submit_exit_button")
        self.submit_exit_button.setGeometry(QRect(90, 200, 101, 31))
        self.submit_exit_button.setStyleSheet(u"QPushButton {\n"
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


        self.retranslateUi(exit_window)

        QMetaObject.connectSlotsByName(exit_window)
    # setupUi

    def retranslateUi(self, exit_window):
        exit_window.setWindowTitle(QCoreApplication.translate("exit_window", u"Form", None))
        self.label.setText(QCoreApplication.translate("exit_window", u"PRODUCTO", None))
        self.label_2.setText(QCoreApplication.translate("exit_window", u"CANTIDAD", None))
        self.submit_exit_button.setText(QCoreApplication.translate("exit_window", u"Aplicar", None))
    # retranslateUi

