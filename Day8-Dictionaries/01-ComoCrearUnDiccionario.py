# Day 8 - Diccionarios.
print()
# Como crear un Diccionario.
"""
    Un diccionario es una colección de parejas de datos, desordenada y modificable.
"""

# Creando un diccionario
# Para crear un diccionario usamos los corchetes curvos, o la función dict()

# Syntax

DiccionarioVacio = {}
print("Esto es un diccionario vacío:", print(DiccionarioVacio))
DiccionarioConDatos = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
print("Este es un diccionario con datos:", DiccionarioConDatos)
print()

# Un diccionario puede contener los siguientes tipos de datos: String, booleano, lista, upla, set o diccionario.

Persona = {
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

print(Persona)
print()