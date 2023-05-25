from PySide6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog
from views.Ui_catalago import Ui_ventana_catalago
from PySide6.QtCore import Signal
import subprocess
import os
import platform
import pandas as pd
import datetime
import sqlite3

class CatalogoForm(QWidget):
    entry_submitted = Signal()
    def __init__(self, add_product,add_mezcla ,parent=None):
        super(CatalogoForm,self).__init__(parent)
        self.ui = Ui_ventana_catalago()
        self.ui.setupUi(self)
        self.get_catalogo()
        self.ui.import_catalago.clicked.connect(self.excel_report)
        add_product.product_submitted.connect(self.get_catalogo)
        add_mezcla.mezcla_submitted.connect(self.get_catalogo)
    def get_catalogo(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        products = c.fetchall()
        self.ui.tabla_catalago.setRowCount(0)
        for row_number, row_data in enumerate(products):
            self.ui.tabla_catalago.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tabla_catalago.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    from PySide6.QtWidgets import QFileDialog

    def excel_report(self):
        conn = sqlite3.connect('inventarioplanta.db')
        c = conn.cursor()
        result = c.execute("SELECT * FROM products")

    # Crear DataFrame
        df_list = []
        for row_data in result:
            df_list.append(pd.DataFrame([list(row_data)], columns=['ID', 'PRODUCTO', 'UNIDAD DE MEDIDA', 'STOCK']))
        df = pd.concat(df_list, ignore_index=True)

    # Generar cuadro de diálogo para guardar archivo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar como...", "","Excel Files (*.xlsx)", options=options)

    # Asegurarse de que el nombre del archivo termina en .xlsx
        if not fileName.endswith('.xlsx'):
            fileName += '.xlsx'

    # Escribir DataFrame en Excel
        if fileName:
            df.to_excel(fileName, index=False)

        # Abre el archivo en Excel
            if platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', fileName))
            elif platform.system() == 'Windows':  # Windows
                os.startfile(fileName)
            else:  # linux variants
                subprocess.call(('xdg-open', fileName))

