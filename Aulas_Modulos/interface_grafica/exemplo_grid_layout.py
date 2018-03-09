from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit, QWidget)

class ExemploGridLayout(QWidget):
    def __init__(self):
        super(ExemploGridLayout, self).__init__()
        self.setWindowTitle("Exemplo QGridLayout")
        self.adicionar_componentes()
        self.definir_layout()

    def adicionar_componentes (self):
        self.label =QLabel ("Label")
        self.edit = QLineEdit()
        self.label1 = QLabel("Label")
        self.edit1 = QLineEdit()
    def definir_layout(self):
        layout_jan = QGridLayout()
        layout_jan.addWidget(self.label, 0, 0)
        layout_jan.addWidget(self.edit, 1, 0)
        layout_jan.addWidget(self.label1, 0, 1)
        layout_jan.addWidget(self.edit1, 1, 1)
        self.setLayout(layout_jan)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    jan = ExemploGridLayout()
    jan.show()
    sys.exit(app.exec_())