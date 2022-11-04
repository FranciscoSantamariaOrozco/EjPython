# Day 10 - Loops.
print()
# For Loop
# Con la palabra clave "for" podemos crear un bucle for, similar al de otros lenguajes de programación, 
# pero con algunas diferencias sintácticas.
# El bucle for se utiliza para iterar por una secuencia (Como una lista, tupla, diccionario, set o string)

# Bucle for con listas
"""
    for iterador in lista
        código
"""
Numeros = [1, 2, 3, 4, 5]
for Numero in Numeros:
    print(Numero)
print()


# Bucle for con strings
# Se puede iterar a lo largo de una string, para, por ejemplo, ir imprimiendo letra a letra.
"""
    for iterador in string:
        código
"""
Lenguaje = "Python"
for Letra in Lenguaje:
    print(Letra)
print()

# Otra manera. Aquí jugamos con la función len.
for i in range(len(Lenguaje)):
    print(Lenguaje[i])
print()


# Bucle for con tuplas
"""
    for iterador in tupla:
        codigo
"""
Numeros = (0, 1, 2, 3, 4, 5)
for i in Numeros:
    print(i)
print()


# Bucle for con diccionarios
# El bucle for con diccionarios recorre el diccionario a lo largo de sus keys.
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
for i in Persona:
    print(i, " - ", Persona[i])
print()


# Bucle for con sets
"""
for iterador in set:
    codigo
"""
IT_Companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for Company in IT_Companies:
    print(Company)
print()