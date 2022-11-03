#Exercises - Day 9
print()

# L2-1- Escribe un código que devuelva un grado a los estudiantes segun la nota que introduzcan:
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

Nota = input("Introduce tu nota del 0 al 100:")
Nota = int(Nota)
if Nota > 100:
    print("Error, no puedes sacar mas de 100 puntos.")
elif Nota < 0:
    print("Error, no puedes sacar menos de 0.")
elif Nota < 50:
    print("Has suspendido 'F' con un", Nota)
elif Nota < 60:
    print("Has aprobado, tienes un 'D' con tus", Nota, "puntos.")
elif Nota < 70:
    print("Has aprobado, tienes un 'C' con tus", Nota, "puntos.")
elif Nota < 90:
    print("Has aprobado, tienes un 'B' con tus", Nota, "puntos.")
else:
    print("Has aprobado, tienes un 'A' con tus", Nota, "puntos.")
print()