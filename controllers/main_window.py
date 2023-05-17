from PySide6.QtWidgets import QWidget
from views.Ui_index import Ui_MainWindow
from controllers.alta_prod import AddWindowForm
from controllers.entradas import AddEntryForm

class MainWindowForm(QWidget):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_product_button.clicked.connect(self.open_addproduct_window)
        self.ui.add_entrada_button.clicked.connect(self.open_entrys_window)
        self.window2 = AddWindowForm()
        self.window3=AddEntryForm()

    def open_addproduct_window(self):
        self.window2.show()
    
    def open_entrys_window(self):
        self.window3.show()
