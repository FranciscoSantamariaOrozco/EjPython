#Exercises - Day 12
print()

# L2-3 - Escribe una función llamada GenerarColores que pueda generar cualquier número de colores hexadecimales o RGB.

from random import choice, randint
Valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E","F"]
Resultado = []


def ListaColoresHexa(Cantidad):
    Cantidad = int(Cantidad)
    print()
    for i in range(Cantidad):
        ID = "#"
        for i2 in range(6):
            RandomNum = choice(Valores)
            RandomNum = str(RandomNum)
            ID = ID + RandomNum
        #print("Color", i, ":", ID)
        Resultado.append(ID)
    return Resultado
def ListaRGB(Cantidad):
    ListaSalida = []
    RGB = "rgb("
    for i in range(Cantidad):
        for i2 in range(3):
            if i2 == 2:
                RandNum = randint(1,255)
                RandNum = str(RandNum)
                RGB = RGB + RandNum
            else:
                RandNum = randint(1,255)
                RandNum = str(RandNum)
                RGB = RGB + RandNum + ","
        ListaSalida.append(RGB + ")")
        RGB = "rgb("
# print("rgb = (", RGB, ")")
    return ListaSalida
def GenerarColores(Tipo,Cantidad):
    if Tipo == "hexa":
        print()
        print("Colores hexadecimales aleatorios:", Cantidad)
        return ListaColoresHexa(Cantidad)
    elif Tipo == "RGB":
        print()
        print("Colores RGB aleatorios:", Cantidad)
        return ListaRGB(Cantidad)

Tipo = input("Introduce (RGB) o (hexa) : ")
if Tipo == "RGB" or Tipo == "hexa":
    Cantidad = input("Introduce la cantidad: ")
    Cantidad = int(Cantidad)
    print(GenerarColores(Tipo, Cantidad))
else:
    print("El tipo que has introducido no es correcto")