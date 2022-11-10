#Exercises - Day 12
print()

# L3-1 - Crea una función llamada MezclarLista, que tome una lista como parámetro y devuelva la lista desordenada.
from random import randint

Frutas = ["Manzana", "Pera", "Kiwi", "Platano", "Naranja"]
Persona = ["Francisco", "Orozco", 34, True, {"Habilidades":"Python"} ]

def MezclarLista(Lista):
    print("Lista original: ", Lista)
    for i in range(len(Lista)):
        Mezcla = Lista[i]
        Lista.remove(Mezcla)
        Lista.insert(randint(0,len(Lista)), Mezcla)
    print(Lista)
print(MezclarLista(Persona))