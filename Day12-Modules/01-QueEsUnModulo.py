# Day 12 - Modules.
print()
# Qué es un módulo
"""
    Un módulo es un archivo que contiene un set de códigos o de funciones que pueden ser incluidos en la aplicación. Un modulo puede ser un archivo que
    contenga una simple variable, una función o una gran base de código.
"""

# Creando un módulo
"""
    Para crear un módulo  debemos escribir nuestro código en Python, y guardar el archivo con la extensión .py
    Crea un archivo llamado mymodule.py dentro de tu proyecto. Nosotros lo vamos a hacer dentro de una carpeta aparte llamada "Modules".
    Vamos a escribir algo de codigo en ese archivo.

# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

"""

# Importando un módulo.
# Para importar un modulo sólo tenemos que utilizar la palabra clave "import" y el nombre del archivo.

import mymodule
print(mymodule.generate_full_name("Francisco", "Orozco"))

# Importando funciones de un módulo.
# Podemos tener varias funciones en un archivo e importarlas aparte unas de otras.

from mymodule import generate_full_name, sum_two_nums, gravity, Persona
print(generate_full_name("Francisco", "Orozco"))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(Persona["Nombre"])

# Importando funciones de un módulo y renombrandolo
# Durante la importación podemos renombrar los módulos.

from mymodule import generate_full_name as fullname, sum_two_nums as total, Persona as p, gravity as g
print(fullname("Francisco", "Orozco"))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p["Nombre"])