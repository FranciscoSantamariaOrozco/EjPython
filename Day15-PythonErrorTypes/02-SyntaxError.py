# Day 15 - Python error types
print()
# Syntax error


# Syntax error.
# Como puedes ver, se crea un Syntax error debido a que hemos olvidado encerrar la cadena a imprimir entre caracteres, y python
# nos sugiere una solución.
"""
asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print 'hello world'
    File "<stdin>", line 1
        print 'hello world'
                        ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
    >>>
"""

# Podemos solucionarlo añadiendo los paréntesis para que la sintaxis de la función print sea correcta.
"""
    >>> print('hello world')
    hello world
    >>>
"""