palavras = []
with open("hino_nacional.txt", encoding="utf-8") as arq:
    for lin in arq:
        palavras += lin.split() ## vai criar uma lista com as palavras de cada linha;

print(palavras)