from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from views.Ui_nueva_mezcla import Ui_nueva_mezcla_window
from database.db import add_mezcla_data

class AddMezclaForm(QWidget):
    mezcla_submitted = Signal()
    def __init__(self, parent=None):
        super(AddMezclaForm, self).__init__(parent)
        self.ui = Ui_nueva_mezcla_window()
        self.ui.setupUi(self)

        self.ui.submit_mezcla_button.clicked.connect(self.submit_mezcla)
    
    def submit_mezcla(self):
        name=self.ui.nombre_mezcla.text()

        add_mezcla_data(name)
        self.ui.nombre_mezcla.clear()
        self.mezcla_submitted.emit()