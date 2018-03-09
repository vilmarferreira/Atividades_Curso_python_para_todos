from Heranca.Exemplo_Pessoa.Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf
