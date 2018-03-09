def soma (num1, num2):
    total = num1 + num2
    return total
def subtracao (num1, num2):
    total = num1 - num2
    return total

def divicao (num1, num2):
    total = num1 / num2
    return total

def multiplicacao (num1, num2):
    total = num1 * num2
    return total

def calcular (funcao, num1, num2): ## recebendo uma função como parametro
    return funcao(num1, num2)


total = calcular(soma, 10, 25)
print(f"Resultado da soma: {total}")
## passando uma função como parametro
total = calcular(multiplicacao, 10, 25)
print(f"Resultado da Multiplicacao: {total}")



# Desempacotamento de parâmetros
def soma2(imprime, *valores):
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f"Soma: {total}")
    return total

soma2(True, 10, 20, 30, 78)
x=soma2(False, 10, 50)

print(x)

