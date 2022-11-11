#Exercises - Day 13
print()

# 6 - Cambia la siguiente lista de listas a una lista de strings concatenadas.
"""
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    output
    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
ListaPlana = [name[0]+ " " + name[1] for row in names for name in row]
print(ListaPlana)
print()