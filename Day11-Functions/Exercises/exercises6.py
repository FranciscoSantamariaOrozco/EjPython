#Exercises - Day 11
print()

# 6- Escribe una función que calcule la pendiente de una ecuación lineal.
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