import sys
from PySide6.QtWidgets import QApplication
from controllers.index import MainWindowForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindowForm()
    widget.show()
    sys.exit(app.exec())
        