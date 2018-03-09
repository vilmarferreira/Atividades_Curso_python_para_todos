from Heranca.Exemplo_Pessoa.Pessoa import Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)
        self.cnpj = cnpj