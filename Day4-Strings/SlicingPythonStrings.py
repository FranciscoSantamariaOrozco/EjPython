# En Python podemos truncar strings dentro de strings:
print()

language = "Python"
FirstThree = language[0:3] # Comienza en el Index 0 y sube hasta el 3 pero no incluye el 3
print(FirstThree)

LastThree = language[3:6]
print(LastThree)
# Otra manera
LastThree = language[-3:]
print(LastThree)
LastThree = language[3:]
print(LastThree)
print()


# Reverse a string
greeting = "Hola, chanchito!"
print(greeting[::-1])
print()

# Skipping characters
language = "Python"
pto = language[0:6:2]
print(pto)
print()