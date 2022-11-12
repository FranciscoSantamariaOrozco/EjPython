# Day 15 - Python error types
print()
# ValueError

# ValueError
# En este caso no podemos cambiar la string a int o a float, ya que la "a" no puede convertirse.
"""
    asabeneh@Asabeneh:~$ python
    Python 3.9.6 (default, Jun 28 2021, 15:26:21)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> int('12a')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '12a'
    >>>
"""