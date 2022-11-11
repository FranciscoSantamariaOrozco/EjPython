#Exercises - Day 13
print()

# L2-7 - Usa filter() para filtrar los países que empiecen por la letra E.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', "Gru", "España"]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def PaisesPorE(Pais):
    if Pais.startswith("E") == True:
        return True
    return False

ListaPaisesPorE = filter(PaisesPorE, countries)
print(list(ListaPaisesPorE))
print()