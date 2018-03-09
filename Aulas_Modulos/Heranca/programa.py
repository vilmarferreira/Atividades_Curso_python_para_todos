from Heranca.clase_derivada1 import Classe_derivada1
from Heranca.classe_derivada2 import Classe_derivada2

class Classe_teste():
    calculo = Classe_derivada1(10, 20)
    resultado = calculo.somar()
    print(resultado)
    resultado = calculo.subtrair()
    print(resultado)
    calculo.imprimir("Olá mundo!")

    calc = Classe_derivada2(25, 41)
    resultado = calc.multiplicar(20, 40)
    print(resultado)
    resultado = calc.somar()
    print(resultado)
