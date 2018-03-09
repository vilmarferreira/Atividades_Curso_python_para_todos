def soma (*valores):
    total=0
    for numero in valores:
        total += numero
    return total

def media (*valores):
    total = soma(*valores)
    return total / len(valores)