class RevelarAcesso(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("Recupenrando ", self.name)
        return self.val
    def __set__(self, instance, value):
        print("Atualizando ", self.name)
        self.val = value

class MinhaClasse (object):
    x = RevelarAcesso(10, 'Var "X"')
    y = 5

m = MinhaClasse()
print("X:", m.x)
m.x = 20
print("X: ", m.x)