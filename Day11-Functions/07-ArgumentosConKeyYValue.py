# Day 11 - Funciones
print()
# Pasando argumentos con llave y valor
# Si pasamos argumentos con llave y valor, el orden de los argumentos no importa.

# Syntax
"""
    def NombreFuncion(para1, para2):
        codigo
        codigo
    print (NombreFuncion(Para1 = "John", para2 = "Doe"))        # El orden de los argumentos no importa aquí.
"""

def NombreCompleto(Nombre, Apellido):
    Espacio = " "
    NomComp = Nombre + Espacio + Apellido
    return NomComp
print(NombreCompleto(Apellido="Orozco", Nombre="Francisco"))
print()

def DosNumeros(Num1, Num2):
    Total = Num1 + Num2
    return Total
print(DosNumeros(Num2=5, Num1=2))
print()