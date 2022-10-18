# Acceso a items de una lista usando el Index positivo.
"""
Los números se indexan conforme la siguiente imagen:
['banana', 'orange', 'mango', 'lemon']
    0          1        2        3
"""
print()

# La lista siempre empieza por el número 0.

Fruits = ['banana', 'orange', 'mango', 'lemon']
FirstFruit = Fruits[0]          # Accedemos al primer item usando el index 0.
print(FirstFruit)               # banana
SecondFruit = Fruits[1]
print(SecondFruit)              # orange
LastFruit = Fruits[3]
print(LastFruit)                # lemon
# último index
LastIndex = len(Fruits) -1
LastFruit = Fruits[LastIndex]
print(LastFruit)