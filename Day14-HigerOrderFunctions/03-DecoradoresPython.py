# Day 14 - List comprehension.
print()
# Python decorators
"""
    Un decorador es un patrón de diseño en Python que permite al usuario añadir nuevas funcionalidades a un objeto existente
    sin modificar su estructura. A los decoradores habitualmente se les llama antes de la definición de la función que quieres decorar.
"""

# Creando decoradores
# Para crear un decorador para una función, necesitamos una función externa con una función envolvente interna.

def Saludo():
    return "Bienvenido a Python!"
def UppercaseDecorator(Funcion):
    def Envoltura():
        Func = Funcion()
        VolverMayusc = Func.upper()
        return VolverMayusc
    return Envoltura

G = UppercaseDecorator(Saludo)
print(G())
print()

# Implementemos el ejemplo anterior con un decorador

def UppercaseDecorator(Funcion):
    def Envoltura():
        Func = Funcion()
        VolverMayusc = Func.upper()
        return VolverMayusc
    return Envoltura

@UppercaseDecorator
def Saludo():
    return "Bienvenido a Python!"
print(Saludo())
print()

# Aplicar multiples decoradores a una sóla función

"""Primer decorador"""
def UppercaseDecorator(Funcion):
    def Envoltura():
        Func = Funcion()
        VolverMayusc = Func.upper()
        return VolverMayusc
    return Envoltura
"""Segundo decorador"""
def SplitStringDecorator(Funcion):
    def Envoltura():
        Func = Funcion()
        SplitString = Func.split()
        return SplitString
    return Envoltura

@SplitStringDecorator
@UppercaseDecorator         # el orden en los decoradores es importante en este caso - .upper() no funciona con listas.
def Saludo():
    return "Bienvenido a Python!"

print(Saludo())
print()

# Aceptando parametros en funciones de decorador.
# La mayor parte del tiempo necesitaremos que nuestras funciones tomen parámetros, para lo que necesitamos definir que el decorador acepte esos parámetros.

def DecoradorConParametros(Funcion):
    def EnvolturaAceptaParametros(Para1, Para2, Para3):
        Funcion(Para1, Para2, Para3)
        print("Yo vivo en {}".format(Para3))
    return EnvolturaAceptaParametros

@DecoradorConParametros
def NombreCompleto(Nombre, Apellido, Pais):
    print("Yo soy {} {}. Amo aprender Python.".format(Nombre, Apellido, Pais))

print(NombreCompleto("Francisco", "Orozco", "Portugal"))
print()