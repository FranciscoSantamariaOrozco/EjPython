# Day 12 - Modules.
print()
# Importando módulos incorporados.
"""
    Como en otros lenguajes de programación, también podemos importar módulos importando el archivo o función usando la palabra clave "import".
    Importaremos el módulo común que usaremos la mayor parte del tiempo. Algunos de los módulos incorporados comunes: Matemáticas, fecha y hora, os, sys,
    aleatorio, estadísticas, colecciones, json, re....
"""

# OS module
"""
   Usando el módulo Python os, es posible realizar automáticamente muchas tareas del sistema operativo.
   El módulo del SO de Python proporciona funciones para crear, cambiar el directorio de trabajo actual y eliminar un directorio (carpeta), 
   recuperar su contenido, cambiar e identificar el directorio actual. 
"""

import os
print(os.getcwd())
os.mkdir("Carpetaprueba")
os.chdir(".\Carpetaprueba")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.rmdir("Carpetaprueba")