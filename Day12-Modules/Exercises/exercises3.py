#Exercises - Day 12
print()

# 3- Escribe na función llamada ColorGen. Debe generar colores rgb (tres valores entre el 0 y el 255)
from random import randint

def ColorGen():
    RGB = ""
    for i in range(3):
        if i == 0:
            Num = randint(1,255)
            Num = str(Num)
            RGB = RGB + Num
        else:
            Num = randint(1,255)
            Num = str(Num)
            RGB = RGB + "," + Num        
    print("rgb = (", RGB, ")")

print(ColorGen())