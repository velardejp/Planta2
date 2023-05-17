from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.Ui_index import MainWindow
from controllers.alta_prod import AddWindowForm

class MainWindowForm(QWidget,MainWindow):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)

        self.add_product_button.clicked.connect(self.open_add_window)
        
    
    def open_add_window(self):
        window=AddWindowForm()
        window.show()