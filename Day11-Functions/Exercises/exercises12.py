#Exercises - Day 11
print()

# 12 - Declara una función llamada RemoverItem. Tomará una lista y un item como parámetros. Devuelve la lista con el item removido.

Frutas = ["Naranja", "Pomelo", "Limón", "Manzana"]
Carne = ["Hamburguesas", "Albóndigas", "Filete"]
def RemoverItem(ListaBase, Item):
    if ListaBase.count(Item) > 0:
        print("Lista original:", ListaBase)
        ListaBase.remove(Item)
        return "Lista con el Item eliminado:", ListaBase
    else:
        return print("El item que has indicado no existe en la lista.\nLos items en la lista indicada son:\n",ListaBase)
print(RemoverItem(Frutas, "Naranja"))
    