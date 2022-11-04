# Day 10 - Loops.
print()
# La función range
# La función range() es usada para listar numeros. El rango (start, end, step) toma tres parámetros, el inicio, el final y el incremento.
# Por defecto empieza en 0 y se incrementa de uno en uno. El rango necesita almenos un argumento (final).
# Creando secuencias usando range:
Lista = list(range(11))
print(Lista)
print()
Set = set(range(1,11))
print(Set)
print()

Lista = list(range(0,11,2))
print(Lista)
print()
Set = set(range(0,11,2))
print(Set)
print()


# Syntax
"""
for iterator in range(start, end, step)
"""
for Numero in range(11):
    print(Numero)
print()