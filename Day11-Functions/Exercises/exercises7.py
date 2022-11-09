#Exercises - Day 11
print()

# 7- Haz una fórmula capaz de resolver ecuaciones cuadradas.

A = int(input("Introduce el valor de A: "))
B = int(input("Introduce el valor de B: "))
C = int(input("Introduce el valor de C: "))
print()
def EcSegGrad(A, B, C):
    XPositivo = (-B + (((B * B) - 4 * A *  C) ** 0.5)) / (2 * A)
    XNegativo = (-B - (((B * B) - 4 * A *  C) ** 0.5)) / (2 * A)
    return XPositivo, XNegativo
print(EcSegGrad(A, B, C))
print()