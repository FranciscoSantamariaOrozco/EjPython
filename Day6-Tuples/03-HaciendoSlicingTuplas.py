# Day 6 - Tuplas
print()
# Slicing en Tuplas
# Podemos hacer slice hacia una subtupla especificando un rango de index de inicio y de final en la tupla.
# Devolverá una nueva tupla con los items especificados.

# Rango de index positivos

Tupla = ('item1', 'item2', 'item3', 'item4', 'item5')
TodosLosItems = Tupla[0:5]
print("Todos los items de la tupla:", TodosLosItems)
SegundoEnAdelante = Tupla[1:]
print("Todos los items de la tupla desde el segundo:", SegundoEnAdelante)
MiddleTwo = Tupla[1:3]
print("los dos items de enmedio", MiddleTwo)
print()


Frutas = ('banana', 'orange', 'mango', 'lemon')
AllFruits = Frutas[0:4]
print("Todas las frutas, de la 0 a la 4:", AllFruits)
AllFruits = Frutas[0:]
print("Todas las frutas, desde el indice 0: ", AllFruits)
OrangeMango = Frutas[1:3]
print("Solo el indice 1 y 2", OrangeMango)
OrangeToTheRest = Frutas[1:]
print("Frutas desde el indice uno en adelante:", OrangeToTheRest)
print()


# Rango de index negativos

Tupla = ('item1', 'item2', 'item3', 'item4')
AllItems = Tupla[-4:]
print("Todos los items:", AllItems)
MiddleTwo = Tupla[-3:-1]
print("Los dos items intermedios:", MiddleTwo)
print()

Frutas = ('banana', 'orange', 'mango', 'lemon')
AllFruits = Frutas[-4]
print("Todas las frutas:", AllFruits)
OrangeMango = Frutas[-3:-1]
print("Frutas de la mitad:", OrangeMango)
OrangeToTheRest = Frutas[-3:]
print("Desde el -3 hasta el final:", OrangeToTheRest)
print()