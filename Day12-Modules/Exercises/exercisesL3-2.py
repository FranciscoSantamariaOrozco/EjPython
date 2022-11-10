#Exercises - Day 12
print()

# L3-2 - Escribe una función que devuelva un array de siete números aleatorios en el rango del 0 al 9. todos los números deben de ser únicos.
from random import randint

def RandomArray():
    ArrayAleatorio = ""
    for i in range(20):
        Num = randint(0,9)
        Num = str(Num)
        if len(ArrayAleatorio) == 7:
            return ArrayAleatorio
        elif ArrayAleatorio.count(Num) == 0:
            ArrayAleatorio = ArrayAleatorio + Num
print(RandomArray())