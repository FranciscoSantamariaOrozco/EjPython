#Exercises - Day 6
print()

# 5- Modifica la tupla TodosLosHermanos y añade el nombre d etu padre y de tu madre, y asignalo a "Familia".

Hermanos = ('Chest', 'Sergio', 'Paco')
Hermanas = ('Leal', 'María', 'Almudena')
TodosLosHermanos = Hermanos + Hermanas

# Sumando tuplas
print("Tenemos la tupla TodosLosHermanos:", TodosLosHermanos)
Padres = ("Rosa", "Arturo")
print("Creamos la tupla Padres:", Padres)
Familia = TodosLosHermanos + Padres
print("Y sumamos las tuplas TodosLosHermanos y Padres en la tupla Familia:", Familia)
print()


# Otra manera 
print("Otra manera de hacerlo, convirtiendolo a una lista y añadiendo los elementos:")
print()
print("Tupla original:", TodosLosHermanos)
TodosLosHermanos = list(TodosLosHermanos)
print("La convertimos a lista:", TodosLosHermanos)
TodosLosHermanos.append("Rosa")
TodosLosHermanos.append("Arturo")
print("añadimos elementos", TodosLosHermanos)
Familia = TodosLosHermanos
print("Modificamos la lista TodosLosHermanos por Familia:", Familia)
Familia = tuple(Familia)
print("Convertimos Familia en una tupla:", Familia)
print()