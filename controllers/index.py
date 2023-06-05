from PySide6.QtWidgets import QMainWindow, QTableWidgetItem,QVBoxLayout 
from PySide6 import QtCharts
from views.Ui_MainWindow import Ui_MainWindow
from controllers.alta_prod import AddWindowForm
from controllers.entradas import AddEntryForm
from controllers.salidas import AddExitForm
from controllers.salida_mezcla import ExitMezclaForm
from controllers.nueva_mezcla import AddMezclaForm
from controllers.reporte_salidas import ExitReportForm
from controllers.reporte_entradas import EntryReportForm
from controllers.reporte_kardex import KardexReportForm
from controllers.catalogo import CatalogoForm
from database.db import get_all_products, mas_salidas
from controllers.graficos import InventoryGraph
import sqlite3
class MainWindowForm (QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Declaracion de ventanas en MainWindow
        self.ventana_productos = AddWindowForm()
        self.ventana_entradas=AddEntryForm(self.ventana_productos)
        self.ventana_salidas=AddExitForm(self.ventana_productos)
        self.ventana_nueva_mezcla=AddMezclaForm(self.ventana_productos)
        self.ventana_mezcla=ExitMezclaForm(self.ventana_productos,self.ventana_nueva_mezcla)
        self.ventana_reporte_salidas=ExitReportForm(self.ventana_salidas,self.ventana_mezcla)
        self.ventana_reporte_entradas=EntryReportForm(self.ventana_entradas)
        self.ventana_kardex=KardexReportForm(self.ventana_entradas,self.ventana_salidas,self.ventana_mezcla)
        self.ventana_catalogo=CatalogoForm(self.ventana_productos,self.ventana_nueva_mezcla)
        # Conexiones para abrir ventanas desde el meni
        self.ui.action_nuevoproducto.triggered.connect(self.open_addproduct_window)
        self.ui.action_entry.triggered.connect(self.open_entrys_window)
        self.ui.action_exit.triggered.connect(self.open_exits_window)
        self.ui.actionMezcla_2.triggered.connect(self.open_exits_mezcla_window)
        self.ui.actionMezcla.triggered.connect(self.open_new_mezcla_window)
        self.ui.action_report_salidas.triggered.connect(self.open_report_exits_window)
        self.ui.action_report_entradas.triggered.connect(self.open_report_entrys_window)
        self.ui.action_report_kardex.triggered.connect(self.open_report_kardex_window)
        self.ui.action_catalago.triggered.connect(self.open_catalogo_window)
        #Señales
        self.ventana_nueva_mezcla.mezcla_submitted.connect(self.load_mezclas)
        self.ventana_mezcla.exit_mezcla_submitted.connect(self.load_product_stock)
        self.ventana_nueva_mezcla.mezcla_submitted.connect(self.ventana_mezcla.refresh)
        #Graficos en pantalla de inicio
        self.get_productos()
        moda_salidas=str( mas_salidas())
        self.ui.mas_salidas.setText(moda_salidas)
        self.inventario_graph = InventoryGraph(self.ui.grafico_1)
        layout = QVBoxLayout()
        layout.addWidget(self.inventario_graph)
        self.ui.grafico_1.setLayout(layout)
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        c.execute("SELECT product_id, SUM(quantity) FROM exits_mezcla GROUP BY product_id")
        data_tuples = c.fetchall()
        conn.commit()
        conn.close()
        data = data_tuples 
        self.inventario_graph.plot(data)
        
    #Funciones para mostrar las otras ventanas
    def open_addproduct_window(self):
        self.ventana_productos.show()

    def open_entrys_window(self):
        self.ventana_entradas.show()

    def open_exits_window(self):
        self.ventana_salidas.show()

    def open_exits_mezcla_window(self):
        self.ventana_mezcla.show()

    def open_new_mezcla_window(self):
        self.ventana_nueva_mezcla.show()

    def open_report_exits_window(self):
        self.ventana_reporte_salidas.show()

    def open_report_entrys_window(self):
        self.ventana_reporte_entradas.show()

    def open_report_kardex_window(self):
        self.ventana_kardex.show()

    def open_catalogo_window(self):
        self.ventana_catalogo.show()
#Funciones para cargar los datos de las señales
    def load_product_stock(self):
        self.ventana_entradas.load_product_data()
        self.ventana_salidas.load_product_data()
    def load_mezclas(self):
        self.ventana_mezcla.load_mezcla_data()

#Funcion para cargar los productos en la tabla de inicio
    def get_productos(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        c.execute("SELECT name, stock FROM products WHERE stock > 0 ORDER BY stock DESC")
        products = c.fetchall()
        self.ui.tabla_stock.setRowCount(0)
        for row_number, row_data in enumerate(products):
            self.ui.tabla_stock.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tabla_stock.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    

    