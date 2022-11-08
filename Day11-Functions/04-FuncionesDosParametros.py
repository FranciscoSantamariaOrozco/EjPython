# Day 11 - Functions.
print()
# Funciones con dos parámetros
"""
    Las funciones pueden tener o no tener parámetro o parmetros. Una función puede tener dos o más parámetros.
    Si tu función toma parámetros los podemos llamar con argumentos. comprobemos una función con dos parámetros:
"""

# Syntax
"""
    def NombreFuncion(para1, para2):
        codigo
        codigo
    print(NombreFuncion(arg1, arg2))
"""

def NombreCompleto(Nombre, Apellido):
    Espacio = " "
    NomComp = Nombre + Espacio + Apellido
    return NomComp
print(NombreCompleto("Francisco", "Orozco"))
print()

def SumaDosNum(Num1, Num2):
    Total = Num1 + Num2
    return Total
print(SumaDosNum(5, 7))
print()

def CalcularEdad(Aactual, Anacimiento):
    Edad = Aactual - Anacimiento
    return Edad
print(CalcularEdad(2021,1819))
print()

def PesoObjeto(Masa, Gravedad):
    Peso = str(Masa * Gravedad) + " N"
    return Peso
print("Peso de objeto en Newtons:", PesoObjeto(100,9.81))
print()