# Day 13 - List comprehension.
print()
# Función Lambda
"""
    La función lambda es una pequeña función anónima sin nombre. Puede tomar cualquier numero de argumentos, pero sólo una expresión.
    La función lambda es similar a la función "anonymous" en JavaScript. 
    La necesitamos cuando queremos crear una función anónima dentro de otra función.
"""

# Creando una función lambda
"""
    para crear una función lambda podemos usar la palabra clave "lambda" seguida de los parámetros, seguida de la expresión.~
    La función lambda no utiliza return ya que ya devuelve explícitamente el return.
"""

# Syntax
"""
    x = lambda param1, param2, param3: param1 + param2 + param2
    print(x(arg1, arg2, arg3))
"""

def SumaDosNumeros(a, b):
    return a + b

print(SumaDosNumeros(3, 5))
print()

# ahora vamos a cambiar la función por una función lambda:

SumaDosNumeros = lambda a, b: a + b
print(SumaDosNumeros(3, 5))
print()

# Función lambda autoinvocada
(lambda a, b: a + b)(3, 5)
print((lambda a, b: a + b)(3, 5))

Cuadrado = lambda a: a * a
print(Cuadrado(5))
Cubo = lambda a: a * a * a
print(Cubo(3))

# Con múltiples variables

MultipleVariables = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(MultipleVariables(5, 5, 3))
print()

# Función lambda dentro de otras funciones

def Potencia(x):
    return lambda n : x ** n
Cubo = Potencia(2)(3)
print(Cubo)
DosElevadoCinco = Potencia(2)(5)
print(DosElevadoCinco)
print()