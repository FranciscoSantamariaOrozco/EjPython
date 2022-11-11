# Day 14 - List comprehension.
print()
# Higer Order Functions
"""
    Python permite que una función anidada acceda al ámbito exterior de la función que la encierra. Esto se conoce como Cierre.
    Veamos como funcionan los cierres en Python. En Python, los cierres se crean anidando una función dentro de otra función encapsuladora 
    y luego devolviendo la función interna. Veamos el siguiente ejemplo.
"""

def AddDiez():
    Diez = 10
    def Add(x):
        return x + Diez
    return Add

ResultadoCierre = AddDiez()
print(ResultadoCierre(5))
print(ResultadoCierre(10))
print()