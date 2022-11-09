#Exercises - Day 11
print()

# L3-1 - Escribe una función llamada EsPrimo, que compruebe si un número es primo.
def EsPrimo(Num):
    i = 2
    while i <= Num:
        if Num % i != 0:
            i = i + 1
        elif i == Num:
            return "El número es primo"
        else:
            return "El número no es primo, es dvisible por", i
print(EsPrimo(31))