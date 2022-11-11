#Exercises - Day 13
print()

# L2-9 - Declara una función llamada ConvertirAString que tome una lista como parámetro y devuelva una lista que contenga solo strings.
TiposVariados = ['Asabeneh', 'Lidiya', {"Casado" : False}, 'Ermias', 'Abraham', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Estonia', True,'Finland', 'Sweden', False, 'Denmark', 'Norway', 'Iceland']

def DetectarStrings(Item):
    if type(Item) is str:
        return Item  

ListaSoloConStrings = filter(DetectarStrings, TiposVariados)
print(list(ListaSoloConStrings))

"""
ListaCompletaConversionStrings = map(ConvertirStrings, TiposVariados)
print(list(ListaCompletaConversionStrings))

def ConvertirStrings(Item):
    Item = str(Item)
    return Item
"""