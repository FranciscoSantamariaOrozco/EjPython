# Day 11 - Funciones
print()
# Número de argumentos arbitrario
# Si no conocemos el número de argumentos que se van a dar con una función, podemos crear una función que tome un número arbitrario de argumentos
# añadiendo * antes del nombre del parámetro.

# Syntax

"""
    def NombreFuncion(*args)
        codigo
        codigo
    NombreFuncion(param1, param2, param3)
"""

def SumNums(*Nums):
    Total = 0
    for Num in Nums:
        Total += Num
    return Total
print(SumNums(5,7,12,20))
print()

# Número arbitrario de argumentos con argumentos por defecto

def GeneradorGrupos(Team = 1, *Args):
    print(Team)
    for i in Args:
        print(i)
print(GeneradorGrupos("Team1", "Francisco", "Chest", "Paco", "Leal"))
print()