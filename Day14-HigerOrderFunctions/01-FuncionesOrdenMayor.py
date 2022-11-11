# Day 14 - List comprehension.
print()
# Higer Order Functions
"""
    En Python las funciones son tratadas como ciudadanos de primera clase, permitiendo realizar las siguientes operaciones con funciones:
        - Una función puede tomar una o más funciones como parámetros.
        - Una funcion puede ser devuelta como resultado de otra función.
        - Una función puede ser modificada.
        - Una función puede ser asignada a una variable.

    En esta sección cubriremos: 
        1 - Manejo de funciones como parámetros.
        2 - Devolver funciones como valor de retorno de otras funciones.
        3 - Usar cierres y decoradores de PYthon.
"""

# Función como parametro

def SumNums(nums):          # Función normal
    return sum(nums)        # Función triste que abusa de la función sum incorporada :(

def HigerOrderFunc(f, Lista):
    Suma = f(Lista)
    return Suma
Result = HigerOrderFunc(SumNums, [1, 2, 3, 4, 5])
print(Result)
print()


# Función como valor de retorno
# En este ejemplo podemos ver como la función superior devuelve diferentes funciones dependiendo del parámetro que le pasemos.

def Cuadrado(x):
    return x ** 2

def Cubo(x):
    return x ** 3

def Absoluto(x):
    if x >= 0:
        return x
    else:
        return -(x)

def HigerOrderFunc(Tipo):
    if Tipo == "Cuadrado":
        return Cuadrado
    elif Tipo == "Cubo":
        return Cubo
    elif Tipo == "Absoluto":
        return Absoluto

Result = HigerOrderFunc("Cuadrado")
print(Result(3))        # 9
Result = HigerOrderFunc("Cubo")
print(Result(3))        # 27
Result = HigerOrderFunc("Absoluto")
print(Result(3))        # 3
print()