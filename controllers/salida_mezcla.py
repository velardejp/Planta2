from PySide6.QtWidgets import QWidget, QTableWidgetItem
from views.Ui_ventana_mezcla import Ui_exit_mezcla_window
import datetime
from PySide6.QtCore import Signal
from database.db import get_all_products, add_exit, get_all_mezclas


class ExitMezclaForm(QWidget):
    
    exit_mezcla_submitted = Signal()
    def __init__(self, parent=None):
        super(ExitMezclaForm, self).__init__(parent)
        self.ui = Ui_exit_mezcla_window()
        self.ui.setupUi(self)

        self.ui.productos_para_mezcla.addItems([product[0] for product in get_all_products()])
        self.ui.mezcla_combobox.addItems([product[0] for product in get_all_mezclas()])
        self.ui.agregar_ingrediente.clicked.connect(self.agregar_ingrediente)
        self.ui.submit_exit_mezcla.clicked.connect(self.submit_exit_mezcla_process)

    def agregar_ingrediente(self):
        ingrediente = self.ui.productos_para_mezcla.currentText()
        cantidad = self.ui.cantidad_exit_paramezcla.value()
        # Obtiene el número actual de filas
        num_row = self.ui.ingredientes_mezcla.rowCount()
        # Inserta una nueva fila al final de la tabla
        self.ui.ingredientes_mezcla.insertRow(num_row)
        # Crea nuevos ítems para la fila
        item_ingrediente = QTableWidgetItem(ingrediente)
        item_cantidad = QTableWidgetItem(str(cantidad))
        # Añade los ítems a la fila
        self.ui.ingredientes_mezcla.setItem(num_row, 0, item_ingrediente)
        self.ui.ingredientes_mezcla.setItem(num_row, 1, item_cantidad)

    def submit_exit_mezcla_process(self):
        num_rows = self.ui.ingredientes_mezcla.rowCount()

        for row in range(num_rows):
            ingrediente = self.ui.ingredientes_mezcla.item(row, 0).text()
            cantidad = float(self.ui.ingredientes_mezcla.item(row, 1).text())  # convertir la cantidad a un número
            add_exit(ingrediente,cantidad)
        self.exit_mezcla_submitted.emit()
    def load_mezcla_data(self):
        self.ui.mezcla_combobox.clear()
        self.ui.mezcla_combobox.addItems([product[0] for product in get_all_mezclas()])
    
    
