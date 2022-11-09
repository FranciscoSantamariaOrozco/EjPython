# Day 12 - Modules.
print()
# Sys module
"""
    El módulo sys provee de funciones y variables usadas para manipular diferentes partes del entorno de ejecución de Python. La función sys.argv
    devuelve una lista de argumentos de la linea de comandos pasados a un script de Python. El elemento en el índice 0 de esta lista siempre es el 
    nombre del script, en el índice 1 stá el argumento pasado desde la línea de comando.
"""

import sys
#print(sys.argv[0], sys.argv[1], sys.argv[2])
print("Bienvenido {}. Disfruta del desafío {}".format(sys.argv[1], sys.argv[2]))
# Ahora escribe desde la linea de comandos:
"""
    python script.py Francisco 30diasdePython

Resultado:
    Bienvenido Francisco. Disfruta del desafío 30diasdePython
"""

# Otros comandos útiles del módulo sys:
# Para salir de sys
sys.exit()
# Para conocer la variable entera más grande que se necesita
sys.maxsize
# Para conocer el path del entorno:
sys.path
# Para conocer la versión de python que usas:
sys.version