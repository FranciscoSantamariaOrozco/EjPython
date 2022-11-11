#Exercises - Day 13
print()

# L2-1 - Usa map() para crear una nueva lista que camnbie cada país a mayúsculas en la lista paises.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Mayusc(Pais):
    return Pais.upper()

PaisesMayusc = map(Mayusc, countries)
print(list(PaisesMayusc))
print()