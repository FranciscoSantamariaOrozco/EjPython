# Day 15 - Python error types
print()
# TypeError

# TypeError
# El error TypeError es generado por que no podemos operar un tipo int con un tipo str.
"""
    asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 4 + '3'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>
"""

# La primera solución es convertir la string en int o en float. Otra solución puede ser convertir el número en string (en 
# cuyo caso se operaria como con strings y el resultado sería 43 al concatenarse estas, en vez de sumarse como números)
"""
    >>> 4 + int('3')
    7
    >>> 4 + float('3')
    7.0
    >>>
"""