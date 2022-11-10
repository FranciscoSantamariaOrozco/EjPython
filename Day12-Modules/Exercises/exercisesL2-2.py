#Exercises - Day 12
print()

# L2-2 - Escribe una función llamada ListaRGB que devuelva cualquier número de colores RGB en un array.
from random import randint

def ListaRGB():
    ListaSalida = []
    Colores = randint(1,10)
    RGB = ""
    for i in range(Colores):
        for i2 in range(3):
            RandNum = randint(1,255)
            RandNum = str(RandNum)
            RGB = RGB + RandNum + ","
        ListaSalida.append("(" + RGB + ")")
        RGB = ""
   # print("rgb = (", RGB, ")")
    print(ListaSalida)
print(ListaRGB())