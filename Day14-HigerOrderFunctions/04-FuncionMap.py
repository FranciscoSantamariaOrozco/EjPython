# Day 14 - List comprehension.
print()
# Creando funciones de orden mayor
"""
    Algunas de las funciones de orden mayor incorporadas que cubrimos en esta parte son map(), filter y reduce. La función lambda
    se puede pasar como un parámetro y el mejor caso de uso de las funciones lambda es en funciones como map, filter y reduce.
"""

# Función map()
# La función map() es una función incorporada que toma una funcion y un iterable como parámetros.

# Syntax
"""
    map(función, iterable)
"""

Numeros = [1, 2, 3, 4, 5]   # iterable
def Cuadrado(x):
    return x  ** 2
NumerosCuadrados = map(Cuadrado, Numeros)
print(list(NumerosCuadrados))
print()

# ahora vamos a aplicar la función lambda
NumerosCuadrados = map(lambda x : x ** 2, Numeros)
print(list(NumerosCuadrados))
print()

# Otro ejemplo

NumerosString = ["1", "2", "3", "4", "5"]   # iterable
NumerosInt = map(int, NumerosString)
print(list(NumerosInt))
print()

# Otro ejemplo más

Nombres = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']    # iterable
def CambioUpper(Nombre):
    return Nombre.upper()

NombresMayusc = map(CambioUpper, Nombres)
print(list(NombresMayusc))
print()

# y ahora con una función lambda

NombresMayusc = map(lambda Nombre: Nombre.upper(), Nombres)
print(list(NombresMayusc))
print()

"""
    Lo que realmente hace la función map es iterar sobre una lista. Por ejemplo, itera sobre los nombres de la lista, 
    los va convirtiendo uno a uno en Mayusc, y devuelve una nueva lista.
"""