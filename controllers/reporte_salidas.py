from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Signal
import pandas as pd
from views.Ui_reporte_salidas import Ui_reporte_salidas
import sqlite3

class ExitReportForm(QWidget):
    reporte_salidas_submitted = Signal()
    def __init__(self, parent=None):
        super(ExitReportForm, self).__init__(parent)
        self.ui = Ui_reporte_salidas()
        self.ui.setupUi(self)
        self.get_all_exits()
        self.ui.import_excel_salidas.clicked.connect(self.excel_report)

    def get_all_exits(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        result = c.execute("SELECT id,product_id,quantity,date FROM exits")
        self.ui.tabla_salidas.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tabla_salidas.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tabla_salidas.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def excel_report(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        result = c.execute("SELECT id,product_id,quantity,date FROM exits")

    # Crear DataFrame
        df_list = []
        for row_data in result:
            df_list.append(pd.DataFrame([list(row_data)], columns=['id', 'product_id', 'quantity', 'date']))
        df = pd.concat(df_list, ignore_index=True)

    # Escribir DataFrame en Excel
        df.to_excel('salidas.xlsx', index=False)
