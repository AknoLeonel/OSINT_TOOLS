import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QWidget, QLineEdit, QTextEdit, QTabWidget, QToolTip
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OSINT Tools GUI")
        self.setGeometry(200, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        # Estilo
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2d2d2d;
            }
            QLabel, QPushButton, QLineEdit, QTextEdit {
                font-family: 'Segoe UI';
                font-size: 12px;
                color: white;
            }
            QPushButton {
                background-color: #5A5A5A;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #76c7c0;
            }
        """)

        # Layout principal
        main_layout = QVBoxLayout()

        # Barra superior
        barra_superior = QHBoxLayout()
        label_titulo = QLabel("OS'int Tools - Segurança da Informação")
        label_titulo.setFont(QFont("Segoe UI", 14, QFont.Bold))
        barra_superior.addWidget(label_titulo)

        # Botão de ajuda (ícone de lâmpada)
        btn_ajuda = QPushButton()
        btn_ajuda.setIcon(QIcon("gui/icons/lamp.png"))
        btn_ajuda.setFixedSize(40, 40)
        btn_ajuda.setToolTip("Clique para saber mais sobre os parâmetros de busca.")
        barra_superior.addWidget(btn_ajuda, alignment=Qt.AlignRight)

        # Adicionar a barra ao layout principal
        main_layout.addLayout(barra_superior)

        # Área de ferramentas
        tabs = QTabWidget()
        tabs.addTab(self.create_whois_tab(), "Whois")
        tabs.addTab(self.create_nmap_tab(), "Nmap")
        tabs.addTab(self.create_geoip_tab(), "GeoIP")
        main_layout.addWidget(tabs)

        # Widget central
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def create_whois_tab(self):
        layout = QVBoxLayout()
        label = QLabel("Parâmetro (Insira o domínio ou IP para consulta WHOIS):")
        input_param = QLineEdit()
        input_param.setPlaceholderText("Exemplo: google.com ou 8.8.8.8")
        input_param.setToolTip("Digite o domínio ou IP que você deseja consultar.")

        result_area = QTextEdit()
        result_area.setReadOnly(True)

        btn_executar = QPushButton("Executar")
        btn_executar.setToolTip("Clique para executar a consulta WHOIS.")

        layout.addWidget(label)
        layout.addWidget(input_param)
        layout.addWidget(btn_executar)
        layout.addWidget(result_area)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def create_nmap_tab(self):
        layout = QVBoxLayout()
        label = QLabel("Parâmetro (Insira o IP ou URL para varredura de portas):")
        input_param = QLineEdit()
        input_param.setPlaceholderText("Exemplo: 192.168.1.1 ou site.com")
        input_param.setToolTip("Digite o IP ou domínio para realizar a varredura de portas com o Nmap.")

        result_area = QTextEdit()
        result_area.setReadOnly(True)

        btn_executar = QPushButton("Executar")
        btn_executar.setToolTip("Clique para realizar a varredura de portas.")

        layout.addWidget(label)
        layout.addWidget(input_param)
        layout.addWidget(btn_executar)
        layout.addWidget(result_area)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def create_geoip_tab(self):
        layout = QVBoxLayout()
        label = QLabel("Parâmetro (Insira o IP para localização geográfica):")
        input_param = QLineEdit()
        input_param.setPlaceholderText("Exemplo: 8.8.8.8")
        input_param.setToolTip("Digite o IP que você deseja localizar geograficamente.")

        result_area = QTextEdit()
        result_area.setReadOnly(True)

        btn_executar = QPushButton("Executar")
        btn_executar.setToolTip("Clique para consultar a localização geográfica do IP.")

        layout.addWidget(label)
        layout.addWidget(input_param)
        layout.addWidget(btn_executar)
        layout.addWidget(result_area)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
