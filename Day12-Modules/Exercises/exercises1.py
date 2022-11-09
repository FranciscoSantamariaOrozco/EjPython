#Exercises - Day 12
print()

# 1- Escribe una función que genere un user_id aleatorio de 6 dígitos.
from random import randint

def RandomUserID():
    return randint(100000, 999999)

print(RandomUserID())