# Day 15 - Python error types
print()
# IndexError

# IndexError
# En el siguiente ejemplo, Python ha generado un error IndexError, por que la lista sólo contiene índices de 0 a 4,
# por lo que estaba fuera de rango.
"""
    asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> numbers[5]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    >>>
"""