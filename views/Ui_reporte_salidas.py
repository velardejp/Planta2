# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reporte_salidas.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_reporte_salidas(object):
    def setupUi(self, reporte_salidas):
        if not reporte_salidas.objectName():
            reporte_salidas.setObjectName(u"reporte_salidas")
        reporte_salidas.resize(753, 385)
        self.verticalLayout = QVBoxLayout(reporte_salidas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(reporte_salidas)
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
        self.tabla_salidas = QTableWidget(self.content_frame)
        if (self.tabla_salidas.columnCount() < 5):
            self.tabla_salidas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_salidas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_salidas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_salidas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_salidas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_salidas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_salidas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Oculta el índice de la tabla.
        self.tabla_salidas.verticalHeader().setVisible(False)
        self.tabla_salidas.setObjectName(u"tabla_salidas")
        self.tabla_salidas.setGeometry(QRect(20, 60, 711, 261))
        self.tabla_salidas.setStyleSheet(u"QTableWidget {\n"
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
        self.import_excel_salidas = QPushButton(self.content_frame)
        self.import_excel_salidas.setObjectName(u"import_excel_salidas")
        self.import_excel_salidas.setGeometry(QRect(584, 323, 131, 51))
        self.import_excel_salidas.setStyleSheet(u"QPushButton {\n"
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
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 15, 711, 51))
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

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(reporte_salidas)

        QMetaObject.connectSlotsByName(reporte_salidas)
    # setupUi

    def retranslateUi(self, reporte_salidas):
        reporte_salidas.setWindowTitle(QCoreApplication.translate("reporte_salidas", u"Reporte salidas", None))
        ___qtablewidgetitem = self.tabla_salidas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("reporte_salidas", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_salidas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("reporte_salidas", u"Producto", None));
        ___qtablewidgetitem2 = self.tabla_salidas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("reporte_salidas", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tabla_salidas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("reporte_salidas", u"Fecha", None));
        ___qtablewidgetitem4 = self.tabla_salidas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("reporte_salidas", u"Mezcla", None));
        self.import_excel_salidas.setText(QCoreApplication.translate("reporte_salidas", u"Excel", None))
        self.label.setText(QCoreApplication.translate("reporte_salidas", u"SALIDAS", None))
    # retranslateUi

