from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QLabel, QLineEdit)
import sys

class ExemploBoxLayout(QWidget):
    def __init__(self):
        super(ExemploBoxLayout,self).__init__()
        self.setWindowTitle("Exemplo Layout")
        self.label_nome = QLabel("Nome: ")
        self.label_telefone = QLabel("Telefone: ")
        self.label_celular = QLabel("Celular")
        self.edit_nome = QLineEdit()
        self.edit_telefone = QLineEdit()
        self.edit_celular = QLineEdit()

        self.layout_tela = QHBoxLayout()
        self.layout_tela.addWidget(self.label_nome)
        self.layout_tela.addWidget(self.edit_nome)
        self.layout_tela.addWidget(self.label_telefone)
        self.layout_tela.addWidget(self.edit_telefone)
        self.layout_tela.addWidget(self.label_celular)
        self.layout_tela.addWidget(self.edit_celular)

        self.setLayout(self.layout_tela)


app = QApplication(sys.argv)
jan = ExemploBoxLayout()
jan.show()
sys.exit(app.exec_())

