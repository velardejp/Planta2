# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nueva_entrada_ventana.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_nueva_entrada(object):
    def setupUi(self, nueva_entrada):
        if not nueva_entrada.objectName():
            nueva_entrada.setObjectName(u"nueva_entrada")
        nueva_entrada.resize(561, 300)
        self.verticalLayout = QVBoxLayout(nueva_entrada)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(nueva_entrada)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.backgroundcolor_frame = QFrame(self.central_frame)
        self.backgroundcolor_frame.setObjectName(u"backgroundcolor_frame")
        self.backgroundcolor_frame.setStyleSheet(u"background-color: #537188;\n"
"")
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
        self.productos_entrada = QComboBox(self.content_frame)
        self.productos_entrada.setObjectName(u"productos_entrada")
        self.productos_entrada.setGeometry(QRect(10, 50, 171, 51))
        self.productos_entrada.setStyleSheet(u"QComboBox {\n"
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
"}\n"
"")
        self.cantidad_entrada = QDoubleSpinBox(self.content_frame)
        self.cantidad_entrada.setObjectName(u"cantidad_entrada")
        self.cantidad_entrada.setGeometry(QRect(10, 140, 171, 51))
        self.cantidad_entrada.setStyleSheet(u"QDoubleSpinBox {\n"
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
"}\n"
"\n"
"")
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 171, 45))
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
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 171, 45))
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
        self.submit_entrada_button = QPushButton(self.content_frame)
        self.submit_entrada_button.setObjectName(u"submit_entrada_button")
        self.submit_entrada_button.setGeometry(QRect(300, 200, 141, 51))
        self.submit_entrada_button.setStyleSheet(u"QPushButton {\n"
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
        self.agregar_producto = QPushButton(self.content_frame)
        self.agregar_producto.setObjectName(u"agregar_producto")
        self.agregar_producto.setGeometry(QRect(40, 190, 111, 51))
        self.agregar_producto.setStyleSheet(u"QPushButton {\n"
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
        self.tabla_new_entrada = QTableWidget(self.content_frame)
        if (self.tabla_new_entrada.columnCount() < 2):
            self.tabla_new_entrada.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_new_entrada.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_new_entrada.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabla_new_entrada.setObjectName(u"tabla_new_entrada")
        self.tabla_new_entrada.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Oculta el índice de la tabla.
        self.tabla_new_entrada.verticalHeader().setVisible(False)
        self.tabla_new_entrada.setGeometry(QRect(220, 10, 311, 192))
        self.tabla_new_entrada.setStyleSheet(u"QTableWidget {\n"
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

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(nueva_entrada)

        QMetaObject.connectSlotsByName(nueva_entrada)
    # setupUi

    def retranslateUi(self, nueva_entrada):
        nueva_entrada.setWindowTitle(QCoreApplication.translate("nueva_entrada", u"Nueva entrada", None))
        self.label.setText(QCoreApplication.translate("nueva_entrada", u"Producto", None))
        self.label_2.setText(QCoreApplication.translate("nueva_entrada", u"Cantidad", None))
        self.submit_entrada_button.setText(QCoreApplication.translate("nueva_entrada", u"Agregar", None))
        self.agregar_producto.setText(QCoreApplication.translate("nueva_entrada", u"A\u00f1adir", None))
        ___qtablewidgetitem = self.tabla_new_entrada.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("nueva_entrada", u"Producto", None));
        ___qtablewidgetitem1 = self.tabla_new_entrada.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("nueva_entrada", u"Cantidad", None));
    # retranslateUi

