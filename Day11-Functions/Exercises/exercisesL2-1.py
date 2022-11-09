#Exercises - Day 11
print()

# L2-1 - Declara una función llamada ParesImpares. Tomará un número entero positivo como parámetro y contará el número de pares e impares en el número.
def ParesImpares(Num):
    i = 0
    TotalPares = 0
    TotalImpares = 0
    while i <= Num:
        if i % 2 == 0:
            TotalPares = TotalPares + 1
            i = i + 1
        elif i % 2 != 0:
            TotalImpares = TotalImpares + 1
            i = i + 1
    return print("# La cantidad de números pares es", TotalPares, "\n# La cantidad de números impares es", TotalImpares)
print(ParesImpares(100))