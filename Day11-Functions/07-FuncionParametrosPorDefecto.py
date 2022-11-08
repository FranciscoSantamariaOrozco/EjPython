# Day 11 - Funciones
print()
# A veces podemos pasar valores por defecto para las funciones. Cuando invocaos la función, si no le facilitamos argumentos al llamarla, 
# los valores por defecto son utilizados.

# Syntax
"""
    def NombreFuncion(parametro = value):
        codigo
        codigo
    NombreFuncion()
    NombreFuncion(arg)
"""

def Saludo(Nombre = "Peter"):
    Mensaje = Nombre + " Welcome to Python for everyone!"
    return Mensaje
print(Saludo())
print()
print(Saludo("Francisco"))
print()

def CalcularEdad(Fnac, Fact = 2022):
    Edad = Fact - Fnac
    return Edad
print(CalcularEdad(1988))
print()

def PesoObjeto(Masa, Gravedad = 9.81):          
    Peso = str(Masa * Gravedad) + " N"
    return Peso
print(PesoObjeto(100))                      # Peso en la superficie terrestre.
print(PesoObjeto(100, 1.62))                # Peso en la luna 
print()