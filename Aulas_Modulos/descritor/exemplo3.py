class DescritorValor():

    def __init__(self):
        self.valor = {}#{} representa o dicionario
    ##metodos para o descritor
    def __get__(self, instance, owner):
        return self.valor[instance]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("O Valor não pode ser negativo.")
        else:
            self.valor[instance] = value
    def __delete__(self, instance):
        del self.valor[instance]

class Carro():
    valor = DescritorValor() ##declarando um descritor
    def __init__(self, marca , modelo, valor):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor

    def __str__(self):
        return f"Marca : {self.marca}, Modelo: {self.modelo}, Valor: R$ {self.valor:.2f}"

fusquinha = Carro("WV", "Fusca", 8500)
gol = Carro("WV", "Gol", 20000)
print(fusquinha)
print(gol)

