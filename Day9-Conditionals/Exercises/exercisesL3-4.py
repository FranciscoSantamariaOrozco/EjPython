#Exercises - Day 9
print()

# L3-4- Si la persona esta casada y vive en España, imprime la siguiente información en el siguiente formato:
"""
        Asabeneh Yetayeh lives in Finland. He is married.
        %Nombre% %apellido% vive en %pais%. Está casado/a.
"""

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
    if "Pais" in Francisco and "Casado" in Francisco:
        if "España" in Francisco["Pais"] and Francisco["Casado"] is True:
            print(Francisco["Nombre"] , Francisco["Apellido"], "Vive en", Francisco["Pais"], "y está casado/a.")
            print()
        else:
            print("Esta persona no se encuentra en España o no esta casado/a.")
            print()
    else:
        print("No tenemos datos sobre su país o estado civil.")
        print()
elif Diccionario == 2:
    if "Pais" in Paco and "Casado" in Paco:
        if "España" in Paco["Pais"] and Paco["Casado"] is True:
            print(Paco["Nombre"] , Paco["Apellido"], "Vive en", Paco["Pais"], "y está casado/a.")
            print()
        else:
            print("Esta persona no se encuentra en España o no esta casado/a.")
            print()
    else:
        print("No tenemos datos sobre su país o estado civil.")
        print()
elif Diccionario == 3:
    if "Pais" in Chest and "Casado" in Chest:
        if "España" in Chest["Pais"] and Chest["Casado"] is True:
            print(Chest["Nombre"] , Chest["Apellido"], "Vive en", Chest["Pais"], "y está casado/a.")
            print()
        else:
            print("Esta persona no se encuentra en España o no esta casado/a.")
            print()
    else:
        print("No tenemos datos sobre su país o estado civil.")
        print()
elif Diccionario == 4:
    if "Pais" in Leal and "Casado" in Leal:
        if "España" in Leal["Pais"] and Leal["Casado"] is True:
            print(Leal["Nombre"] , Leal["Apellido"], "Vive en", Leal["Pais"], "y está casado/a.")
            print()
        else:
            print("Esta persona no se encuentra en España o no esta casado/a.")
            print()
    else:
        print("No tenemos datos sobre su país o estado civil.")
        print()
elif Diccionario == 5:
    if "Pais" in Zoraida and "Casado" in Zoraida:
        if "España" in Zoraida["Pais"] and Zoraida["Casado"] is True:
            print(Zoraida["Nombre"] , Zoraida["Apellido"], "Vive en", Zoraida["Pais"], "y está casado/a.")
            print()
        else:
            print("Esta persona no se encuentra en España o no esta casado/a.")
            print()
    else:
        print("No tenemos datos sobre su país o estado civil.")
        print()
else:
    print()