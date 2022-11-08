# Day 11 - Functions.
print()
# Funciones
"""
    Hasta ahora hemos visto muchas funciones integradas de Python. En esta sección, nos centraremos en las funciones personalizadas.
    Qué es una función? antes de comenzar a crear funciones, aprendamos qué es una función y por qué las necesitamos.
"""

# Definiendo una función.

"""
    Una función es un bloque de código reutilizable para sentencias programadas y diseñadas para realizar ciertas tareas.
    para declarar una función, Pyton dispone de la palabra clave "def". La siguiente es la syntaxis para definir una función.
    El bloque de código de la función se ejecuta solo si la función es llamada o invocada.
"""

# Declarando y llamando una función

"""
    Cuando hacemos una función, lo llamamos declarar una función. Cuando empezamos a utilizarla, lo llamamos 
    "calling" o "ivoking" una función. Una función puede ser declarada con o sin parámetros.
"""

# Syntax
def NombreDeFunción():          # Declarando una función
    None
NombreDeFunción()               # llamando a la función


# Función sin parámetros

def GeneraNombreCompleto():
    PrimerNombre = "Francisco"
    Apellido = "Orozco"
    Espacio = " "
    NombreCompleto = PrimerNombre + Espacio + Apellido
    print(NombreCompleto)

GeneraNombreCompleto()
print()


def AñadeDosNum():
    NumUno = 2
    NumDos = 3
    Total = NumUno + NumDos
    print(Total)
AñadeDosNum()
print()