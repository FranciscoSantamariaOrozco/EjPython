# Day 7 - Sets
print()
# Encontrando items cruzados entre dos sets
# El método intersection nos devuelve los items que se encuentran en ambos sets.

# Syntax
Set1 = {"item1", "item2", "item3", "item4"}
Set2 = {"item3", "item5", "item1"}
print("Los elementos que coinciden en ambos sets son:", Set1.intersection(Set2))
print()


Numeros = {1, 2, 3 , 4, 5, 6, 7, 8, 9, 10}
MasNumeros = {0, 2, 4, 6, 8, 10, 12}
print("Los números que coinciden en ambos sets son:", Numeros.intersection(MasNumeros))
print()