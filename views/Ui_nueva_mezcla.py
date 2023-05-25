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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_nueva_mezcla_window(object):
    def setupUi(self, nueva_mezcla_window):
        if not nueva_mezcla_window.objectName():
            nueva_mezcla_window.setObjectName(u"nueva_mezcla_window")
        nueva_mezcla_window.resize(698, 364)
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
        self.backgroundcolor_frame.setStyleSheet(u"background-color: #537188;")
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
        self.label.setGeometry(QRect(10, 20, 251, 41))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border: 2px solid #537188;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    background-color: #CBB279;\n"
"}")
        self.nombre_mezcla = QLineEdit(self.content_frame)
        self.nombre_mezcla.setObjectName(u"nombre_mezcla")
        self.nombre_mezcla.setGeometry(QRect(10, 60, 251, 51))
        self.nombre_mezcla.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E1D4BB;\n"
"    color: #537188;\n"
"    border: 2px solid #CBB279;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"}")
        self.submit_mezcla_button = QPushButton(self.content_frame)
        self.submit_mezcla_button.setObjectName(u"submit_mezcla_button")
        self.submit_mezcla_button.setGeometry(QRect(275, 260, 401, 51))
        self.submit_mezcla_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #E1D4BB;\n"
"    color: #537188;\n"
"    border: 2px solid #CBB279;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CBB279;\n"
"    border: 2px solid #537188;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CBB279;\n"
"    border: 2px solid #537188;\n"
"    padding-left: 7px;\n"
"}")
        self.ingrediente_nueva_mezcla = QComboBox(self.content_frame)
        self.ingrediente_nueva_mezcla.setObjectName(u"ingrediente_nueva_mezcla")
        self.ingrediente_nueva_mezcla.setGeometry(QRect(10, 150, 251, 51))
        self.ingrediente_nueva_mezcla.setStyleSheet(u"QComboBox {\n"
"    background-color: #E1D4BB;\n"
"    color: #537188;\n"
"    border: 2px solid #CBB279;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-expand-arrow-24.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #537188;\n"
"    selection-background-color: #CBB279;\n"
"}")
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 251, 41))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border: 2px solid #537188;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    background-color: #CBB279;\n"
"}")
        self.tabla_ingredientes = QTableWidget(self.content_frame)
        if (self.tabla_ingredientes.columnCount() < 3):
            self.tabla_ingredientes.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_ingredientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_ingredientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_ingredientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabla_ingredientes.setObjectName(u"tabla_ingredientes")
        self.tabla_ingredientes.setGeometry(QRect(275, 20, 401, 231))
        self.tabla_ingredientes.setStyleSheet(u"QTableWidget {\n"
"    background-color: #E1D4BB;\n"
"    color: #537188;\n"
"    border: 2px solid #CBB279;\n"
"    border-radius: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    gridline-color: #537188;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid #537188;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #CBB279;\n"
"    color: #E1D4BB;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #E1D4BB;\n"
"    color: #537188;\n"
"    padding: 5px;\n"
"    border: 2px solid #CBB279;\n"
"    border-radius: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"}")
        self.agregar_ingrediente = QPushButton(self.content_frame)
        self.agregar_ingrediente.setObjectName(u"agregar_ingrediente")
        self.agregar_ingrediente.setGeometry(QRect(140, 200, 121, 51))
        self.agregar_ingrediente.setStyleSheet(u"QPushButton {\n"
"    background-color: #E1D4BB;\n"
"    color: #537188;\n"
"    border: 2px solid #CBB279;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CBB279;\n"
"    border: 2px solid #537188;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CBB279;\n"
"    border: 2px solid #537188;\n"
"    padding-left: 7px;\n"
"}")
        self.cantidad_ingrediente = QDoubleSpinBox(self.content_frame)
        self.cantidad_ingrediente.setObjectName(u"cantidad_ingrediente")
        self.cantidad_ingrediente.setGeometry(QRect(10, 200, 121, 51))
        self.cantidad_ingrediente.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #E1D4BB;\n"
"    color: #537188;\n"
"    border: 2px solid #CBB279;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    width: 20px;\n"
"    border: none;\n"
"    background: #537188 url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-collapse-arrow-24.png) no-repeat center;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    width: 20px;\n"
"    border: none;\n"
"    background: #537188 url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-expand-arrow-24.png) no-repeat center;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background: #CBB279 url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-collapse-arrow-24.png) no-repeat center;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background: #CBB279 url(C:/Users/velar/OneDrive/Escritorio/Planta2/assets/icons8-expand-arrow-24.png) no-repeat center;\n"
"}")

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(nueva_mezcla_window)

        QMetaObject.connectSlotsByName(nueva_mezcla_window)
    # setupUi

    def retranslateUi(self, nueva_mezcla_window):
        nueva_mezcla_window.setWindowTitle(QCoreApplication.translate("nueva_mezcla_window", u"Nueva mezcla", None))
        self.label.setText(QCoreApplication.translate("nueva_mezcla_window", u"Nombre", None))
        self.submit_mezcla_button.setText(QCoreApplication.translate("nueva_mezcla_window", u"Agregar", None))
        self.label_2.setText(QCoreApplication.translate("nueva_mezcla_window", u"Ingredientes", None))
        ___qtablewidgetitem = self.tabla_ingredientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("nueva_mezcla_window", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_ingredientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("nueva_mezcla_window", u"Ingrediente", None));
        ___qtablewidgetitem2 = self.tabla_ingredientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("nueva_mezcla_window", u"Cantidad", None));
        self.agregar_ingrediente.setText(QCoreApplication.translate("nueva_mezcla_window", u"A\u00f1adir", None))
    # retranslateUi

