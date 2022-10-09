# Operadores lógicos
# and: devuelve True cuando ambos operandos devuelven True.
# or:  devuelve True cuando uno de los operandos devuelve True.
# not: invierte el resultado, devuelve False si el resultado es True.

print(3 > 2 and 4 > 3)      # True, ambos son true.
print(3 > 2 and 4 < 3)      # False, el segundo operando es False.
print(3 < 2 and 4 < 3)      # False, ambos operandos son False.
print("True and True: ", True and True)
print(3 > 2 or 4 > 3)       # True, ambos son True.
print(3 > 2 or 4 < 3)       # True, por que el segundo operando es True.
print(3 < 2 or 4 < 3)       # False, por que ambos operandos son false.
print("True or False: ", True or False)
print(not 3 > 2)            # False, ya que 3>2 es True, y el not lo invierte.
print(not True)             # False, negation.
print(not False)            # True
print(not not True)         # True
print(not not False)        # False
print()

print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and False: ", False and False)
print()
print("True or True: ", True or True)
print("True or False", True or False)
print("False or False", False or False)
print()
print("not True: ", not True)
print("not False: ", not False)