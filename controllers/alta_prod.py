from PySide6.QtWidgets import QWidget
from views.Ui_add_producto import Ui_AddWindowForm

class AddWindowForm(QWidget):
    def __init__(self, parent=None):
        super(AddWindowForm, self).__init__(parent)
        self.ui = Ui_AddWindowForm()
        self.ui.setupUi(self)
