from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from views.Ui_nuevo_producto_ventana import Ui_ventana_nuevo_producto
from database.db import add_product_data, make_id_prod



class AddWindowForm(QWidget):
    product_submitted = Signal()
    def __init__(self, parent=None):
        super(AddWindowForm, self).__init__(parent)
        self.ui = Ui_ventana_nuevo_producto()
        self.ui.setupUi(self)
        
        self.ui.submit_nuevoproducto_button.clicked.connect(self.submit_product)
        
    def submit_product(self):
        id = make_id_prod()
        name = self.ui.nombre_nuevo_prod.text()
        if self.ui.litros_radiobutton.isChecked():
            unit_of_measure=self.ui.litros_radiobutton.text()
        elif self.ui.kilos_radiobutton.isChecked():
            unit_of_measure=self.ui.kilos_radiobutton.text()

        add_product_data(id,name,unit_of_measure)
        self.ui.nombre_nuevo_prod.clear()
        self.product_submitted.emit()

        
    
   

    