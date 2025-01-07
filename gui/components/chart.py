from PyQt5.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ChartComponent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)

        self.ax = self.canvas.figure.add_subplot(111)
        self.ax.plot([1, 2, 3], [4, 6, 5], label="Exemplo")
        self.ax.legend()

        self.setLayout(layout)
