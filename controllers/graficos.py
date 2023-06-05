from database.db import get_all_products
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class InventoryGraph(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.axes = fig.add_subplot(111)
        self.axes.set_facecolor((1, 1, 1, 0.5))  # Set facecolor to white with 50% transparency
        fig.patch.set_facecolor((1, 1, 1, 0.5))  # Set figure patch facecolor to white with 50% transparency
        super(InventoryGraph, self).__init__(fig)
        self.setParent(parent)


        
        self.axes.set_xlabel('Cantidad') # Cambiado a set_xlabel ya que ahora las cantidades estarán en el eje x
        self.axes.set_ylabel('Mezcla')

        # Define the palette here
        self.palette = ["#537188", "#CBB279", "#E1D4BB", "#EEEEEE"]

    def plot(self, data):
        names, values = zip(*data)
        self.axes.barh(names, values, color=self.palette, height=0.8)
        self.axes.set_xlim(0, max(values) * 1.2)  # Este código aumentará el límite superior del eje x a un 20% más que el valor más alto.
        self.axes.tick_params(axis='x', colors='white')  # Cambia el color de las etiquetas en el eje x a rojo
        self.axes.tick_params(axis='y', colors='white')
        # Asegúrate de que las etiquetas no se corten
        self.figure.tight_layout()

