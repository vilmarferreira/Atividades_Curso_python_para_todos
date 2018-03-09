from PyQt5.QtWidgets import QApplication,  QMainWindow, QPushButton, QToolButton, QToolBar
from PyQt5.QtGui import QIcon
import sys

a = QApplication(sys.argv)

#Criando um objeto do incone Qicon
icone= QIcon()
#adicionando a imagem do icone
icone.addFile("../img/exit.png")
#Criando um botao para a barra de ferramenteas
tb_sair = QToolButton()
#Setando imagem
tb_sair.setIcon(icone)
tb_sair.clicked.connect(QApplication.instance().quit)

#criando a barra de ferramentas
barra = QToolBar()
#Adicionando o botão na barra de ferramenteas
barra.addWidget(tb_sair)

jan = QMainWindow()
jan.setGeometry(50,50,250,250)
jan.setWindowTitle("Minha Janela")
jan.setWindowIcon(QIcon("../img/teste.png"))
jan.statusBar().showMessage("Mensagem")
#Adicionando a barra de ferramentas na janela
jan.addToolBar(barra)

b = QPushButton("Tchau", jan)
b.move(100,100)
b.clicked.connect(QApplication.instance().quit)
b.setToolTip("Se clicar irá sair")

jan.show()
sys.exit(a.exec_())