# Day 7 - Sets
print()
# Diferencias simetricas entre dos sets
# Esta función devuelve la diferencia simetrica entre dos sets.
# Esto significa que devuele un conjunto que contiene todos los elementos de ambos conjuntos, excepto
# los elementos que estan presentes en ambos conjuntos, matemáticamente. (A\B) o (B\A)

# Syntax

Set1 = {"item1", "item2", "item3", "item4"}
Set2 = {"item2", "item3"}
print("Este es el set 1:", Set1)
print("Este es el set2:", Set2)
print("Y esta es la diferencia simetrica de ambos Sets:", Set2.symmetric_difference(Set1))
print()

Numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
MasNumeros = {1, 2, 3, 4, 5}
print("Este es el set Numeros:", Numeros)
print("Este es el set MasNumeros:", MasNumeros)
print("Y esta es la diferencia simetrica entre ellos:", MasNumeros.symmetric_difference(Numeros))
print()


Phyton = {"p", "y", "t", "h", "o", "N"}
Dragon = {"d", "r", "a", "g", "o", "n"}
print("Esto es el set python:", Phyton)
print("Y esto es la cadena dragon", Dragon)
print("Esta es la diferencia simetrica entre ambos sets", Phyton.symmetric_difference(Dragon))
print()