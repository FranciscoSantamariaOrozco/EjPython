#Exercises - Day 11
print()

# 8- Declara una función que tome una lista como parámetro e imprima cada elemento de la lista.
Frutas = ["Manzana", "Pera", "Kiwi", "Platano", "Naranja"]
NoSoyUnaLista = {"Soy", "un", "set"}
def ImprimirLista(Lista):
    if type(Lista) is list:
        for i in Lista:
            print(i)
        return "\nFin de la lista"
    else:
        return "no es una lista, no se puede procesar"
print(ImprimirLista(Frutas))
print()