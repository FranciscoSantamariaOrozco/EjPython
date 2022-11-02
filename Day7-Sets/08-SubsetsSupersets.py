# Day 7 - Sets
print()
# Comprobando Subsets y Super Sets
# Un set puede ser un subset o un superset de otros sets:
# Subset: issubset()
# Super set: issuperset

# Syntax
Set1 = {"item1", "item2", "item3", "item4"}
Set2 = {"item2", "item3"}
print("Es Set2 un subset de Set1?", Set2.issubset(Set1))
print("Es Set1 un superset de Set2?", Set1.issuperset(Set2))
print()


Numeros = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
MasNumeros ={"0", "2", "4", "6", "8", "10"}
print("Es Numeros un subset de MasNumeros?", Numeros.issubset(MasNumeros))
print("Es false, ya que Numeros es un superset de MasNumeros, no un subset.")
print()
print("Es Numeros un superset de MasNumeros?", Numeros.issuperset(MasNumeros))
print("Es True, ya que efectivamente Numeros es un superset de MasNumeros")
print()


Python = {"P", "Y", "T", "H", "O", "N"}
Dragon = {"D", "R", "A", "G", "O", "N"}
print("Es Python un subset o un superset de Dragon?", Python.issubset(Dragon), Python.issuperset(Dragon))
print("En ninguno de los casos Python es un subset o superset.")