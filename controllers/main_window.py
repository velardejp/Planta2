from PySide6.QtWidgets import QWidget
from views.Ui_index import Ui_MainWindow
from controllers.alta_prod import AddWindowForm

class MainWindowForm(QWidget):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_product_button.clicked.connect(self.open_add_window)
        self.window2 = AddWindowForm()

    def open_add_window(self):
        self.window2.show()
