#Exercises - Day 13
print()

# 7 - Escribe una función lambda que pueda resolver una pendiente o intersección de funciones lineales.

EcLineal = lambda X1,X2,Y1,Y2: (Y2 - Y1) / (X2 - X1)
print(EcLineal(5,3,10,6))

# 6- Escribe una función que calcule la pendiente de una ecuación lineal.
"""
Punto1_X = int(input("Introduce las X del punto 1: "))
Punto1_Y = int(input("Introduce las Y del punto 1: "))
print()
Punto2_X = int(input("Introduce las X del punto 2: "))
Punto2_Y = int(input("Introduce las Y del punto 2: "))
print()
def Pendiente(Punto1_X, Punto1_Y, Punto2_X, Punto2_Y):
    PendienteEc = (Punto2_Y - Punto1_Y) / (Punto2_X - Punto1_X)
    return PendienteEc
print("La inclinación de la ecuación lineal es: ", Pendiente(Punto1_X, Punto1_Y, Punto2_X, Punto2_Y))
"""