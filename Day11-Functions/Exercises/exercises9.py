#Exercises - Day 11
print()

# 9- Declara una función que se llame ListaReversa. Tomará un array como parámetro y devolverá el array a la inversa (usa bucles).

ListaFrutas = ["Manzana", "Pera", "Kiwi", "Platano", "Naranja"]
TuplaItems = ("Item1", "Item2", "Item3", "Item4")

def ListaReversa(Array):
    LisInv = []
    i = len(Array)-1
    while i > -1:
        LisInv.append(Array[i])
        i = i -1
    return LisInv
print(ListaReversa(ListaFrutas))
print()
print(ListaReversa(TuplaItems))
print()