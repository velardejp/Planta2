from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from views.Ui_MainWindow import Ui_MainWindow
from controllers.alta_prod import AddWindowForm
from controllers.entradas import AddEntryForm
from controllers.salidas import AddExitForm
from controllers.salida_mezcla import ExitMezclaForm
from controllers.nueva_mezcla import AddMezclaForm
from controllers.reporte_salidas import ExitReportForm
from controllers.reporte_entradas import EntryReportForm
from controllers.reporte_kardex import KardexReportForm
from database.db import get_all_products
import openai
import sqlite3
openai.api_key="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"
class MainWindowForm (QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventana_productos = AddWindowForm()
        self.ventana_entradas=AddEntryForm(self.ventana_productos)
        self.ventana_salidas=AddExitForm()
        self.ventana_mezcla=ExitMezclaForm()
        self.ventana_nueva_mezcla=AddMezclaForm()
        self.ventana_reporte_salidas=ExitReportForm()
        self.ventana_reporte_entradas=EntryReportForm()
        self.ventana_kardex=KardexReportForm()
        # Conectamos la función open_addproduct_window a la acción action_nuevoproducto
        self.ui.action_nuevoproducto.triggered.connect(self.open_addproduct_window)
        self.ui.action_entry.triggered.connect(self.open_entrys_window)
        self.ui.action_exit.triggered.connect(self.open_exits_window)
        self.ui.action_exit_mezcla.triggered.connect(self.open_exits_mezcla_window)
        self.ui.action_nuevomezcla.triggered.connect(self.open_new_mezcla_window)
        self.ui.action_report_salidas.triggered.connect(self.open_report_exits_window)
        self.ui.action_report_entradas.triggered.connect(self.open_report_entrys_window)
        self.ui.action_report_kardex.triggered.connect(self.open_report_kardex_window)
        self.ventana_nueva_mezcla.mezcla_submitted.connect(self.load_mezclas)
        self.ventana_mezcla.exit_mezcla_submitted.connect(self.load_product_stock)
       
        self.ui.chatbutton.clicked.connect(self.enviar_mensaje)

    def open_addproduct_window(self):
        self.ventana_productos.show()

    def open_entrys_window(self):
        self.ventana_entradas.show()

    def open_exits_window(self):
        self.ventana_salidas.show()
    
    def open_exits_mezcla_window(self):
        self.ventana_mezcla.show()
    def open_new_mezcla_window(self):
        self.ventana_nueva_mezcla.show()
    def open_report_exits_window(self):
        self.ventana_reporte_salidas.show()
    def open_report_entrys_window(self):
        self.ventana_reporte_entradas.show()
    def open_report_kardex_window(self):
        self.ventana_kardex.show()
    def load_product_stock(self):
        
        self.ventana_entradas.load_product_data()
        self.ventana_salidas.load_product_data()
        
    def load_mezclas(self):
        self.ventana_mezcla.load_mezcla_data()

    def enviar_mensaje(self):
        # Obtener el mensaje del usuario del campo de entrada de texto
        mensaje_usuario = self.ui.userinput.text()

        # Agregar el mensaje del usuario al historial del chat
        self.ui.chathistory.insertPlainText(f"Usuario: {mensaje_usuario}")

        # Limpiar el campo de entrada de texto
        self.ui.userinput.clear()

        # Obtener la respuesta del modelo usando la API de OpenAI
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": mensaje_usuario}
            ]
        )

        # Agregar la respuesta del modelo al historial del chat
        self.ui.chathistory.insertPlainText(f"AI: {respuesta['choices'][0]['message']['content']} \n")
