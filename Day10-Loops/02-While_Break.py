# Day 10 - Loops.
print()
# Break y Continue.
# Podemos usar break si queremos salir o parar el bucle.

# Syntax
"""
    while condición:
        Código
        if otracondición:
            break
"""

Count = 0
while Count < 5:
    print(Count)
    Count = Count + 1
    if Count == 3:
        break