with open("teste_aula2.txt") as arq: #utilizando o with para abrir e não ter que se preocupar com o fechamento do arquivo
    for lin in arq:
        print(lin)

arq2 = open("teste_aula2.txt", "w")
arq2.write("Mais uma linha")
arq.close()
