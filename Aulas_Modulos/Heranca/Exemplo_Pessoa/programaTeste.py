from Heranca.Exemplo_Pessoa.pessoaFisica import PessoaFisica
from Heranca.Exemplo_Pessoa.pessoaJuridica import PessoaJuridica

pf = PessoaFisica("Teste1", 5, "000.000.000-00")
pj = PessoaJuridica("Loja Teste", 2, "00.000.000/0000-00")
print(pf.nome)
print(pf.idade)
print(pf.cpf)

print(pj.nome)
print(pj.idade)
print(pj.cnpj)
