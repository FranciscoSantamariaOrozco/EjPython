#Exercises - Day 9
print()

# L3-2- Aqui disponemos de un diccionario llamado "Persona". Sientete libre de modificarlo!

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

# Comprueba si en el diccionario esta la llave "Skills", si es así, comprueba también que exista la habiliad "Python". Imprime el resultado.

print("CONSULTA DE DICCIONARIOS (comprobación Python)\n")
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
        if "Python" in Francisco["Skills"]:
            print("Este usuario tiene conocimientos sobre Python.")
        else:
            print("Este usuario no tiene conocimientos de Python.")
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 2:
    if "Skills" in Paco:
        if "Python" in Paco["Skills"]:
            print("Este usuario tiene conocimientos sobre Python.")
        else:
            print("Este usuario no tiene conocimientos de Python.")
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 3:
    if "Skills" in Chest:
        if "Python" in Chest["Skills"]:
            print("Este usuario tiene conocimientos sobre Python.")
        else:
            print("Este usuario no tiene conocimientos de Python.")
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()