lista_numeros = [1,2,3,4,5]
lista_clonada = lista_numeros[:] ##o parametro {:} serve para clonar a lista e a nova ficar independente da outra.
lista_clonada += [6]

print(lista_numeros)
print(lista_clonada)

lista_numeros += [7]
print("############")
print(lista_numeros)
print(lista_clonada)