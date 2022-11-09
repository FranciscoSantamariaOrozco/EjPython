#Exercises - Day 11
print()

# L2-3 - Declara una función que se llame EstaVacio. Tomará un parámetro y comprobara si esta vacío o no.
def EstaVacio(Item):
    if len(Item) == 0:
        return "Este item está vacío."
    else:
        return "Este item tiene una longitud de", len(Item)
print(EstaVacio("Chocolate"))