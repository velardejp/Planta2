from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Signal
import pandas as pd
from views.Ui_reporte_entradas import Ui_reporte_entradas
import sqlite3

class EntryReportForm(QWidget):
    reporte_salidas_submitted = Signal()
    def __init__(self, add_entry,parent=None):
        super(EntryReportForm, self).__init__(parent)
        self.ui = Ui_reporte_entradas()
        self.ui.setupUi(self)
        self.get_all_entrys()
        self.ui.import_excel_entradas.clicked.connect(self.excel_report)
        add_entry.entry_submitted.connect(self.get_all_entrys)

    def get_all_entrys(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        result = c.execute("SELECT id,product_id,quantity,date FROM entries")
        self.ui.tabla_entradas.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tabla_entradas.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tabla_entradas.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def excel_report(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        result = c.execute("SELECT id,product_id,quantity,date FROM entries")

    # Crear DataFrame
        df_list = []
        for row_data in result:
            df_list.append(pd.DataFrame([list(row_data)], columns=['id', 'product_id', 'quantity', 'date']))
        df = pd.concat(df_list, ignore_index=True)

    # Escribir DataFrame en Excel
        df.to_excel('salidas.xlsx', index=False)
