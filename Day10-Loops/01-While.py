# Day 10 - Loops.
print()
# Loop While.

# Podemos usar la palabra reservada "while" para hacer un bucle while. 
# Se utiliza para ejecutar un bloque de sentencias repetidamente siempre que una candición sea satisfecha.
# Cuando la condición se vuelve False, las líneas de código despues del loop pueden continuar siendo ejecutadas.

# Syntax
"""
while condición:
    Código
else:
    Código
"""

Count = 0
while Count <5:
    print(Count)
    Count += 1
else:
    print()
# este bucle va iterando desde el 0 hasta el 5, imprimiendo todos los valores en el proceso.
# al adquirir el valor de 5, ya no cumple la condición de "Count <5" por lo que este último número no se imprime.
# Esto se puede solucionar poniendo "Count <=5"
Count = 0
while Count <=5:
    print(Count)
    Count += 1
else:
    print()

# Otra opción es poner al final en el else un print con el resultado Count final, asi al terminar de iterar el bucle, 
# devolverá el valor actualmente almacenado por Count, que es 5 (el 5 que no cumplia la condición de "while Count <5:" y 
# por lo tanto hace que se termine de iterar el bucle)
Count = 0
while Count <5:
    print(Count)
    Count += 1
else:
    print(Count)