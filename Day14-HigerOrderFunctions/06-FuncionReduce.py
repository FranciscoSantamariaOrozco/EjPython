# Day 14 - List comprehension.
print()
# Función reduce()
"""
    La función reduce() es definida en el módulo functools y deberíamos importarla desde este módulo.
    De una manera parecida a map() y filter(), toma dos parámetros, una función y un iterable. 
    Sin embargo, no devuelve otro iterable, si no que devuelve un único valor.
"""
from functools import reduce

NumerosString = ["1", "2", "3", "4", "5"]   # iterable
def SumDosNum(x, y):
    return int(x) + int(y)

Total = reduce(SumDosNum, NumerosString)
print(Total)
print()