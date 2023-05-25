from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Signal

from views.Ui_nueva_mezcla import Ui_nueva_mezcla_window
from database.db import make_mezcla_prod, add_mezcla_data, get_all_products, add_mezcla_ingredient

class AddMezclaForm(QWidget):
    mezcla_submitted = Signal()
    def __init__(self, add_product,parent=None):
        super(AddMezclaForm, self).__init__(parent)
        self.ui = Ui_nueva_mezcla_window()
        self.ui.setupUi(self)
        products = get_all_products()
        for product in products:
            product_name = product[0]
            product_id = product[1]
            self.ui.ingrediente_nueva_mezcla.addItem(product_name, product_id)
        self.ui.submit_mezcla_button.clicked.connect(self.submit_mezcla)
        self.ui.agregar_ingrediente.clicked.connect(self.agregar_ingredientes)
        add_product.product_submitted.connect(self.load_product_data)
    
    def agregar_ingredientes(self):
        ingrediente = self.ui.ingrediente_nueva_mezcla.currentText()
        id=self.ui.ingrediente_nueva_mezcla.currentData()
        cantidad = self.ui.cantidad_ingrediente.value()
        # Obtiene el número actual de filas
        num_row = self.ui.tabla_ingredientes.rowCount()
        # Inserta una nueva fila al final de la tabla
        self.ui.tabla_ingredientes.insertRow(num_row)
        # Crea nuevos ítems para la fila
        item_id=QTableWidgetItem(id)
        item_ingrediente = QTableWidgetItem(ingrediente)
        item_cantidad = QTableWidgetItem(str(cantidad))
        # Añade los ítems a la fila
        self.ui.tabla_ingredientes.setItem(num_row, 0, item_id)
        self.ui.tabla_ingredientes.setItem(num_row, 1, item_ingrediente)
        self.ui.tabla_ingredientes.setItem(num_row, 2, item_cantidad)
    def submit_mezcla(self):
        num_rows = self.ui.tabla_ingredientes.rowCount()
        name=self.ui.nombre_mezcla.text()
        unit="Kilogramos"
        id=make_mezcla_prod()
        add_mezcla_data(id, name, unit)
        for row in range(num_rows):
            ingrediente = self.ui.tabla_ingredientes.item(row, 0).text()
            cantidad = float(self.ui.tabla_ingredientes.item(row, 2).text())  # convertir la cantidad a un número
            add_mezcla_ingredient(id, ingrediente,cantidad)
          # Esto eliminará todos los elementos del QTableWidget
        self.ui.tabla_ingredientes.clearContents()
        self.ui.tabla_ingredientes.setRowCount(0)

        self.ui.nombre_mezcla.clear()
        self.mezcla_submitted.emit()
    
    
    def load_product_data(self):
        self.ui.ingrediente_nueva_mezcla.clear()
        products = get_all_products()
        for product in products:
            product_name = product[0]
            product_id = product[1]
            self.ui.ingrediente_nueva_mezcla.addItem(product_name, product_id)