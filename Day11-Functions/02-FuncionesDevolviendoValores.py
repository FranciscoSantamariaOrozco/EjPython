# Day 11 - Functions.
print()
# Funciones devolviendo valores
"""
    Las funciones también pueden devolver valores, Si la función no tiene declarado un return, el valor de la función es None.
    Reescribamos las funciones anteriores usando return. De ahora en adelante, obtenemos un valor de una función cuando llamamos 
    a la función y la imprimimos.
"""
def GeneraNombre():
    Nombre = "Francisco"
    Apellido = "Orozco"
    Espacio = " "
    NombreCompleto = Nombre + Espacio + Apellido
    return(NombreCompleto)
print(GeneraNombre())
print()

def DosNums():
    NumUno = 5
    NumDos = 3
    Total = NumUno + NumDos
    return(Total)
print(DosNums())
print()