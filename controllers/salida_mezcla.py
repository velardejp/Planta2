from PySide6.QtWidgets import QWidget, QTableWidgetItem
from views.Ui_ventana_mezcla import Ui_exit_mezcla_window
import datetime
from PySide6.QtCore import Signal
import sqlite3
from database.db import get_all_products, add_exit, get_all_mezclas, make_id_exit,add_exit_mezcla

class ExitMezclaForm(QWidget):
    total_porcentaje = 0  # Variable para almacenar el porcentaje total
    exit_mezcla_submitted = Signal()
    def __init__(self, add_product, add_mezcla, parent=None):
        super(ExitMezclaForm, self).__init__(parent)
        self.ui = Ui_exit_mezcla_window()
        self.ui.setupUi(self)
        
        self.total_porcentaje = 0  # Variable para almacenar el porcentaje total

        products = get_all_mezclas()
        for mezclas in products:
            mezcla_name = mezclas[0]
            mezcla_id = mezclas[1]
            self.ui.mezcla_combobox.addItem(mezcla_name, mezcla_id)
        
        self.get_all_ingredients()
        
        self.ui.mezcla_combobox.currentTextChanged.connect(self.get_all_ingredients)
        self.ui.productos_para_mezcla.addItems([product[0] for product in get_all_products()])
        self.ui.agregar_ingrediente.clicked.connect(self.agregar_ingrediente)
        self.ui.submit_exit_mezcla.clicked.connect(self.submit_exit_mezcla_process)
        add_product.product_submitted.connect(self.load_mezcla_data)
        add_mezcla.mezcla_submitted.connect(self.load_mezcla_data)
        add_mezcla.mezcla_submitted.connect(self.get_all_ingredients)
        self.ui.ingredientes_mezcla.cellChanged.connect(self.percent)
        
        self.check_porcentaje()

        
        


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
        id = make_id_exit()
        mezcla_quantity = self.ui.cantidad_mezcla.value()
        mezcla = self.ui.mezcla_combobox.currentText()
        self.total_porcentaje = 0  # Reiniciar el porcentaje total
        exit_successful = True

        for row in range(num_rows):
            ingrediente = self.ui.ingredientes_mezcla.item(row, 0).text()
            cantidad = float(self.ui.ingredientes_mezcla.item(row, 1).text())

            if not add_exit(id, ingrediente, cantidad, mezcla):
                exit_successful = False
                break

        if not exit_successful:
            return

        self.ui.ingredientes_mezcla.clearContents()
        self.ui.ingredientes_mezcla.setRowCount(0)
        add_exit_mezcla(id, mezcla, mezcla_quantity)
        self.exit_mezcla_submitted.emit()
    
    def get_all_ingredients(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        id=self.ui.mezcla_combobox.currentData()
        result = c.execute("SELECT product_name, cantidad FROM mezcla_ingrediente WHERE mezcla_id=?",(id,))
        self.ui.ingredientes_mezcla.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.ingredientes_mezcla.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.ingredientes_mezcla.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def percent(self):
        num_rows = self.ui.ingredientes_mezcla.rowCount()
        mezcla_quantity = self.ui.cantidad_mezcla.value()

        if mezcla_quantity == 0:
            self.ui.porcentaje.setText('0%')
            return

        total_porcentaje = 0  # Variable local para almacenar el porcentaje total

        for row in range(num_rows):
            cantidad_item = self.ui.ingredientes_mezcla.item(row, 1)
            if cantidad_item is not None:
                ingrediente = float(cantidad_item.text())
                porcentaje = (ingrediente * 100) / mezcla_quantity
                porcentaje_item = self.ui.ingredientes_mezcla.item(row, 2)
                if porcentaje_item is None:
                    porcentaje_item = QTableWidgetItem()
                    self.ui.ingredientes_mezcla.setItem(row, 2, porcentaje_item)
                porcentaje_item.setText(f'{porcentaje:.2f}%')
                total_porcentaje += porcentaje

        self.total_porcentaje = total_porcentaje
        self.ui.porcentaje.setText(str(total_porcentaje))  # Actualizar la variable de porcentaje total
        self.check_porcentaje()
    def check_porcentaje(self):
        if self.total_porcentaje == 100:
            self.ui.porcentaje.setStyleSheet("background-color: green;")
            self.ui.submit_exit_mezcla.setEnabled(True)
        else:
            self.ui.porcentaje.setStyleSheet("background-color: red;")
            self.ui.submit_exit_mezcla.setEnabled(False)

        
    def load_mezcla_data(self):
        self.ui.mezcla_combobox.clear()
        self.ui.mezcla_combobox.addItems([product[0] for product in get_all_mezclas()])
        self.ui.productos_para_mezcla.addItems([product[0] for product in get_all_products()])
        self.get_all_ingredients()
    def refresh(self):
        self.load_mezcla_data()
    # Aquí puedes añadir cualquier otra función que necesites para actualizar la ventana.


    
    
