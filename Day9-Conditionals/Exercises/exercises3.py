#Exercises - Day 9
print()

# 2- Obten dos números del usuario con la función input. Si A es mayor que B, devuelve "%numeroA% Es mayor que %numeroB%".
# Si B es mas pequeño, lo mismo pero indicando que es mas pequeño. También haz un else si son iguales.

print("Comparadora de números.\nEste programa comprueba si el primer número que introduces (A)\nes mayor o menor que el segundo número introducido (B)\n")

A = input("Introduce el número A:")
B = input("Introduce el número B:")
if A > B:
    print(A, "es mayor que", B)
elif A < B:
    print(A, "es menor que", B)
else:
    print("A y B son iguales", A, "==", B)
print()