a = lambda x: x ** 2
b = a(4)
print(b)

dobrar = lambda a: a *2
print("O dobro de vinte é : ", dobrar(20))


def inc(n):
    return lambda x: x + n

somar2 = inc(2)
somar15 = inc(15)

a = 10
b = somar2(a)

print("Primeiro incremento: ",b)

b = somar15(a)
print ("Segundo incremento:",b)



