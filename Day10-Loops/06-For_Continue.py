# Day 10 - Loops.
print()
# continue en for.
# Podemos usar continue para hacer skip de algunas de las iteraciones del bucle.
"""
    for iterador in secuencia
        codigo
        if ccondicion:
            continue
"""
Numeros = (1, 2, 3, 4, 5)
for i in Numeros:
    print(i)
    if i == 3:
        continue
    print("El proximo número debería ser ", i + 1) if i != 5 else print("Final del bucle")
print("Saliendo del bucle....")
print()