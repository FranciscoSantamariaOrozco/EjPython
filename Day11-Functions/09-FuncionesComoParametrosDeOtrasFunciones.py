# Day 11 - Funciones
print()
# Funciones como parámetro de otras funciones

def NumeroAlCuadrado(Numero):
    return Numero* Numero
def HazAlgo(f,x):
    return f(x)
print(HazAlgo(NumeroAlCuadrado, 3))
print()