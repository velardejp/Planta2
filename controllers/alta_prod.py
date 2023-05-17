from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from views.Ui_add_producto import AddWindowForm

class AddWindowForm(QWidget,AddWindowForm):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)