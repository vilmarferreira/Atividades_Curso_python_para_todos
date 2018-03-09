arq = open ("teste_aula2.txt", "w")
lista = ["Laranja\n","Maçã\n", "Uva\n"]

arq.writelines(lista)
arq.close()