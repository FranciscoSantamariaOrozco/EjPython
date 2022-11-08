#Exercises - Day 11
print()

# 9- Declara una función que se llame ListaReversa. Tomará un array como parámetro y devolverá el array a la inversa (usa bucles).

ListaFrutas = ["Manzana", "Pera", "Kiwi", "Platano", "Naranja"]
SetProgramacion = {"Python", "HTML", "CSS", "JavaScript", "Java"}
#TuplaItems = ("Item1", "Item2", "Item3", "Item4")
DiccionarioPersona = {
    "Nombre":"Francisco",
    "Apellido":"Orozco",
    "Edad":"34",
    "Pais":"Portugal",
    "Casado":False,
    "Skills":["Javascript", "React", "Node", "MongoDB", "Python"],
    "Direccion":{
        "Calle":"Av. Padre Manuel Nóbrega",
        "CP":"1000-223"
    }
}

def ListaReversa(Array):
    i = len(Array)
    while i > 0:
        print(Array[i])
        i = i -1
    return None
print(ListaReversa(ListaFrutas))
print()
print(ListaReversa(SetProgramacion))
print()
#print(ListaReversa(TuplaItems))
print()
print(ListaReversa(DiccionarioPersona))
print()