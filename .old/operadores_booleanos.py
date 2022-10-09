# Ejemplo de operadores de comparación (booleanos)
print(3 > 2)        # True
print(3 >= 2)       # True
print(3 < 2)        # False
print(2 < 3)        # True
print(2 <= 3)       # True
print(3 == 2)       # False
print(3 != 2)       # True
print()
print(len("mango") == len("avocado"))       # False
print(len("mango") != len("avocato"))       # True
print(len("mango") < len("avocato"))        # True
print(len("milk") != len("meat"))           # False
print(len("milk") == len("meat"))               # True
print(len("tomato") == len("potato"))       # True
print(len("python") > len("dragon"))        # False
print()

# Comparaciones de True y False
print("True == True: ", True == True)
print("True == False: ", True == False)
print("False == False: ", False == False)
print()

# Otros comparadores de operadores en python
# is (==), is not (!=), in, not in 

print("1 is 1: ", 1 is 1)
print("1 is not 2: ", 1 is not 2)
print("F in Francisco", "F" in "Francisco")
print("B in Francisco: ", "B" in "Francisco" )
print("coding" in "coding for all")
print("CodiNg" in "coding for all")
print("a in an: ", "a" in "an")
print("4 is 2 ** 2: ", 4 is 2 ** 2)