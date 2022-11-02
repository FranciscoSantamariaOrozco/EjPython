# Day 7 - Sets
print()
# Unir Sets
# Si dos sets no tienen ningún item en comun, los llamamos conjuntos disjuntos.
# podemos comprobar si dos sets son disjuntos usando isdisjoint.

# Syntax

Set1 = {"item1", "item", "item3", "item4"}
Set2 = {"item1", "item5"}
print("Este es el set 1:", Set1)
print("Y este es el set 2:", Set2)
print("Son disjuntos estos dos sets? ", Set1.isdisjoint(Set2))
print()


Numeros = {0, 2, 4, 6, 8}
MasNumeros = {1, 3, 5, 7,9}
print("Esta es la cadena Numeros:", Numeros)
print("Y esta es la cadena MasNumeros:", MasNumeros)
print("Son ambas cadenas disjuntas?", Numeros.isdisjoint(MasNumeros))
print()