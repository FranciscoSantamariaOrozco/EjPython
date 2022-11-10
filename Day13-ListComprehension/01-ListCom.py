# Day 13 - List comprehension.
print()
# Comprensión de listas.
"""
    La comprensión de listas en Python es una manera compacta de crear una lista desde una secuencia. Es un camino rápido para crear
    una nueva lista. La comprensión de listas es considerablemente más rápida que procesar una lista usando el bucle for.
"""

# Syntax
"""
    i for i in iterable if expresión
"""

# Por ejemplo, si quieres cambiar una cadena a una lista de caracteres, podemos usar varios métodos. 

LenguajeProgramacion = "Python"

ListPython = list(LenguajeProgramacion)
print(type(ListPython))
print(ListPython)
print()

ListPython = [i for i in LenguajeProgramacion]
print(type(ListPython))
print(ListPython)
print()

# Por ejemplo, si queremos generar una lista con todos los números.

Nums = [i for i in range(11)]
print(Nums)
print()

# Es posible hacer operaciones durante la iteración

Cuadrados = [i * i for i in range(11)]
print(Cuadrados)
print()

# También es posible generar una lista de tuplas

NumsConCuadrados = [(i, i * i) for i in range(11)]
print(NumsConCuadrados)
print()


# La comprensión de listas puede ser combinada con expresiones

Pares = [i for i in range(51) if i % 2 == 0]
print(Pares)
Impares = [i for i in range(51) if i % 2 != 0]
print(Impares)
print()

# Filtrar números; vamos a filtrar los números pares positivos:
NumsEnt = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10, 80]
ParesFiltrados = [i for i in range(100) if i % 2 == 0 and i > 0 and NumsEnt.count(i) >= 1]
print(ParesFiltrados)
print()

# Aplanar matriz dimensional
ListaDeListas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ListaPlana = [number for row in ListaDeListas for number in row]
print(ListaPlana)
print()