# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reporte_kardex.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_reporte_kardex(object):
    def setupUi(self, reporte_kardex):
        if not reporte_kardex.objectName():
            reporte_kardex.setObjectName(u"reporte_kardex")
        reporte_kardex.resize(753, 669)
        self.verticalLayout = QVBoxLayout(reporte_kardex)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(reporte_kardex)
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
        self.tabla_entradas_kardex = QTableWidget(self.content_frame)
        if (self.tabla_entradas_kardex.columnCount() < 4):
            self.tabla_entradas_kardex.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_entradas_kardex.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_entradas_kardex.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_entradas_kardex.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_entradas_kardex.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabla_entradas_kardex.setObjectName(u"tabla_entradas_kardex")
        self.tabla_entradas_kardex.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Oculta el índice de la tabla.
        self.tabla_entradas_kardex.verticalHeader().setVisible(False)
        self.tabla_entradas_kardex.setGeometry(QRect(20, 100, 711, 261))
        self.tabla_entradas_kardex.setStyleSheet(u"QTableWidget {\n"
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
        self.import_excel_kardex = QPushButton(self.content_frame)
        self.import_excel_kardex.setObjectName(u"import_excel_kardex")
        self.import_excel_kardex.setGeometry(QRect(540, 10, 131, 51))
        self.import_excel_kardex.setStyleSheet(u"QPushButton {\n"
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
        self.productos_kardex = QComboBox(self.content_frame)
        self.productos_kardex.setObjectName(u"productos_kardex")
        self.productos_kardex.setGeometry(QRect(240, 10, 221, 51))
        self.productos_kardex.setStyleSheet(u"QComboBox {\n"
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
        self.tabla_salidas_kardex = QTableWidget(self.content_frame)
        if (self.tabla_salidas_kardex.columnCount() < 5):
            self.tabla_salidas_kardex.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tabla_salidas_kardex.setObjectName(u"tabla_salidas_kardex")
        self.tabla_salidas_kardex.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Oculta el índice de la tabla.
        self.tabla_salidas_kardex.verticalHeader().setVisible(False)
        self.tabla_salidas_kardex.setGeometry(QRect(20, 400, 711, 261))
        self.tabla_salidas_kardex.setStyleSheet(u"QTableWidget {\n"
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
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 355, 711, 51))
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
        self.label_2.setGeometry(QRect(20, 55, 711, 51))
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
        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 221, 51))
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

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(reporte_kardex)

        QMetaObject.connectSlotsByName(reporte_kardex)
    # setupUi

    def retranslateUi(self, reporte_kardex):
        reporte_kardex.setWindowTitle(QCoreApplication.translate("reporte_kardex", u"Reporte kardex", None))
        ___qtablewidgetitem = self.tabla_entradas_kardex.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("reporte_kardex", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_entradas_kardex.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("reporte_kardex", u"Producto", None));
        ___qtablewidgetitem2 = self.tabla_entradas_kardex.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("reporte_kardex", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tabla_entradas_kardex.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("reporte_kardex", u"Fecha", None));
        self.import_excel_kardex.setText(QCoreApplication.translate("reporte_kardex", u"Excel", None))
        ___qtablewidgetitem4 = self.tabla_salidas_kardex.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("reporte_kardex", u"ID", None));
        ___qtablewidgetitem5 = self.tabla_salidas_kardex.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("reporte_kardex", u"Producto", None));
        ___qtablewidgetitem6 = self.tabla_salidas_kardex.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("reporte_kardex", u"Cantidad", None));
        ___qtablewidgetitem7 = self.tabla_salidas_kardex.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("reporte_kardex", u"Fecha", None));
        ___qtablewidgetitem8 = self.tabla_salidas_kardex.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("reporte_kardex", u"Mezcla", None));
        self.label.setText(QCoreApplication.translate("reporte_kardex", u"SALIDAS", None))
        self.label_2.setText(QCoreApplication.translate("reporte_kardex", u"ENTRADAS", None))
        self.label_3.setText(QCoreApplication.translate("reporte_kardex", u"PRODUCTO", None))
    # retranslateUi

