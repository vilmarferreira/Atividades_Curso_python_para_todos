palavras = []
with open("hino_nacional.txt" , "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.replace(",","").replace("!","") ## ira fazer a substituição do caracter pelo outro
        palavras += linha.upper().split()
print(palavras)

while True:
    palavra = input ("\n\nInforme uma palavra para ver se faz parte do Hino Nacional (ou sair para finalizar ): ")

    if palavra.upper() == "SAIR":
        print ("\nObrigado por usar o sistema, volte sempre. ")
        break
    elif palavra.upper() in palavras:
        print ("A palavra ", palavra, "foi encontrada no Hino Nacional.") ## palavra.upper verifica se tem alguma palavra na lista
        print ("Quantidade de ocorrências: ", palavras.count(palavra.upper())) ##ira contar o numero de vezes que a palavra aparece na lista
    else:
        print ("A palavra, ", palavra, "não foi encontrada no Hino Nacional")