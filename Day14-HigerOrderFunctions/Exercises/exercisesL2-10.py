#Exercises - Day 13
print()

# L2-10 - Usa reduce para sumar todos los números en la lista números.
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def SumDosNum(x, y):
    return int(x) + int(y)

Suma = reduce(SumDosNum, numbers)
print(Suma)