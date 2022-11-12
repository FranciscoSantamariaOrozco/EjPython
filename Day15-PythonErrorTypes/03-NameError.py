# Day 15 - Python error types
print()
# NameError

# NameError
# Como puedes ver en el mensaje, la variable edad no está definida. Si, es cierto que no hemos definido una variable de edad, pero
# estábamos intentando imprimirla como si la hubiéramos declarado.
"""
    asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print(age)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'age' is not defined
>>>
"""

# Podemos solucionarlo asignando un valor a esa variable.
"""
    >>> age = 25
    >>> print(age)
    25
    >>>
"""