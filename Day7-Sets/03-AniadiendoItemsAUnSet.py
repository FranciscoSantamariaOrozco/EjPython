# Day 7 - Sets
print()
# Comprobando items en un set.

# Para comprobar si un item existe en un set es necesario utilizar el operador in.

Set = {"item1", "item2", "item3", "item4"}
print("El set original:", Set)
Set.add("item5")
print("El set con item 5 añadido:", Set)
print()

Frutas = {"banana", "orange", "mango", "lemon"}
print("El set original:", Frutas)
Frutas.add("lime")
print("El set con lima añadido:", Frutas)
print()

# Se pueden añadir varios items a la vez con la función update(). Esta función toma una lista como argumento.
Set = {"item1", "item2", "item3", "item4"}
print("El set original:", Set)
Set.update(["item5", "item6", "item7"])
print("El set con items 5, 6 y 7 añadido:", Set)
print()

Frutas = {"banana", "orange", "mango", "lemon"}
print("El set original:", Frutas)
Vegetales = ("tomato", "potato", "cabbage", "onion", "carrot")
Frutas.update(Vegetales)
print("El set con Vegetales añadido:", Frutas)
print()