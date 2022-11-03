#Exercises - Day 9
print()

# 2- Compara los valores de "MiEdad" y "TuEdad" usando if y else. Quien es mayor de los dos? 
# Usa input() para introducir la edad.
# Tu puedes usar condicionales anidados para imprimir distintos mensajes para 1 año de diferencia en la edad,
# "años" para diferencias mas grandes, y un mensaje personalizado si los dos tenemos la misma edad.

MyAge = 34
UserAge = input("Introduce tu edad:")
UserAge = int(UserAge)
if UserAge == MyAge:
    print("Somos de la misma quinta!")
elif UserAge == MyAge + 1:
    print("Sólo eres un año mayor que yo!")
elif UserAge == MyAge -1:
    print("Sólo eres un año menor que yo!")
elif UserAge > MyAge:
    print("Eres", UserAge - MyAge, "años mayor que yo")
else:
    print("Eres", MyAge - UserAge, "años mas pequeño que yo")