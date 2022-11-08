#Exercises - Day 11
print()

# 2- El área de un circulo se calcula de la siguiente manera: PI * r * r. Escribe una función que calcule el área de un circulo dando el radio.

def AreaCirc(Radio):
    NumPi = 3.1416
    Area = NumPi * (Radio * Radio)
    return Area
print(AreaCirc(5))
print()