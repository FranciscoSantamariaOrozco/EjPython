#Exercises - Day 13
print()

# L2-4 - Usa filter() para filtrar los países que contengan "land"
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def PaisesConLand(Pais):
    if Pais.count("land") >= 1:
        return True
    return False

PaisesLand = filter(PaisesConLand, countries)
print(list(PaisesLand))
print()