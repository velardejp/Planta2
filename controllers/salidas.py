from PySide6.QtWidgets import QWidget
from views.Ui_ventana_salidas import Ui_exit_window
import datetime
from PySide6.QtCore import Signal
from database.db import get_all_products, add_exit

class AddExitForm(QWidget):
    exit_submitted = Signal()
    def __init__(self, parent=None):
        super(AddExitForm, self).__init__(parent)
        self.ui = Ui_exit_window()
        self.ui.setupUi(self)
        
        self.ui.productos_exit.addItems([product[0] for product in get_all_products()])
        
        self.ui.submit_exit_button.clicked.connect(self.submit_exit)
        
        
    def submit_exit(self):
        product_name = self.ui.productos_exit.currentText()
        quantity_out=self.ui.cantidad_exit_spin.value()
        
        add_exit(product_name, quantity_out)
        self.exit_submitted.emit()
    
    def load_product_data(self):
        self.ui.productos_exit.clear()
        self.ui.productos_exit.addItems([product[0] for product in get_all_products()])