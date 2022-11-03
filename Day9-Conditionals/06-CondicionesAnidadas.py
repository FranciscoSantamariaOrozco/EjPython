# Day 9 - Condicionales.
print()
# Condiciones anidadas 
# Las condiciones pueden ser anidadas unas bajo las otras.

# Syntax
"""
    if condicion:
        codigo
        if condicion:
            codigo
"""


A = input("Introduce un número:")
A = int(A)
if A > 0:
    if A % 2 == 0:
        print("El número es positivo y es un número par")
    else:
        print("El número es un número positivo.")
elif A == 0:
    print("El número es cero")
else:
    print("El número es un número negativo.")
print()


# Se puede evitar el uso de las condiciones anidadas con el operador and.