# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(885, 499)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_frame = QFrame(MainWindow)
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
        self.productos_button = QPushButton(self.content_frame)
        self.productos_button.setObjectName(u"productos_button")
        self.productos_button.setGeometry(QRect(20, 120, 101, 24))
        self.add_entrada_button = QPushButton(self.content_frame)
        self.add_entrada_button.setObjectName(u"add_entrada_button")
        self.add_entrada_button.setGeometry(QRect(20, 170, 101, 24))
        self.add_salida_button = QPushButton(self.content_frame)
        self.add_salida_button.setObjectName(u"add_salida_button")
        self.add_salida_button.setGeometry(QRect(20, 220, 111, 24))
        self.add_product_button = QPushButton(self.content_frame)
        self.add_product_button.setObjectName(u"add_product_button")
        self.add_product_button.setGeometry(QRect(10, 78, 111, 24))
        self.stock_deprods = QTableWidget(self.content_frame)
        if (self.stock_deprods.columnCount() < 2):
            self.stock_deprods.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.stock_deprods.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.stock_deprods.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.stock_deprods.setObjectName(u"stock_deprods")
        self.stock_deprods.setGeometry(QRect(300, 70, 431, 231))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_deprods.sizePolicy().hasHeightForWidth())
        self.stock_deprods.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.productos_button.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.add_entrada_button.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.add_salida_button.setText(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.add_product_button.setText(QCoreApplication.translate("MainWindow", u"Agregar Producto", None))
        ___qtablewidgetitem = self.stock_deprods.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Producto Name", None));
        ___qtablewidgetitem1 = self.stock_deprods.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
    # retranslateUi

