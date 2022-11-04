# Day 10 - Loops.
print()
# Continue
# Con la sentencia continue podemos hacer skip de la iteracción actual, y continuar con la siguiente.

# Syntax
"""
    while condición:
        código
        if otracondición
            continue
"""

Count = 0
while Count < 10:
    if Count == 3:
        Count = Count +1
        continue
    elif Count == 6:
        Count = Count +1
        continue
    print(Count)
    Count = Count + 1
else:
    print(Count)
print()

# Este bucle se saltará el 3 y el 6, pero seguirá iterando hasta obtener todos los números.