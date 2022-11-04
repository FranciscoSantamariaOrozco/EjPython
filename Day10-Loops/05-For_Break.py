# Day 10 - Loops.
print()
# Break en for
# Podemos usar break para parar o salir del bucle, igual que haciamos con while.
"""
    for iterador in secuencia
        codigo
        if condicion
            break
"""
Numeros = (1, 2, 3, 4, 5)
for i in Numeros:
    print(i)
    if i == 3:
        break
print()