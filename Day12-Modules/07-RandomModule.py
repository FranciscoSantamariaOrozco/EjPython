# Day 12 - Modules.
print()
# Random Module
"""
    Ahora que importar módulos ya es algo familiar para nosotros, hagamos una importación más para terminar de familiarizarnos con ella.
    Importemos el módulo random que nos da un número aleatorio entre 0 y 0.9999.....
    El módulo aleatorio tiene muchas funciones, pero en esta sección solo usaremos random y randint.
"""
from random import random, randint
print(random())             # Si no le damos argumentos, nos devuelve un valor entre 0 y 0.9999
print(randint(5,20))        # Nos devolverá un entero aleatorio entre el 5 y el 20, inclusive.