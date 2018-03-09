lista_pares = []
lista_impares = []

while True:
    numero= int (input("Digite um número inteiro (informe 0 para sair )"))
    if numero == 0:
        break

    if numero %2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    lista_pares.sort()
    lista_impares.sort()

print(f"Números pares : {lista_pares}")
print(f"Números impares: {lista_impares}")