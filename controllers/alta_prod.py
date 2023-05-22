from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from views.Ui_add_producto import Ui_AddWindowForm
from database.db import add_product_data



class AddWindowForm(QWidget):
    product_submitted = Signal()
    def __init__(self, parent=None):
        super(AddWindowForm, self).__init__(parent)
        self.ui = Ui_AddWindowForm()
        self.ui.setupUi(self)
        
        self.ui.submit_product_button.clicked.connect(self.submit_product)
        
    def submit_product(self):
        name = self.ui.product_name.text()
        if self.ui.litros_button.isChecked():
            unit_of_measure=self.ui.litros_button.text()
        elif self.ui.kilos_button.isChecked():
            unit_of_measure=self.ui.kilos_button.text()

        add_product_data(name,unit_of_measure)
        self.ui.product_name.clear()
        self.ui.unidad_medida.clear()

        self.product_submitted.emit()

        
    
   

    