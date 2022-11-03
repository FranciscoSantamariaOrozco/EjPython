#Exercises - Day 9
print()

# L3-1- Aqui disponemos de un diccionario llamado "Persona". Sientete libre de modificarlo!

Francisco = {
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
Paco = {
    "Nombre":"Paco",
    "Apellido":"EresDios",
    "Edad":"30",
    "Pais":"España",
    "Casado":True,
    "Skills":["Barman", "Laboratorio", "Cachondo Mental", "Master de rol", "Amigo"],
    "Direccion":{
        "Calle":"Enfesta de San Telmo, 6",
        "CP":"36002"
    }
}
Chest = {
    "Nombre":"Chest",
    "Apellido":"Merlo",
    "Edad":"32",
    "Pais":"España",
    "Casado":False,
    "Direccion":{
        "Calle":"Echegaray",
        "CP":"36002"
    }
}

# Comprueba si en el diccionario esta la llave "Skills", si es así, imprima la habilidad intermedia de la lista.

print("CONSULTA DE DICCIONARIOS (Consulta de Skills)\n")
print("Que diccionario deseas consultar?\n1-Francisco\n2-Paco\n3-Chest\n")

Diccionario = input("Introduce el número de diccionario a consultar:")
Diccionario = int(Diccionario)

if Diccionario > 3:
    print("El registro de diccionario no existe")
    print()
elif Diccionario < 1:
    print("El registro de diccionario no existe")
    print()
elif Diccionario == 1:
    if "Skills" in Francisco:
        print("Habilidad intermedia:", Francisco["Skills"][len(Francisco) // 2])
        print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 2:
    if "Skills" in Paco:
        print("Habilidad intermedia:", Paco["Skills"][len(Paco) // 2])
        print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 3:
    if "Skills" in Chest:
        print("Habilidad intermedia:", Chest["Skills"][len(Chest) // 2])
        print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()