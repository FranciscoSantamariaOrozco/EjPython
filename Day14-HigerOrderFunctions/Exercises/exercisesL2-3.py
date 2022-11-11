#Exercises - Day 13
print()

# L2-3 - Usa map() para cambiar todos los nombres a mayúsculas en la lista de nombres.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Mayusc(Nombre):
    return Nombre.upper()

NombresMayusc = map(Mayusc, names)
print(list(NombresMayusc))
print()