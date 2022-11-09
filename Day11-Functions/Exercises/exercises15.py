#Exercises - Day 11
print()

# 15 - Declara una función llamada SumaPares. Tomará un número como parámetro, y sumará todos los pares en el rango.
def SumaPares(Num):
    Total = 0
    i = 0
    while i <= Num:
        if i % 2 == 0:
            Total = Total + i
            i = i + 1
        else:
            i = i + 1
    return Total
print(SumaPares(5))
print(SumaPares(10))
print(SumaPares(100))