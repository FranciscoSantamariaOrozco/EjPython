# Day 6 - Tuplas
print()
# Accediendo a items en una tupla
# El index positivo es similar al ya utilizado para las listas. Se comienza en el 0. Para contar a la inversa se puede empezara con -1.
TuplaItems = ("Item1", "Item2", "Item3", "Item4")
TuplaFrutas = ("Banana", "Orange", "Mango", "Lemon")

print(TuplaItems)
FirstItem = TuplaItems[0]
SecondItem = TuplaItems[1]
LastItem = TuplaItems[len(TuplaItems)-1]
print("El primer Item de la tupla es:", FirstItem)
print("El segundo Item de la tupla es:", SecondItem)
print("El último Item de la tupla es:", LastItem)
print()


# El index negativo comienza con -1.

print(TuplaFrutas)
FirstItem = TuplaFrutas[-4]
SecondItem = TuplaFrutas[-3]
LastItem = TuplaFrutas[-1]
print("El primer Item de la tupla es:", FirstItem)
print("El segundo Item de la tupla es:", SecondItem)
print("El último Item de la tupla es:", LastItem)
print()