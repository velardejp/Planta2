from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Signal
import pandas as pd
from views.Ui_reporte_kardex import Ui_reporte_kardex
from database.db import get_all_products
import sqlite3

class KardexReportForm(QWidget):
    reporte_salidas_submitted = Signal()
    def __init__(self, add_entry, add_exit, exit_mezcla,parent=None):
        super(KardexReportForm, self).__init__(parent)
        self.ui = Ui_reporte_kardex()
        self.ui.setupUi(self)
        self.ui.productos_kardex.addItems([product[0] for product in get_all_products()])
        self.get_all_entrys()
        self.get_all_exits()
        self.ui.productos_kardex.currentTextChanged.connect(self.get_all_entrys)
        self.ui.productos_kardex.currentTextChanged.connect(self.get_all_exits)
        add_entry.entry_submitted.connect(self.get_all_entrys)
        add_exit.exit_submitted.connect(self.get_all_exits)
        exit_mezcla.exit_mezcla_submitted.connect(self.get_all_exits)
    
        self.ui.import_excel_kardex.clicked.connect(self.excel_report)

    def get_all_entrys(self):
        name=self.ui.productos_kardex.currentText()
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        resultentry = c.execute("SELECT id,product_id,quantity,date FROM entries WHERE product_id = ?",(name,))
        self.ui.tabla_entradas_kardex.setRowCount(0)
        for row_number, row_data in enumerate(resultentry):
            self.ui.tabla_entradas_kardex.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tabla_entradas_kardex.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def get_all_exits(self):
        name=self.ui.productos_kardex.currentText()
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        resultexit = c.execute("SELECT id,product_id,quantity,date, mezcla FROM exits WHERE product_id = ?",(name,))
        self.ui.tabla_salidas_kardex.setRowCount(0)
        for row_number, row_data in enumerate(resultexit):
            self.ui.tabla_salidas_kardex.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tabla_salidas_kardex.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    
    def excel_report(self):
        name = self.ui.productos_kardex.currentText()
        conn = sqlite3.connect('inventarioplanta.db')

        # Crear consultas SQL
        query_exit = "SELECT id, product_id, quantity, date, mezcla FROM exits WHERE product_id = ?"
        query_entry = "SELECT id, product_id, quantity, date FROM entries WHERE product_id = ?"

        # Crear DataFrames
        entry = pd.read_sql_query(query_entry, conn, params=(name,))
        exit = pd.read_sql_query(query_exit, conn, params=(name,))

        # Cerrar la conexión a la base de datos
        conn.close()

        # Escribir DataFrames en Excel
        file = name + "kardex.xlsx"
        with pd.ExcelWriter(file) as writer:
            entry.to_excel(writer, sheet_name='Entry', index=False)
            exit.to_excel(writer, sheet_name='Exit', index=False)


