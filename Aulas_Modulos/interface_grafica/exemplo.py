from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPicture, QPixmap

class ExemploLabel(QWidget):
    def __init__(self):
        super(ExemploLabel, self).__init__()
        self.setWindowTitle("Exemplo QLabel (Rótulo)")
        self.setGeometry(200, 200, 400, 200)

        self.label_nome = QLabel("Nome")
        self.edit_nome = QLineEdit()

        self.label_sobrenome = QLabel("Sobrenome")
        self.edit_sobrenome = QLineEdit()

        self.label_celular = QLabel("&Celular")
        self.edit_celular = QLineEdit()

        self.label_nascimento = QLabel("&Data de nascimento")
        self.edit_nascimento = QLineEdit()

        self.label_numero = QLabel()
        self.label_figura = QLabel()
        self.label_imagem = QLabel()

        self.label_endereco = QLabel("&Endereço completo")
        self.edit_endereco = QLineEdit()

        self.label_nome.setText("&Primeiro nome")

        self.label_sobrenome.setFrameStyle(QFrame.Panel)
        self.label_celular.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.label_nascimento.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        self.label_sobrenome.setAlignment(Qt.AlignCenter)
        self.label_celular.setAlignment(Qt.AlignRight)

        self.label_nome.setBuddy(self.edit_nome)
        self.label_sobrenome.setBuddy(self.edit_sobrenome)
        self.label_celular.setBuddy(self.edit_celular)
        self.label_nascimento.setBuddy(self.edit_nascimento)


        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label_nome)
        self.layout.addWidget(self.edit_nome)

        self.layout.addWidget(self.label_sobrenome)
        self.layout.addWidget(self.edit_sobrenome)

        self.layout.addWidget(self.label_celular)
        self.layout.addWidget(self.edit_celular)

        self.layout.addWidget(self.label_nascimento)
        self.layout.addWidget(self.edit_nascimento)

        self.layout.addWidget(self.label_endereco)
        self.layout.addWidget(self.edit_endereco)

        self.layout.addWidget(self.label_numero)
        self.layout.addWidget(self.label_figura)
        self.layout.addWidget(self.label_imagem)

        self.label_nome.setToolTip("Informe seu nome:")
        self.label_numero.setNum(10.5)

        figura = QPicture()
        pintor = QPainter()
        pintor.begin(figura)
        pintor.drawEllipse(0, 0, 60, 60)
        pintor.end()

        self.label_figura.setPicture(figura)
        pixmap = QPixmap('../img/teste.png')
        self.label_imagem.setPixmap(pixmap)

        self.setLayout(self.layout)

import sys
app = QApplication(sys.argv)
jan = ExemploLabel()
jan.show()
sys.exit(app.exec_())
