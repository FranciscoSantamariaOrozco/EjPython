#Exercises - Day 11
print()

# 10- Declara unfa función llamada "ListaEnMayusc". Tomará una lista como parámetro y devolverá una lista de los items en Mayusc.

def ListaEnMayusc(*Array):
    ListMayusc = []
    for i in Array:
        ListMayusc.append(i.upper())
    return ListMayusc
print(ListaEnMayusc("Pomelo", "Manzana", "Tomate", "Plátano", "Pera", "Naranja"))
print()