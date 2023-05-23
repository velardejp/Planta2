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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

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
        self.tabla_entradas_kardex.setGeometry(QRect(20, 60, 711, 261))
        self.tabla_entradas_kardex.setStyleSheet(u"QTableWidget {\n"
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
        self.import_excel_kardex = QPushButton(self.content_frame)
        self.import_excel_kardex.setObjectName(u"import_excel_kardex")
        self.import_excel_kardex.setGeometry(QRect(610, 600, 101, 41))
        self.import_excel_kardex.setStyleSheet(u"QPushButton {\n"
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
        self.productos_kardex = QComboBox(self.content_frame)
        self.productos_kardex.setObjectName(u"productos_kardex")
        self.productos_kardex.setGeometry(QRect(80, 10, 211, 31))
        self.productos_kardex.setStyleSheet(u"QComboBox {\n"
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
        self.tabla_salidas_kardex = QTableWidget(self.content_frame)
        if (self.tabla_salidas_kardex.columnCount() < 4):
            self.tabla_salidas_kardex.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_salidas_kardex.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tabla_salidas_kardex.setObjectName(u"tabla_salidas_kardex")
        self.tabla_salidas_kardex.setGeometry(QRect(20, 330, 711, 261))
        self.tabla_salidas_kardex.setStyleSheet(u"QTableWidget {\n"
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

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.backgroundcolor_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(reporte_kardex)

        QMetaObject.connectSlotsByName(reporte_kardex)
    # setupUi

    def retranslateUi(self, reporte_kardex):
        reporte_kardex.setWindowTitle(QCoreApplication.translate("reporte_kardex", u"Form", None))
        ___qtablewidgetitem = self.tabla_entradas_kardex.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("reporte_kardex", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_entradas_kardex.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("reporte_kardex", u"Producto", None));
        ___qtablewidgetitem2 = self.tabla_entradas_kardex.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("reporte_kardex", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tabla_entradas_kardex.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("reporte_kardex", u"Fecha", None));
        self.import_excel_kardex.setText(QCoreApplication.translate("reporte_kardex", u"excel", None))
        ___qtablewidgetitem4 = self.tabla_salidas_kardex.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("reporte_kardex", u"ID", None));
        ___qtablewidgetitem5 = self.tabla_salidas_kardex.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("reporte_kardex", u"Producto", None));
        ___qtablewidgetitem6 = self.tabla_salidas_kardex.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("reporte_kardex", u"Cantidad", None));
        ___qtablewidgetitem7 = self.tabla_salidas_kardex.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("reporte_kardex", u"Fecha", None));
    # retranslateUi

