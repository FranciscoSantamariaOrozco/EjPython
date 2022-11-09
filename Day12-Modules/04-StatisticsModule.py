# Day 12 - Modules.
print()
# Statistics Module
"""
    El módulo estadísticas provee funciones para estadística matematica de datos numéricos. Las funciones estadísticas mas populares
    vienen definidas en este módulo: mean, median, mode, stdev....
"""

from statistics import *                # Importa todos los módulos
Edades = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(Edades))
print(median(Edades))
print(mode(Edades))
print(stdev(Edades))