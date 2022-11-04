#Exercises - Day 10
print()

# L3-2 Esta es una lista de frutas: ['banana', 'orange', 'mango', 'lemon']. Dale la vuelta a la lista usando un loop.
Frutas = ['banana', 'orange', 'mango', 'lemon']
FrutasR = []
for i in range(len(Frutas)):
    FrutasR.insert(0, Frutas[i])
Frutas = FrutasR
del FrutasR
print(Frutas)