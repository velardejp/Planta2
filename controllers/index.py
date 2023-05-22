from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from views.Ui_MainWindow import Ui_MainWindow
from controllers.alta_prod import AddWindowForm
from controllers.entradas import AddEntryForm
from controllers.salidas import AddExitForm
from controllers.salida_mezcla import ExitMezclaForm
from controllers.nueva_mezcla import AddMezclaForm
from controllers.reporte_salidas import ExitReportForm
import sqlite3

class MainWindowForm (QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventana_productos = AddWindowForm()
        self.ventana_entradas=AddEntryForm()
        self.ventana_salidas=AddExitForm()
        self.ventana_mezcla=ExitMezclaForm()
        self.ventana_nueva_mezcla=AddMezclaForm()
        self.ventana_reporte_salidas=ExitReportForm()
        # Conectamos la función open_addproduct_window a la acción action_nuevoproducto
        self.ui.action_nuevoproducto.triggered.connect(self.open_addproduct_window)
        self.ui.action_entry.triggered.connect(self.open_entrys_window)
        self.ui.action_exit.triggered.connect(self.open_exits_window)
        self.ui.action_exit_mezcla.triggered.connect(self.open_exits_mezcla_window)
        self.ui.action_nuevomezcla.triggered.connect(self.open_new_mezcla_window)
        self.ui.action_report_salidas.triggered.connect(self.open_report_exits_window)
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
    
    def load_product_stock(self):
        
        self.ventana_entradas.load_product_data()
        self.ventana_salidas.load_product_data()
        
    def load_mezclas(self):
        self.ventana_mezcla.load_mezcla_data()


