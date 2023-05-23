from PySide6.QtWidgets import QWidget
from views.Ui_nueva_entrada_ventana import Ui_nueva_entrada
from PySide6.QtCore import Signal
import datetime
from database.db import get_all_products, add_entry

class AddEntryForm(QWidget):
    entry_submitted = Signal()
    def __init__(self, add_product_form,parent=None):
        super(AddEntryForm, self).__init__(parent)
        self.ui = Ui_nueva_entrada()
        self.ui.setupUi(self)
        
        self.ui.productos_entrada.addItems([product[0] for product in get_all_products()])
        
        self.ui.submit_entrada_button.clicked.connect(self.submit_entry)
        add_product_form.product_submitted.connect(self.load_product_data)
        
    def submit_entry(self):
        product_name = self.ui.productos_entrada.currentText()
        quantity=self.ui.cantidad_entrada.text()
        
        add_entry(product_name, quantity)
        self.entry_submitted.emit()
    
    def load_product_data(self):
        self.ui.productos_entrada.clear()
        self.ui.productos_entrada.addItems([product[0] for product in get_all_products()])
        

    
