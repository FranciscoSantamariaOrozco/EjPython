#Exercises - Day 10
print()

# 7- Usa un bucle for para iterar del 0 al 100 e imprimir solamente los números pares.

for i in range(101):
    if i % 2 != 0:
        continue
    else:
        print(i)