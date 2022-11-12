# Day 15 - Python error types
print()
# ImportError

# ImportError
# No existe ninguna función llamada power en el módulo math, la que existe tiene un nombre diferente: pow.
"""
    asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from math import power
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ImportError: cannot import name 'power' from 'math'
    >>>
"""

# Vamos a hacerlo correctamente ahora.
"""
    >>> from math import pow
    >>> pow(2,3)
    8.0
    >>>
"""