from PySide6.QtWidgets import QWidget
from views.Ui_entradas import Ui_Entradas
import datetime
from database.db import get_all_products, add_entry

class AddEntryForm(QWidget):
    def __init__(self, parent=None):
        super(AddEntryForm, self).__init__(parent)
        self.ui = Ui_Entradas()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems([product[0] for product in get_all_products()])
        
        self.ui.submit_entrada.clicked.connect(self.submit_entry)

    def submit_entry(self):
        product_name = self.ui.comboBox.currentText()
        quantity=self.ui.cantidad_entrada.text()
        
        add_entry(product_name, quantity)



