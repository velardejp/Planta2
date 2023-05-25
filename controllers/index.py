from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

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
from database.db import get_all_products
import sqlite3
class MainWindowForm (QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventana_productos = AddWindowForm()
        self.ventana_entradas=AddEntryForm(self.ventana_productos)
        self.ventana_salidas=AddExitForm(self.ventana_productos)
        self.ventana_nueva_mezcla=AddMezclaForm(self.ventana_productos)
        self.ventana_mezcla=ExitMezclaForm(self.ventana_productos,self.ventana_nueva_mezcla)
        self.ventana_reporte_salidas=ExitReportForm(self.ventana_salidas,self.ventana_mezcla)
        self.ventana_reporte_entradas=EntryReportForm(self.ventana_entradas)
        self.ventana_kardex=KardexReportForm(self.ventana_entradas,self.ventana_salidas,self.ventana_mezcla)
        self.ventana_catalogo=CatalogoForm(self.ventana_productos,self.ventana_nueva_mezcla)
        # Conectamos la función open_addproduct_window a la acción action_nuevoproducto
        self.ui.action_nuevoproducto.triggered.connect(self.open_addproduct_window)
        self.ui.action_entry.triggered.connect(self.open_entrys_window)
        self.ui.action_exit.triggered.connect(self.open_exits_window)
        self.ui.actionMezcla_2.triggered.connect(self.open_exits_mezcla_window)
        self.ui.actionMezcla.triggered.connect(self.open_new_mezcla_window)
        self.ui.action_report_salidas.triggered.connect(self.open_report_exits_window)
        self.ui.action_report_entradas.triggered.connect(self.open_report_entrys_window)
        self.ui.action_report_kardex.triggered.connect(self.open_report_kardex_window)
        self.ui.action_catalago.triggered.connect(self.open_catalogo_window)
        self.ventana_nueva_mezcla.mezcla_submitted.connect(self.load_mezclas)
        self.ventana_mezcla.exit_mezcla_submitted.connect(self.load_product_stock)
       
        

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
    def load_product_stock(self):
        
        self.ventana_entradas.load_product_data()
        self.ventana_salidas.load_product_data()
        
    def load_mezclas(self):
        self.ventana_mezcla.load_mezcla_data()

    