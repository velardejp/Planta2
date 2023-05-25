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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_exit_window(object):
    def setupUi(self, exit_window):
        if not exit_window.objectName():
            exit_window.setObjectName(u"exit_window")
        exit_window.resize(561, 300)
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
        self.productos_exit = QComboBox(self.content_frame)
        self.productos_exit.setObjectName(u"productos_exit")
        self.productos_exit.setGeometry(QRect(10, 50, 171, 51))
        self.productos_exit.setStyleSheet(u"QComboBox {\n"
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
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 171, 45))
        self.label.setLayoutDirection(Qt.LeftToRight)
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
        self.cantidad_exit_spin = QDoubleSpinBox(self.content_frame)
        self.cantidad_exit_spin.setObjectName(u"cantidad_exit_spin")
        self.cantidad_exit_spin.setGeometry(QRect(10, 140, 171, 51))
        self.cantidad_exit_spin.setStyleSheet(u" QDoubleSpinBox {\n"
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
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 171, 45))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
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
        self.submit_exit_button = QPushButton(self.content_frame)
        self.submit_exit_button.setObjectName(u"submit_exit_button")
        self.submit_exit_button.setGeometry(QRect(300, 200, 141, 51))
        self.submit_exit_button.setStyleSheet(u"QPushButton {\n"
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
        self.tabla_productos_salida = QTableWidget(self.content_frame)
        if (self.tabla_productos_salida.columnCount() < 2):
            self.tabla_productos_salida.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_productos_salida.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_productos_salida.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabla_productos_salida.setObjectName(u"tabla_productos_salida")
        self.tabla_productos_salida.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Oculta el índice de la tabla.
        self.tabla_productos_salida.verticalHeader().setVisible(False)
        self.tabla_productos_salida.setGeometry(QRect(220, 10, 311, 192))
        self.tabla_productos_salida.setStyleSheet(u"QTableWidget {\n"
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
        self.agrega_ingrediente_salida = QPushButton(self.content_frame)
        self.agrega_ingrediente_salida.setObjectName(u"agrega_ingrediente_salida")
        self.agrega_ingrediente_salida.setGeometry(QRect(40, 190, 111, 51))
        self.agrega_ingrediente_salida.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(exit_window)

        QMetaObject.connectSlotsByName(exit_window)
    # setupUi

    def retranslateUi(self, exit_window):
        exit_window.setWindowTitle(QCoreApplication.translate("exit_window", u"Nueva salida", None))
        self.label.setText(QCoreApplication.translate("exit_window", u"PRODUCTO", None))
        self.label_2.setText(QCoreApplication.translate("exit_window", u"CANTIDAD", None))
        self.submit_exit_button.setText(QCoreApplication.translate("exit_window", u"Aplicar", None))
        ___qtablewidgetitem = self.tabla_productos_salida.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("exit_window", u"Producto", None));
        ___qtablewidgetitem1 = self.tabla_productos_salida.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("exit_window", u"Cantidad", None));
        self.agrega_ingrediente_salida.setText(QCoreApplication.translate("exit_window", u"Aplicar", None))
    # retranslateUi

