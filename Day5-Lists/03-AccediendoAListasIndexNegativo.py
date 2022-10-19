# Acceso a items de una lista usando el Index negativo.
"""
Los números se indexan conforme la siguiente imagen:
['banana', 'orange', 'mango', 'lemon']
   -4         -3       -2       -1
"""
print()

# El index negativo comienza desde el final hasta el principio, empezando por -1 para el último item, -2 para el penúltimo....
Fruits = ['banana', 'orange', 'mango', 'lemon']
FirstFruit = Fruits[-4]
LastFruit = Fruits[-1]
SecondLast = Fruits[-2]
print(FirstFruit)           # banana
print(LastFruit)            # lemon
print(SecondLast)           # mango
print()

# Desempaquetando items de la lista
Lst = ['item', 'item2', 'item3', 'item4', 'item5']
FirstItem, SecondItem, ThirdItem, *Rest = Lst
print(FirstItem)