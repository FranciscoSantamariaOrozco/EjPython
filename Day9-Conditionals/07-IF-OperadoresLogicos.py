# Day 9 - Condicionales.
print()
# Condiciones IF y operadores lógicos.
"""
    if condicion and condicion:
        code
"""

A = input("Introduce un número:")
A = int(A)
if A > 0 and A % 2 == 0:
    print("El número es positivo y par")
elif A > 0 and A % 2 != 0:
    print("El número es positivo")
elif A == 0:
    print("El número es 0")
else:
    print("El número es negativo")
print()