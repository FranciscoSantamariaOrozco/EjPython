#Exercises - Day 11
print()

# L3-2 - Escribe una funcion que compruebe si todos los items de una lista son únicos.

Frutas = ["Manzana", "Pera", "Kiwi", "Platano", "Naranja", "Manzana"]
def ListaUnica(Lista, Item):
    i = 0
    while i < len(Frutas):
        if Lista.count(Item) == 1:
            return "El item es único"
        elif Lista.count(Item) == 0:
            return "El item no existe en la lista"
        else:
            return "El item no es único, existe", Lista.count(Item), "veces."
        print()
print(ListaUnica(Frutas, "Manzana"))