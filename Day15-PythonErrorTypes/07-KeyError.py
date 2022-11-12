# Day 15 - Python error types
print()
# KeyError

# KeyError
# Hay un error en la clave utilizada para obtener el valor del diccionario. Por lo tanto, este es un KeyError.
"""
    asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
    >>> users['name']
    'Asab'
    >>> users['county']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'county'
    >>>
"""

# Se soluciona fácilmente corrigiendo la key del diccionario.
"""
    >>> user['country']
    'Finland'
    >>>
"""