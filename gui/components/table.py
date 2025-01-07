from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableComponent(QWidget):
    def __init__(self, data=None, headers=None):
        super().__init__()
        self.init_ui(data, headers)

    def init_ui(self, data, headers):
        layout = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        layout.addWidget(table)
        self.setLayout(layout)
