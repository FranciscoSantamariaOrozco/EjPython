#Exercises - Day 8
print()

# 11- Elimina uno de los diccionarios.

Estudiante = {}
Estudiante["nombre"] = "Francisco"
Estudiante["apellido"] = "Orozco"
Estudiante["genero"] = "Hombre"
Estudiante["edad"] = "34"
Estudiante["estado civil"] = "Soltero"
Estudiante["habilidades"] = ["HTML", "CSS", "Javascript", "Python", "Bash"]
Estudiante["pais"] = "Portugal"
Estudiante["ciudad"] = "Lisboa"
print("Diccionario original:", Estudiante)
del Estudiante          
#print(Estudiante)      # Error
                        # Traceback (most recent call last):
                        #   File "c:\Users\Francisco.Orozco\Documents\Programacion\EjPython\Day8-Dictionaries\Exercises\exercises11.py", line 17, in <module>
                        #     print(Estudiante)
                        # NameError: name 'Estudiante' is not defined
print()