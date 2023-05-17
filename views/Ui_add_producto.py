# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_producto.ui'
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

class AddWindowForm(object):
    def setupUi(self, AddWindowForm):
        if not AddWindowForm.objectName():
            AddWindowForm.setObjectName(u"AddWindowForm")
        AddWindowForm.resize(333, 324)
        self.verticalLayout = QVBoxLayout(AddWindowForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_frame = QFrame(AddWindowForm)
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
        self.submit_product_button = QPushButton(self.content_frame)
        self.submit_product_button.setObjectName(u"submit_product_button")
        self.submit_product_button.setGeometry(QRect(100, 160, 111, 31))
        self.product_name = QLineEdit(self.content_frame)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setGeometry(QRect(60, 60, 191, 21))
        self.product_name.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.unidad_medida = QLineEdit(self.content_frame)
        self.unidad_medida.setObjectName(u"unidad_medida")
        self.unidad_medida.setGeometry(QRect(60, 110, 191, 21))
        self.unidad_medida.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 181, 16))
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 191, 16))

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(AddWindowForm)

        QMetaObject.connectSlotsByName(AddWindowForm)
    # setupUi

    def retranslateUi(self, AddWindowForm):
        AddWindowForm.setWindowTitle(QCoreApplication.translate("AddWindowForm", u"Form", None))
        self.submit_product_button.setText(QCoreApplication.translate("AddWindowForm", u"Agregar Producto", None))
        self.label.setText(QCoreApplication.translate("AddWindowForm", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("AddWindowForm", u"Unidad de medida:", None))
    # retranslateUi

