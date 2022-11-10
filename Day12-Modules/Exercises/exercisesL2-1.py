#Exercises - Day 12
print()

# L2-1 - Escribe una función llamada ListaColoresHexa que devuelva cualquier número de colores en exadecimal en un array (Los números hexadecimales
# se escribe con un # delante). Los números hexadecimales estan formados por 16 símbolos, de la a a la f y los números del 0 al 9.

from random import choice, randint
Valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E","F"]
Resultado = []
def ListaColoresHexa():
    width = randint(1,10)
    print()
    for i in range(width):
        ID = "#"
        for i2 in range(6):
            RandomNum = choice(Valores)
            RandomNum = str(RandomNum)
            ID = ID + RandomNum
        #print("Color", i, ":", ID)
        Resultado.append(ID)
    print(Resultado)

print(ListaColoresHexa())