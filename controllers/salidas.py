from PySide6.QtWidgets import QWidget, QTableWidgetItem
from views.Ui_ventana_salidas import Ui_exit_window
import datetime
from PySide6.QtCore import Signal
from database.db import get_all_products, add_exit, make_id_exit

class AddExitForm(QWidget):
    exit_submitted = Signal()
    def __init__(self, add_product_form,parent=None):
        super(AddExitForm, self).__init__(parent)
        self.ui = Ui_exit_window()
        self.ui.setupUi(self)
        
        self.ui.productos_exit.addItems([product[0] for product in get_all_products()])
        self.ui.agrega_ingrediente_salida.clicked.connect(self.agregar_ingrediente)
        self.ui.submit_exit_button.clicked.connect(self.submit_exit)
        add_product_form.product_submitted.connect(self.load_product_data)
        
    def agregar_ingrediente(self):
        ingrediente = self.ui.productos_exit.currentText()
        cantidad = self.ui.cantidad_exit_spin.value()
        # Obtiene el número actual de filas
        num_row = self.ui.tabla_productos_salida.rowCount()
        # Inserta una nueva fila al final de la tabla
        self.ui.tabla_productos_salida.insertRow(num_row)
        # Crea nuevos ítems para la fila
        item_ingrediente = QTableWidgetItem(ingrediente)
        item_cantidad = QTableWidgetItem(str(cantidad))
        # Añade los ítems a la fila
        self.ui.tabla_productos_salida.setItem(num_row, 0, item_ingrediente)
        self.ui.tabla_productos_salida.setItem(num_row, 1, item_cantidad)    
    
    def submit_exit(self):
        num_rows = self.ui.tabla_productos_salida.rowCount()
        id=make_id_exit()
        for row in range(num_rows):
            ingrediente = self.ui.tabla_productos_salida.item(row, 0).text()
            cantidad = float(self.ui.tabla_productos_salida.item(row, 1).text())  # convertir la cantidad a un número
            mezcla="NO"
            add_exit(id, ingrediente,cantidad,mezcla)
        self.ui.tabla_productos_salida.clearContents()  # Esto eliminará todos los elementos del QTableWidget
        self.ui.tabla_productos_salida.setRowCount(0)  # Esto eliminará todas las filas
        self.exit_submitted.emit()
    
    def load_product_data(self):
        self.ui.productos_exit.clear()
        self.ui.productos_exit.addItems([product[0] for product in get_all_products()])