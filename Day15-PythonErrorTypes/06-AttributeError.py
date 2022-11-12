# Day 15 - Python error types
print()
# AttributeError

# AttributeError
# Como puedes ver, me he vuelto a equivocar! En lugar de pi, intenté llamar a una funcion de PI del módulo math.
# Se produjo un error de atributo, lo que significa que la función no existe en el módulo. 
"""
    asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import math
    >>> math.PI
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    AttributeError: module 'math' has no attribute 'PI'
    >>>
"""

# Corrigiendo el nombre de la función ya podemos obtener la función pi del módulo y recibir el resultado.
"""
    >>> math.pi
    3.141592653589793
    >>>
"""