arq = open ("teste_aula.txt", "r") #paramentro W para criaçao e escrita, caso o arquivo exista, será apagado seu conteudo e criado um do zero.
# parametro a abre o arquivo para adicionar conteudo no arquivo
#print (arq.read()) ## ler o arquivo completo
#print (arq.readline()) ## ler linha por linha
#arq.write("XXXX, estou escrevendo no arquivo .\n") ##escreve no doc
#arq.write("XXXX, está é a segunda linha  .\n")
#print (arq.readlines()) ##cria uma lista com as linhas do arquivo


#Pecorrendo todas as linhas com readlines
for lin in arq.readlines():
    print(lin)

arq.close() ## sempre é necessario fechar o arquivo