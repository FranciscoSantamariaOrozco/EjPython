#Exercises - Day 11
print()

# 13 - Declara una función llamada SumaNumeros. Este tomará un número como parámetro y sumará todos los números en ese rango.
def SumaNumeros(Num):
    Total = 0
    i = 0
    while i <= Num:
        Total = Total + i
        i = i + 1
    return Total
print(SumaNumeros(5))
print(SumaNumeros(10))
print(SumaNumeros(100))