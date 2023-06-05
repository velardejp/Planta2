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
        exit_mezcla_window.resize(366, 545)
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
        self.productos_para_mezcla = QComboBox(self.content_frame)
        self.productos_para_mezcla.setObjectName(u"productos_para_mezcla")
        self.productos_para_mezcla.setGeometry(QRect(10, 140, 211, 51))
        self.productos_para_mezcla.setStyleSheet(u"QComboBox {\n"
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
        self.productos_para_mezcla.setEditable(True)
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 100, 211, 43))
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
        self.cantidad_exit_paramezcla = QDoubleSpinBox(self.content_frame)
        self.cantidad_exit_paramezcla.setObjectName(u"cantidad_exit_paramezcla")
        self.cantidad_exit_paramezcla.setGeometry(QRect(220, 140, 131, 51))
        self.cantidad_exit_paramezcla.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.cantidad_exit_paramezcla.setMaximum(9999.989999999999782)
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 100, 131, 43))
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
        self.submit_exit_mezcla = QPushButton(self.content_frame)
        self.submit_exit_mezcla.setObjectName(u"submit_exit_mezcla")
        self.submit_exit_mezcla.setGeometry(QRect(220, 470, 131, 51))
        self.submit_exit_mezcla.setStyleSheet(u"QPushButton {\n"
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
        self.ingredientes_mezcla = QTableWidget(self.content_frame)
        if (self.ingredientes_mezcla.columnCount() < 3):
            self.ingredientes_mezcla.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.ingredientes_mezcla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ingredientes_mezcla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ingredientes_mezcla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.ingredientes_mezcla.setObjectName(u"ingredientes_mezcla")
        self.ingredientes_mezcla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Oculta el índice de la tabla.
        self.ingredientes_mezcla.verticalHeader().setVisible(False)
        self.ingredientes_mezcla.setGeometry(QRect(10, 230, 341, 192))
        self.ingredientes_mezcla.setStyleSheet(u"QTableWidget {\n"
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
        self.mezcla_combobox = QComboBox(self.content_frame)
        self.mezcla_combobox.setObjectName(u"mezcla_combobox")
        self.mezcla_combobox.setGeometry(QRect(10, 50, 211, 51))
        self.mezcla_combobox.setStyleSheet(u"QComboBox {\n"
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
        self.mezcla_combobox.setEditable(True)
        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 211, 43))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border: 2px solid #537188;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    background-color: #CBB279;\n"
"}")
        self.agregar_ingrediente = QPushButton(self.content_frame)
        self.agregar_ingrediente.setObjectName(u"agregar_ingrediente")
        self.agregar_ingrediente.setGeometry(QRect(10, 190, 341, 41))
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
        self.label_4 = QLabel(self.content_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 10, 131, 43))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border: 2px solid #537188;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    background-color: #CBB279;\n"
"}")
        self.cantidad_mezcla = QDoubleSpinBox(self.content_frame)
        self.cantidad_mezcla.setObjectName(u"cantidad_mezcla")
        self.cantidad_mezcla.setGeometry(QRect(220, 50, 131, 51))
        self.cantidad_mezcla.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.cantidad_mezcla.setMaximum(9999.989999999999782)
        self.cantidad_sacos = QDoubleSpinBox(self.content_frame)
        self.cantidad_sacos.setObjectName(u"cantidad_sacos")
        self.cantidad_sacos.setGeometry(QRect(120, 470, 101, 51))
        self.cantidad_sacos.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.cantidad_sacos.setMaximum(9999.989999999999782)
        self.label_5 = QLabel(self.content_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 470, 101, 43))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border: 2px solid #537188;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    background-color: #CBB279;\n"
"}")
        self.porcentaje = QLabel(self.content_frame)
        self.porcentaje.setObjectName(u"porcentaje")
        self.porcentaje.setGeometry(QRect(20, 420, 321, 43))
        self.porcentaje.setLayoutDirection(Qt.LeftToRight)
        self.porcentaje.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border: 2px solid #537188;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    background-color: #CBB279;\n"
"}")

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(exit_mezcla_window)

        QMetaObject.connectSlotsByName(exit_mezcla_window)
    # setupUi

    def retranslateUi(self, exit_mezcla_window):
        exit_mezcla_window.setWindowTitle(QCoreApplication.translate("exit_mezcla_window", u"Salida mezcla", None))
        self.label.setText(QCoreApplication.translate("exit_mezcla_window", u"INGREDIENTE", None))
        self.label_2.setText(QCoreApplication.translate("exit_mezcla_window", u"CANTIDAD", None))
        self.submit_exit_mezcla.setText(QCoreApplication.translate("exit_mezcla_window", u"Aplicar", None))
        ___qtablewidgetitem = self.ingredientes_mezcla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("exit_mezcla_window", u"Ingrediente", None));
        ___qtablewidgetitem1 = self.ingredientes_mezcla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("exit_mezcla_window", u"Cantidad", None));
        ___qtablewidgetitem2 = self.ingredientes_mezcla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("exit_mezcla_window", u"%", None));
        self.mezcla_combobox.setPlaceholderText(QCoreApplication.translate("exit_mezcla_window", u"mezclas", None))
        self.label_3.setText(QCoreApplication.translate("exit_mezcla_window", u"MEZCLA", None))
        self.agregar_ingrediente.setText(QCoreApplication.translate("exit_mezcla_window", u"Agregar", None))
        self.label_4.setText(QCoreApplication.translate("exit_mezcla_window", u"CANTIDAD", None))
        self.label_5.setText(QCoreApplication.translate("exit_mezcla_window", u"SACOS", None))
        self.porcentaje.setText("")
    # retranslateUi

