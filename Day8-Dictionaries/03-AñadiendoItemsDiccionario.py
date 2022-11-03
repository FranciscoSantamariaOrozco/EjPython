# Day 8 - Diccionarios.
print()
# Añadiendo items al diccionario
# Podemos añadir nuevas llaves o parejas de valores a un diccionario.

# Syntax

Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
print("Diccionario original:", Diccionario)
Diccionario["llave5"] = "valor5"
print("Diccionario con registro añadido:", Diccionario)
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
Persona["Trabajo"] = "Informático"
Persona["Skills"].append("HTML")
print(Persona)
print()