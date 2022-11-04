#Exercises - Day 9
print()

# L3-3- Si la persona tiene entre sus skills Javascript y react, imprime "Este usuario es un FrontEnd developer."
# Si la persona tiene entre sus skills Node, Python y MongoDB, imprime "Este usuario es un BackEnd developer."
# Si la persona tiene entre sus skills React, Node y MongoDB, imprime "Este usuario es un FullStack developer."
# Se puede ser mas preciso anidando más condicionales!!!!

#Bibliotecas
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
    "Skills":["Javascript", "React", "Barman", "Laboratorio", "Cachondo Mental", "Master de rol", "Amigo"],
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
    "Skills":["Node", "Python", "MongoDB", "Aspi", "Master de rol", "Bro"],
    "Direccion":{
        "Calle":"Echegaray",
        "CP":"36002"
    }
}
Leal = { 
    "Nombre":"Leal",
    "Apellido":"Pereira",
    "Edad":"34",
    "Pais":"España",
    "Casado":False,
    "Skills":["Deportes", "Idiomas", "Moda","Eventos"],
    "Direccion":{
        "Calle":"Eduardo Pondal",
        "CP":"36001"
    }
}
Zoraida = { 
    "Nombre":"Zoraida",
    "Apellido":"Regueira",
    "Edad":"32",
    "Pais":"España",
    "Casado":True,
    "Direccion":{
        "Calle":"Eduardo Pondal",
        "CP":"36001"
    }
}

# Menú
print("CONSULTA DE DICCIONARIOS (comprobación Python)\n")
print("Que diccionario deseas consultar?\n1-Francisco\n2-Paco\n3-Chest\n4-Leal\n5-Zoraida\n")

Diccionario = input("Introduce el número de diccionario a consultar:")
Diccionario = int(Diccionario)

# Código
#
# Excluyentes
if Diccionario > 5:
    print("El registro de diccionario no existe")
    print()
elif Diccionario < 1:
    print("El registro de diccionario no existe")
    print()

# Diccionarios
elif Diccionario == 1:
    if "Skills" in Francisco:
        if "React" in Francisco["Skills"] and "Node" in Francisco["Skills"] and "MongoDB" in Francisco["Skills"]:
            print("Este usuario es fullstack developer.")
            print()
        elif "React" in Francisco["Skills"] and "Javascript" in Francisco["Skills"]:
            print("Este usuario es FrontEnd developer.")
            print()
        elif "Node" in Francisco["Skills"] and "Python" in Francisco["Skills"] and "MongoDB" in Francisco["Skills"]:
            print("Este usuario es BackEnd developer.")
            print()
        else:
            print("Este usuario no cuenta con la habilidades TI suficientes")
            print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 2:
    if "Skills" in Paco:
        if "React" in Paco["Skills"] and "Node" in Paco["Skills"] and "MongoDB" in Paco["Skills"]:
            print("Este usuario es fullstack developer.")
            print()
        elif "React" in Paco["Skills"] and "Javascript" in Paco["Skills"]:
            print("Este usuario es FrontEnd developer.")
            print()
        elif "Node" in Paco["Skills"] and "Python" in Paco["Skills"] and "MongoDB" in Paco["Skills"]:
            print("Este usuario es BackEnd developer.")
            print()
        else:
            print("Este usuario no cuenta con la habilidades TI suficientes")
            print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 3:
    if "Skills" in Chest:
        if "React" in Chest["Skills"] and "Node" in Chest["Skills"] and "MongoDB" in Chest["Skills"]:
            print("Este usuario es fullstack developer.")
            print()
        elif "React" in Chest["Skills"] and "Javascript" in Chest["Skills"]:
            print("Este usuario es FrontEnd developer.")
            print()
        elif "Node" in Chest["Skills"] and "Python" in Chest["Skills"] and "MongoDB" in Chest["Skills"]:
            print("Este usuario es BackEnd developer.")
            print()
        else:
            print("Este usuario no cuenta con la habilidades TI suficientes")
            print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 4:
    if "Skills" in Leal:
        if "React" in Leal["Skills"] and "Node" in Leal["Skills"] and "MongoDB" in Leal["Skills"]:
            print("Este usuario es fullstack developer.")
            print()
        elif "React" in Leal["Skills"] and "Javascript" in Leal["Skills"]:
            print("Este usuario es FrontEnd developer.")
            print()
        elif "Node" in Leal["Skills"] and "Python" in Leal["Skills"] and "MongoDB" in Leal["Skills"]:
            print("Este usuario es BackEnd developer.")
            print()
        else:
            print("Este usuario no cuenta con la habilidades TI suficientes")
            print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()
elif Diccionario == 5:
    if "Skills" in Zoraida:
        if "React" in Zoraida["Skills"] and "Node" in Zoraida["Skills"] and "MongoDB" in Zoraida["Skills"]:
            print("Este usuario es fullstack developer.")
            print()
        elif "React" in Zoraida["Skills"] and "Javascript" in Zoraida["Skills"]:
            print("Este usuario es FrontEnd developer.")
            print()
        elif "Node" in Zoraida["Skills"] and "Python" in Zoraida["Skills"] and "MongoDB" in Zoraida["Skills"]:
            print("Este usuario es BackEnd developer.")
            print()
        else:
            print("Este usuario no cuenta con la habilidades TI suficientes")
            print()
    else:
        print("Este usuario no tiene ninguna habilidad.")
        print()