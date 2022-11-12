# Day 15 - Python error types
print()
# ModuleNotFound Error

# ModuleNotFound Error
# En el ejemplo, hemos añadido deliberadamente una letra "s" a una operación matemática, y Python ha generado un error
# ModuleNotFoundError. 
"""
asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import maths
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'maths'
>>>
"""

# Podemos solucionarlo poniendo correctamente el nombre del módulo a importar.
"""
    >>> import math
    >>>
"""