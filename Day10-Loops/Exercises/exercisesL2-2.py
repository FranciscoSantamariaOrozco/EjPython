#Exercises - Day 10
print()

# L2-2 Usa un bucle que itere desde 0 hasta 100 e imprima la suma de todos los números pares juntos, y todos los impares juntos.
SumPares = 0
SumImpares = 0
for i in range(101):
    if i % 2 == 0:
        SumPares = SumPares + i
    else:
        SumImpares = SumImpares + i
print("La suma de los números pares del 1 al 100 es", SumPares, ", y la de los impares es", SumImpares)