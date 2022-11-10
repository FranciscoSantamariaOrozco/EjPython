#Exercises - Day 13
print()

# 2 - Aplana la siguiente matriz dimensional:

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

ListaPlana = [number for row in list_of_lists for number in row]
ListaPlana = [number for row in ListaPlana for number in row]
print(ListaPlana)
print()