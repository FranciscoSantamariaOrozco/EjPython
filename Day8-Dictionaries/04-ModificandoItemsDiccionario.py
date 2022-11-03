# Day 8 - Diccionarios.
print()
# Modificando items de un diccionario.
# Podemos modificar items de un diccionario de la siguiente manera.

# Syntax

Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
print("Diccionario original:", Diccionario)
Diccionario["llave1"] = "valor-uno"
print("Diccionario modificado:", Diccionario)
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
print("Datos originales:", Persona)
Persona["Nombre"] = "Fran"
Persona["Edad"] = "35"
print()
print("Datos modificados:", Persona)
print()