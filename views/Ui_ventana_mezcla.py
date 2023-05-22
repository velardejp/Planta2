# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_mezcla.ui'
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

class Ui_exit_mezcla_window(object):
    def setupUi(self, exit_mezcla_window):
        if not exit_mezcla_window.objectName():
            exit_mezcla_window.setObjectName(u"exit_mezcla_window")
        exit_mezcla_window.resize(382, 505)
        self.verticalLayout = QVBoxLayout(exit_mezcla_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(exit_mezcla_window)
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
        self.productos_para_mezcla = QComboBox(self.content_frame)
        self.productos_para_mezcla.setObjectName(u"productos_para_mezcla")
        self.productos_para_mezcla.setGeometry(QRect(40, 160, 191, 41))
        self.productos_para_mezcla.setStyleSheet(u"QComboBox {\n"
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
        self.label.setGeometry(QRect(90, 110, 101, 31))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"        color: #ffffff;            /* Color del texto */\n"
"        \n"
"        border: 2px solid #457B9D; /* Color del borde */\n"
"        border-radius: 5px;        /* Radio del borde (para bordes redondeados) */\n"
"        padding: 5px;              /* Espacio interior alrededor del texto */\n"
"        font-size: 14px;           /* Tama\u00f1o del texto */\n"
"    }")
        self.cantidad_exit_paramezcla = QDoubleSpinBox(self.content_frame)
        self.cantidad_exit_paramezcla.setObjectName(u"cantidad_exit_paramezcla")
        self.cantidad_exit_paramezcla.setGeometry(QRect(250, 160, 101, 41))
        self.cantidad_exit_paramezcla.setStyleSheet(u" QDoubleSpinBox {\n"
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
        self.label_2.setGeometry(QRect(250, 110, 101, 31))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"QLabel {\n"
"        color: #ffffff;            /* Color del texto */\n"
"        \n"
"        border: 2px solid #457B9D; /* Color del borde */\n"
"        border-radius: 5px;        /* Radio del borde (para bordes redondeados) */\n"
"        padding: 5px;              /* Espacio interior alrededor del texto */\n"
"        font-size: 14px;           /* Tama\u00f1o del texto */\n"
"    }")
        self.submit_exit_mezcla = QPushButton(self.content_frame)
        self.submit_exit_mezcla.setObjectName(u"submit_exit_mezcla")
        self.submit_exit_mezcla.setGeometry(QRect(130, 450, 131, 31))
        self.submit_exit_mezcla.setStyleSheet(u"QPushButton {\n"
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
        self.ingredientes_mezcla = QTableWidget(self.content_frame)
        if (self.ingredientes_mezcla.columnCount() < 2):
            self.ingredientes_mezcla.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.ingredientes_mezcla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ingredientes_mezcla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.ingredientes_mezcla.setObjectName(u"ingredientes_mezcla")
        self.ingredientes_mezcla.setGeometry(QRect(40, 230, 211, 192))
        self.ingredientes_mezcla.setStyleSheet(u"QTableWidget {\n"
"        background-color: #F1FAEE;\n"
"        color: #1D3557;\n"
"        border: 2px solid #457B9D;\n"
"        border-radius: 5px;\n"
"        font-size: 14px;\n"
"        gridline-color: #457B9D;\n"
"    }\n"
"    QTableWidget::item {\n"
"        border: 1px solid #457B9D;\n"
"    }\n"
"    QTableWidget::item:selected {\n"
"        background-color: #457B9D;\n"
"        color: #F1FAEE;\n"
"    }\n"
"    QHeaderView::section {\n"
"        background-color: #457B9D;\n"
"        color: #F1FAEE;\n"
"        padding: 5px;\n"
"        border: 2px solid #1D3557;\n"
"        border-radius: 5px;\n"
"        font-size: 14px;\n"
"    }")
        self.mezcla_combobox = QComboBox(self.content_frame)
        self.mezcla_combobox.setObjectName(u"mezcla_combobox")
        self.mezcla_combobox.setGeometry(QRect(40, 50, 311, 41))
        self.mezcla_combobox.setStyleSheet(u"QComboBox {\n"
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
        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 10, 81, 31))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"QLabel {\n"
"        color: #ffffff;            /* Color del texto */\n"
"        \n"
"        border: 2px solid #457B9D; /* Color del borde */\n"
"        border-radius: 5px;        /* Radio del borde (para bordes redondeados) */\n"
"        padding: 5px;              /* Espacio interior alrededor del texto */\n"
"        font-size: 14px;           /* Tama\u00f1o del texto */\n"
"    }")
        self.agregar_ingrediente = QPushButton(self.content_frame)
        self.agregar_ingrediente.setObjectName(u"agregar_ingrediente")
        self.agregar_ingrediente.setGeometry(QRect(260, 230, 91, 31))
        self.agregar_ingrediente.setStyleSheet(u"QPushButton {\n"
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


        self.retranslateUi(exit_mezcla_window)

        QMetaObject.connectSlotsByName(exit_mezcla_window)
    # setupUi

    def retranslateUi(self, exit_mezcla_window):
        exit_mezcla_window.setWindowTitle(QCoreApplication.translate("exit_mezcla_window", u"Form", None))
        self.label.setText(QCoreApplication.translate("exit_mezcla_window", u"INGREDIENTE", None))
        self.label_2.setText(QCoreApplication.translate("exit_mezcla_window", u"CANTIDAD", None))
        self.submit_exit_mezcla.setText(QCoreApplication.translate("exit_mezcla_window", u"Aplicar", None))
        ___qtablewidgetitem = self.ingredientes_mezcla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("exit_mezcla_window", u"Ingrediente", None));
        ___qtablewidgetitem1 = self.ingredientes_mezcla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("exit_mezcla_window", u"Cantidad", None));
        self.label_3.setText(QCoreApplication.translate("exit_mezcla_window", u"MEZCLA", None))
        self.agregar_ingrediente.setText(QCoreApplication.translate("exit_mezcla_window", u"Agregar", None))
    # retranslateUi

