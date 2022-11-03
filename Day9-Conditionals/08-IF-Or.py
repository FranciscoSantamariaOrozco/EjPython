# Day 9 - Condicionales.
print()
# If y OR como operadores lógicos.

# Syntax
"""
    if condicion or condicion:
        codigo
"""


Usuario = input("Introduzca el nombre del usuario:")
AccLvl = input("Introduzca el nivel de permisos:")
AccLvl = int(AccLvl)
if Usuario == "admin" or AccLvl >= 4:
    print("Acceso permitido!")
else:
    print("Acceso denegado!")
print()