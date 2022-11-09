#Exercises - Day 11
print()

# 11 - Declara una función que se llame "AñadirItem". Esta tomará una lista y un ítem como parámetros. Devolvera la lista con el item añadido al final.

Frutas = ["Naranja", "Pomelo", "Limón", "Manzana"]
Carne = ["Hamburguesas", "Albóndigas", "Filete"]

def AnadirItem(ListaBase, *Item):
    if type(ListaBase) is list:
        i = 0
        while i < len(Item):
            ListaBase.append(Item[i])
            i = i + 1
        return ListaBase
    else:
        print("No has facilitado una lista válida")
        return "Error"

print(AnadirItem(Frutas, "Platano", "Pera", "Kiwi"))
print(AnadirItem(Carne, "Lomo", "Picaña", "Paté"))
print(AnadirItem("Cocacola", "Fanta"))
