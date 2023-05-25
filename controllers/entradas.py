from PySide6.QtWidgets import QWidget, QTableWidgetItem
from views.Ui_nueva_entrada_ventana import Ui_nueva_entrada
from PySide6.QtCore import Signal
import datetime
from database.db import get_all_products, add_entry, make_id_entry

class AddEntryForm(QWidget):
    entry_submitted = Signal()
    def __init__(self, add_product_form,parent=None):
        super(AddEntryForm, self).__init__(parent)
        self.ui = Ui_nueva_entrada()
        self.ui.setupUi(self)
        
        self.ui.productos_entrada.addItems([product[0] for product in get_all_products()])
        
        self.ui.submit_entrada_button.clicked.connect(self.submit_entry)
        self.ui.agregar_producto.clicked.connect(self.agregar_ingrediente)
        add_product_form.product_submitted.connect(self.load_product_data)
    
    def agregar_ingrediente(self):
        ingrediente = self.ui.productos_entrada.currentText()
        cantidad = self.ui.cantidad_entrada.value()
        # Obtiene el número actual de filas
        num_row = self.ui.tabla_new_entrada.rowCount()
        # Inserta una nueva fila al final de la tabla
        self.ui.tabla_new_entrada.insertRow(num_row)
        # Crea nuevos ítems para la fila
        item_ingrediente = QTableWidgetItem(ingrediente)
        item_cantidad = QTableWidgetItem(str(cantidad))
        # Añade los ítems a la fila
        self.ui.tabla_new_entrada.setItem(num_row, 0, item_ingrediente)
        self.ui.tabla_new_entrada.setItem(num_row, 1, item_cantidad)
        
    def submit_entry(self):
        num_rows = self.ui.tabla_new_entrada.rowCount()
        id=make_id_entry()
        for row in range(num_rows):
            ingrediente = self.ui.tabla_new_entrada.item(row, 0).text()
            cantidad = float(self.ui.tabla_new_entrada.item(row, 1).text())  # convertir la cantidad a un número
            add_entry(id, ingrediente,cantidad)
          # Esto eliminará todos los elementos del QTableWidget
        self.ui.tabla_new_entrada.clearContents()
        self.ui.tabla_new_entrada.setRowCount(0)
          # Esto eliminará todas las filas
        self.entry_submitted.emit()

    
    def load_product_data(self):
        self.ui.productos_entrada.clear()
        self.ui.productos_entrada.addItems([product[0] for product in get_all_products()])
        

    
