# Day 14 - List comprehension.
print()
# Función filter()
"""
   La función filter()  llama a la función especificada y devuelve un valor booleano para cada item del iterable(una lista) especificado. 
   Filtra los elementos que cumplen con los criterios del filtrado.
"""

# Syntax
"""
    filter(funcion, iterable)
"""

# Filtrar solo los números pares.
Numeros  = [1, 2, 3, 4, 5]   # iterable

def EsPar(num):
    if num % 2 == 0:
        return True
    return False

NumerosPares = filter(EsPar, Numeros)
print(list(NumerosPares))
print()


# Otro ejemplo
Numeros  = [1, 2, 3, 4, 5]   # iterable

def EsImpar(x):
    if x % 2 != 0:
        return True
    return False

NumerosImpares = filter(EsImpar, Numeros)
print(list(NumerosImpares))
print()

# Filtrar nombres largos
Nombres = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham', "Francisco"]  # iterable
def EsElNombreLargo(Nombre):
    if len(Nombre) > 7:
        return True
    return False

NombresLargos = filter(EsElNombreLargo, Nombres)
print(list(NombresLargos))