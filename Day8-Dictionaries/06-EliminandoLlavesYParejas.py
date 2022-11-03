# Day 8 - Diccionarios.
print()
# Eliminar llaves y parejas e valores de un diccionario.
"""
    pop("llave"): Remueve el objeto con la llave epecificada.
    popitem(): Remueve el ultimo objeto.
    del: remueve el objeto con la llave especificada.
"""

# Syntax

Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
print("Diccionario original:", Diccionario)
Diccionario.pop("llave1")
print("Eliminamos la llave1 y su valor con Diccionario.pop(llave1):  ", Diccionario)
Diccionario.popitem()
print("Eliminamos la ultima llave con popitem():                     ", Diccionario)
del Diccionario["llave2"]
print("Eliminamos la llave dos con del Diccionario['llave2']:        ", Diccionario)
print()


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
print("Diccionario original:", Persona)
print()
Persona.pop("Nombre")
print("Eliminamos el nombre del diccionario:", Persona)
Persona.popitem()
print()
print("Ahora eliminamos el último item (Direccion) del diccionario:", Persona)
del Persona["Casado"]
print()
print("Por último eliminamos el estado civil:", Persona)
print()