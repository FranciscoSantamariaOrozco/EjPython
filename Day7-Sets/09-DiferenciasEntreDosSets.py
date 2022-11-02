# Day 7 - Sets
print()
# Diferencias entre dos sets
# Podemos utilizar la fución diference() para encontrar las diferencias entre dos sets.
# Compara la primera cadena con la segunda.


Set1 = {"item1", "item2", "item3", "item4"}
Set2 = {"item2", "item3"}
print("", Set2.difference(Set1))            # Al no haber diferencias, muestra solamente un set vacio. (todos los componentes de set2 comparados con Set1 existen)
print("", Set1.difference(Set2))        
print()


Numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
MasNumeros = {0, 2, 4, 6, 8, 10}
print("Esta es la cadena Numeros:", Numeros)
print("Y esta es la cadena MasNumeros:", MasNumeros)
print("Y estas son las diferencias entre ambas cadenas:", Numeros.difference(MasNumeros))
print()


Python = {"p", "y", "t", "h", "o" , "n"}
Dragon = {"d", "r", "a", "g", "o" , "n"}
print("Esta es la cadena python:", Python)
print("Y esta la cadena dragon:", Dragon)
print("Estas son las diferencias entre ambas cadenas", Python.difference(Dragon))
print()