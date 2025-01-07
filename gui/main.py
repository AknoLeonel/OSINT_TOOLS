import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QLineEdit, QTextEdit, QTabWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from components.table import TableComponent
from components.chart import ChartComponent

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OSINT Tools - Segurança da Informação")
        self.setGeometry(200, 100, 1000, 700)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet(open(r"C:\Users\Aknol\APIs Github\OSINT_TOOLS\OSINT_TOOLS\gui\styles.qss").read())

        # Layout principal
        main_layout = QVBoxLayout()

        # Barra superior
        barra_superior = QHBoxLayout()
        label_titulo = QLabel("OSINT Tools - Segurança da Informação")
        barra_superior.addWidget(label_titulo)

        btn_ajuda = QPushButton()
        btn_ajuda.setIcon(QIcon("gui/icons/lamp.png"))
        btn_ajuda.setFixedSize(40, 40)
        btn_ajuda.setToolTip("Clique para saber mais sobre os parâmetros.")
        barra_superior.addWidget(btn_ajuda, alignment=Qt.AlignRight)

        # Adicionar a barra ao layout principal
        main_layout.addLayout(barra_superior)

        # Abas de ferramentas
        tabs = QTabWidget()
        tabs.addTab(self.create_whois_tab(), "Whois")
        tabs.addTab(self.create_nmap_tab(), "Nmap")
        tabs.addTab(self.create_chart_tab(), "Gráficos")
        main_layout.addWidget(tabs)

        # Widget central
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def create_whois_tab(self):
        layout = QVBoxLayout()
        label = QLabel("Insira o domínio ou IP para consulta WHOIS:")
        input_param = QLineEdit()
        input_param.setPlaceholderText("Exemplo: google.com ou 8.8.8.8")
        result_area = QTextEdit()
        result_area.setReadOnly(True)

        btn_executar = QPushButton("Executar")
        layout.addWidget(label)
        layout.addWidget(input_param)
        layout.addWidget(btn_executar)
        layout.addWidget(result_area)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def create_nmap_tab(self):
        layout = QVBoxLayout()
        label = QLabel("Insira o IP ou domínio para varredura de portas:")
        input_param = QLineEdit()
        input_param.setPlaceholderText("Exemplo: 192.168.1.1 ou site.com")
        result_area = QTextEdit()
        result_area.setReadOnly(True)

        btn_executar = QPushButton("Executar")
        layout.addWidget(label)
        layout.addWidget(input_param)
        layout.addWidget(btn_executar)
        layout.addWidget(result_area)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def create_chart_tab(self):
        layout = QVBoxLayout()
        label = QLabel("Gráficos e Relatórios:")
        chart_component = ChartComponent()  # Exemplo de gráfico
        layout.addWidget(label)
        layout.addWidget(chart_component)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
