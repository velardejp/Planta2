# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 507)
        self.action_nuevoproducto = QAction(MainWindow)
        self.action_nuevoproducto.setObjectName(u"action_nuevoproducto")
        self.action_catalago = QAction(MainWindow)
        self.action_catalago.setObjectName(u"action_catalago")
        self.action_entry = QAction(MainWindow)
        self.action_entry.setObjectName(u"action_entry")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_report_entradas = QAction(MainWindow)
        self.action_report_entradas.setObjectName(u"action_report_entradas")
        self.action_report_salidas = QAction(MainWindow)
        self.action_report_salidas.setObjectName(u"action_report_salidas")
        self.action_report_kardex = QAction(MainWindow)
        self.action_report_kardex.setObjectName(u"action_report_kardex")
        self.actionMezcla = QAction(MainWindow)
        self.actionMezcla.setObjectName(u"actionMezcla")
        self.actionMezcla_2 = QAction(MainWindow)
        self.actionMezcla_2.setObjectName(u"actionMezcla_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.centralwidget)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: #537188;")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.grafico_1 = QFrame(self.content_frame)
        self.grafico_1.setObjectName(u"grafico_1")
        self.grafico_1.setGeometry(QRect(350, 20, 461, 211))
        self.grafico_1.setFrameShape(QFrame.StyledPanel)
        self.grafico_1.setFrameShadow(QFrame.Raised)
        self.tabla_stock = QTableWidget(self.content_frame)
        if (self.tabla_stock.columnCount() < 2):
            self.tabla_stock.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_stock.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_stock.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabla_stock.setObjectName(u"tabla_stock")
        self.tabla_stock.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Oculta el índice de la tabla.
        self.tabla_stock.verticalHeader().setVisible(False)
        self.tabla_stock.setGeometry(QRect(25, 31, 311, 411))
        self.tabla_stock.setStyleSheet(u"QTableWidget {\n"
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
        self.mas_salidas = QLabel(self.content_frame)
        self.mas_salidas.setObjectName(u"mas_salidas")
        self.mas_salidas.setGeometry(QRect(350, 250, 111, 81))
        self.mas_salidas.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.mas_almacen = QLabel(self.content_frame)
        self.mas_almacen.setObjectName(u"mas_almacen")
        self.mas_almacen.setGeometry(QRect(500, 250, 111, 81))
        self.mas_almacen.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.mas_almacen_2 = QLabel(self.content_frame)
        self.mas_almacen_2.setObjectName(u"mas_almacen_2")
        self.mas_almacen_2.setGeometry(QRect(650, 250, 111, 81))
        self.mas_almacen_2.setStyleSheet(u"border-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self.background_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 835, 22))
        self.menuProductos = QMenu(self.menubar)
        self.menuProductos.setObjectName(u"menuProductos")
        self.menuEntradas = QMenu(self.menubar)
        self.menuEntradas.setObjectName(u"menuEntradas")
        self.menuSalidas = QMenu(self.menubar)
        self.menuSalidas.setObjectName(u"menuSalidas")
        self.menuReportes = QMenu(self.menubar)
        self.menuReportes.setObjectName(u"menuReportes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProductos.menuAction())
        self.menubar.addAction(self.menuEntradas.menuAction())
        self.menubar.addAction(self.menuSalidas.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menuProductos.addAction(self.action_nuevoproducto)
        self.menuProductos.addAction(self.action_catalago)
        self.menuProductos.addAction(self.actionMezcla)
        self.menuEntradas.addAction(self.action_entry)
        self.menuSalidas.addAction(self.action_exit)
        self.menuSalidas.addAction(self.actionMezcla_2)
        self.menuReportes.addAction(self.action_report_entradas)
        self.menuReportes.addAction(self.action_report_salidas)
        self.menuReportes.addAction(self.action_report_kardex)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Control de Inventario", None))
        self.action_nuevoproducto.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.action_catalago.setText(QCoreApplication.translate("MainWindow", u"Catalogo", None))
        self.action_entry.setText(QCoreApplication.translate("MainWindow", u"Nueva", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Nueva", None))
        self.action_report_entradas.setText(QCoreApplication.translate("MainWindow", u"Entradas", None))
        self.action_report_salidas.setText(QCoreApplication.translate("MainWindow", u"Salidas", None))
        self.action_report_kardex.setText(QCoreApplication.translate("MainWindow", u"Kardex", None))
        self.actionMezcla.setText(QCoreApplication.translate("MainWindow", u"Mezcla", None))
        self.actionMezcla_2.setText(QCoreApplication.translate("MainWindow", u"Mezcla", None))
        ___qtablewidgetitem = self.tabla_stock.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem1 = self.tabla_stock.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        self.mas_salidas.setText("")
        self.mas_almacen.setText("")
        self.mas_almacen_2.setText("")
        self.menuProductos.setTitle(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.menuEntradas.setTitle(QCoreApplication.translate("MainWindow", u"Entradas", None))
        self.menuSalidas.setTitle(QCoreApplication.translate("MainWindow", u"Salidas", None))
        self.menuReportes.setTitle(QCoreApplication.translate("MainWindow", u"Reportes", None))
    # retranslateUi

