# Day 8 - Diccionarios.
print()
# Accediendo a los items del diccionario.
# Podemos acceder a los items del diccionario haciendo referencia a su llave.

Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
print("El valor de la llave1 es:", Diccionario["llave1"])
print("El valor de la llave4 es:", Diccionario["llave4"])
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
print(Persona["Nombre"])
print(Persona["Pais"])
print(Persona["Skills"])
print(Persona["Skills"][0])
print(Persona["Direccion"]["Calle"])
#print(Persona["Ciudad"])            # ERROR
                                    # Traceback (most recent call last):
                                    #   File "c:\Users\Francisco.Orozco\Documents\Programacion\EjPython\Day8-Dictionaries\02-AccediendoItemsDelDiccionario.py", line 29, in <module>
                                    #     print(Persona["Ciudad"])           # ERROR
                                    # KeyError: 'Ciudad'
print()


# Acceder a un item por su llave genera un error en caso de que esa llave no exista. Para evitar este error,
# primero debemos verificar si existe la clave. Podemos usar para esto el método get.
# El método get devuelve None si no existe la llave, que es un tipo de datos de objeto NoneType.


print(Persona.get("Nombre"))
print(Persona.get("Pais"))
print(Persona.get("Skills"))
print(Persona.get("Ciudad"))    # Aquí indicara none, ya que la llave "Ciudad" no existe en el diccionario.
print()