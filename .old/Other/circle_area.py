# Ejercicio para cálculo del area de un círculo 
# (en metros).

from math import pi

print()
print("introduce el radio del círculo en metros:")
radio = int(input())
area = pi * (radio * radio)
print("el area de un círculo de", radio, "m de radio es:", (area), "metros.")
print()


circunferencia = (2 * pi * radio)
print("la circunferencia de un círculo de ", radio, "m de radio es:", circunferencia, "metros.")
print