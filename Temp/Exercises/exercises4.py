#Exercises - Day 11
print()

# 4- La temperatura en ºC puede ser convertida a ºF usando la siguiente formula: 
# ºF = (ºC x 9/5) + 32.
# Escribe una función que convierta los grados Celsius en Farenheit.

def CelsiusAFarenheit(Celsius):
    Farenheit = (Celsius * 9/5) + 32
    return Farenheit
print(CelsiusAFarenheit(20))
print()