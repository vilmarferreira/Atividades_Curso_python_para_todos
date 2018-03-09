class MeuDescritor(object):
    def __init__(self, valor_inicial=None, nome="my_var"):
        self.valor = valor_inicial
        self.nome = nome

    def __get__(self, instance, owner):
        print("Obtendo: ",self.nome)
        return self.valor

    def __set__(self, instance, value):
        print(f"Atribuindo {value} a {self.nome}")
        self.valor=value

class MinhaCLasse(object):
    descritor = MeuDescritor(valor_inicial='10', nome ='Dinheiro')
    normal = 20

classe = MinhaCLasse()
print(classe.descritor)
print(classe.normal)
classe.descritor =200
print(classe.descritor)
classe.normal = 150
print(classe.normal)
