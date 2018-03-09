def faturial(x):
    if x <= 1:
        return 1
    else :
        return (x * faturial(x-1))


n = int (input("Informe um valor: "))
print ("Fatorial de ",n, "é", faturial(n))

