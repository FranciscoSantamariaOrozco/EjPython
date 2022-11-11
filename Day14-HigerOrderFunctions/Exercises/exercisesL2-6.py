#Exercises - Day 13
print()

# L2-6 - Usa filter() para filtrar los países que tengan 6 caracteres o más en la lista de países.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', "Gru"]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def PaisesSeisLetrasOMas(Pais):
    if len(Pais) >= 6:
        return True
    return False

PaisesSeisLoMas = filter(PaisesSeisLetrasOMas, countries)
print(list(PaisesSeisLoMas))
print()