#Exercises - Day 13
print()

# 5 - Usa un bucle for para imprimir todos los nombres de la lista nombres.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Nombres(Lista):
    for i in range(len(Lista)):
        print(Lista[i])

print(Nombres(names))