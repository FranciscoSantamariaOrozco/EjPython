#Exercises - Day 11
print()

# L3-3 - Escribe una función que compruebe si todos los items de una lista contienen el mismo tipo de dato.
Frutas = ["Manzana", "Pera", "Kiwi", "Platano", "Naranja", "Manzana"]
Persona = ["Francisco", "Orozco", 34, True, {"Habilidades":"Python"} ]
def SameItems(Lista):
    i = 0
    while i < len(Lista):
        i2 = 0
        while i2 < len(Lista):
            if type(Lista[i]) == type(Lista[i2]):
                i2 = i2 + 1
            else:
                return "Esta es una lista mixta"
        i = i + 1
    return "Todos los  items en la lista son del mismo tipo:", type(Lista[0])
print(SameItems(Persona))