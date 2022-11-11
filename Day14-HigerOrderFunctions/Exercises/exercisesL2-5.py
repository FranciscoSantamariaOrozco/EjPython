#Exercises - Day 13
print()

# L2-5 - Usa filter() para filtrar los países que tengan exactamente 6 caracteres.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def PaisesSeisLetras(Pais):
    if len(Pais) == 6:
        return True
    return False

PaisesSeisL = filter(PaisesSeisLetras, countries)
print(list(PaisesSeisL))
print()