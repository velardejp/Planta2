from PySide6.QtWidgets import QWidget, QTableWidgetItem
from views.Ui_index import Ui_MainWindow
from controllers.alta_prod import AddWindowForm
from controllers.entradas import AddEntryForm
from controllers.salidas import AddExitForm
import sqlite3

class MainWindowForm(QWidget):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_product_button.clicked.connect(self.open_addproduct_window)
        self.ui.add_entrada_button.clicked.connect(self.open_entrys_window)
        self.ui.add_salida_button.clicked.connect(self.open_exits_window)
        
        self.ventana_productos = AddWindowForm()
        self.ventana_entradas=AddEntryForm()
        self.ventana_salidas=AddExitForm()
        self.load_product_stock()
        self.ventana_productos.product_submitted.connect(self.load_product_stock)
        self.ventana_entradas.entry_submitted.connect(self.load_product_stock)
        self.ventana_salidas.exit_submitted.connect(self.load_product_stock)
        
    
    def open_addproduct_window(self):
        self.ventana_productos.show()
    
    def open_entrys_window(self):
        self.ventana_entradas.show()

    def open_exits_window(self):
        self.ventana_salidas.show()
    
   
    def load_product_stock(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        result = c.execute("SELECT name, stock FROM products")
        self.ui.stock_deprods.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.stock_deprods.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.stock_deprods.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        self.ventana_entradas.load_product_data()
        self.ventana_salidas.load_product_data()
