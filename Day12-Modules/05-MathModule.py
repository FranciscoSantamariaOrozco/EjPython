# Day 12 - Modules.
print()
# Math Module
"""
    Este módulo contiene la mayoría de operaciones y constantes matemáticas.
"""
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
print()

"""
    Con esto, hemos importado el módulo math que contiene montones de funciones que nos pueden ayudar a mejorar los cálculos matemáticos.
    para comprobar que funciones existen en este módulo, podemos usar help(math) o dir(math). Esto nos enseñaralas funciones disponibles en el módulo.
    Si queremos importar una función en específico del módulo podemos hacerlo de la siguiente manera:
"""
from math import pi
print(pi)
print()

# También es posible importar múltiples funciones a la vez
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
print()

# Pero si queremos importar todas las funciones del módulo math podemos usar *
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
print()

# Cuando importamos también podemos renombrar la función.
from math import pi as PI
print(PI)
print()