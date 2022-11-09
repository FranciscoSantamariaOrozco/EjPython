#Exercises - Day 11
print()

# 14 - Declara una función llamada SumaImpares. Tomará un número como parámetro, y sumará todos los impares en el rango.
def SumaImpares(Num):
    Total = 0
    i = 0
    while i <= Num:
        if i % 2 != 0:
            Total = Total + i
            i = i + 1
        else:
            i = i + 1
    return Total
print(SumaImpares(5))
print(SumaImpares(10))
print(SumaImpares(100))