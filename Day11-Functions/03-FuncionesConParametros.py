# Day 11 - Functions.
print()
# Funciones con parámetros
"""
    Una función puede pasar diferentes tipos de datos 
    (números, strings, boolean, listas, tuplas, diccionarios o sets) como parámetros.
"""

# Syntax
"""
    def NombreFuncion(parametro)
        codigo
        codigo
    print(NombreFuncion(argumento))
"""

def Saludo(Nombre):
    Mensaje = Nombre + ", Bienvenido de vuelta a Python para todos!"
    return Mensaje
print(Saludo("Francisco"))
print()

def DiezMas(num):
    Diez = 10
    return num + Diez
print(DiezMas(90))
print()

def CuadradoNumero(x):
    return x * x
print(CuadradoNumero(2))
print()

def AreaCirculo(r):
    PI = 3.14
    Area = PI * r ** 2
    return Area
print(AreaCirculo(10))
print()

def Sumatorio(n):
    Total = 0
    for i in range(n+1):
        Total += i
    return(Total)
print(Sumatorio(10))
print(Sumatorio(100))
print()