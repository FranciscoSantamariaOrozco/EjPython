#Exercises - Day 12
print()

# 2- Modifica la tarea anterior. Declara una funci]on llamada UserIDGenByUser. No debe tomar ningún parámetro, pero toma dos entradas usando input.
# Uno de los imputs será el número de caracteres, y el segundo input sera el número de IDs que queremos generar.

from random import choice
from string import ascii_letters, digits
Characters = ascii_letters + digits
def UserIDGenByUser():
    width = input("Introduce la longitud de caracteres de las IDs: ")
    width = int(width)
    NumIDs = input("Introduce el número de IDs a generar: ")
    NumIDs = int(NumIDs)
    print()
    for i in range(NumIDs):
        ID = "#"
        for i2 in range(width):
            RandomNum = choice(Characters)
            RandomNum = str(RandomNum)
            ID = ID + RandomNum
        print("ID número", i, ":", ID)    

print(UserIDGenByUser())

"""
from random import randint

def UserIDGenByUser():
    width = input("Introduce la longitud de caracteres de las IDs: ")
    width = int(width)
    NumIDs = input("Introduce el número de IDs a generar: ")
    NumIDs = int(NumIDs)
    for i in range(NumIDs):
        ID = []
        for i2 in range(width):
            ID.append(randint(1,9))
        print(ID)
print(UserIDGenByUser())
"""