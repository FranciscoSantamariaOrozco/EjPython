# Day 9 - Condicionales.
print()
# Condicional If Elif Else
# En caso de que tengamos más de dos condiciones, podemos utilizar el condicionarl If Elif Else.
# En la vida real, tomamos decisiones a diario. No comprobamos una o dos condiciones si no que comprobamos múltiples condiciones.
# De una manera similar, en la programación podemos necesitar consultar muchas condiciones. Usaremos Elif cuando tengamos múltiples condiciones.

# Syntax
"""
# syntax
if condicion:
    codigo
elif condicion:
    codigo
else:
    codigo
"""

# Este código permite introducir un número desde consola, y comprobar si es positivo, negativo, o cero.

A = input("Introduce un número:")
A = int(A)
if A > 0:
    print("A es un número positivo")
elif A < 0:
    print("A es un número negativo")
else:
    print("A es igual a cero")
print()