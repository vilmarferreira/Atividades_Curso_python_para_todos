class Arrancada(object):
    def __init__(self, metros, segundos):
        self._metros_percorridos = metros
        self._tempo_gasto = segundos
        self._velocidade = self._metros_percorridos / self._tempo_gasto

    ##Transformar a função em propriedade
    @property
    def velocidade(self):
        print("Retornando o valor de velocidade.")
        return f"A média de velocidade foi: {self._velocidade:.2f} metros por segundo."

    #propriedade set
    @velocidade.setter
    def velocidade(self, velocidade):
        print("Atribuindo valor à velocidade.")
        self._velocidade = velocidade

    @velocidade.deleter
    def velocidade(self):
        print("Excluindo velocidade.")
        del self._velocidade

a = Arrancada(10, 30)
print(a.velocidade)
##passando o valor para a propriedae
a.velocidade = 40
print(a.velocidade)

del a.velocidade
