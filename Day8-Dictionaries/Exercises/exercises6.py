#Exercises - Day 8
print()

# 6- Modifica los valores de habilidades, añadiendo una o dos habilidades nuevas.

Estudiante = {}
Estudiante["nombre"] = "Francisco"
Estudiante["apellido"] = "Orozco"
Estudiante["genero"] = "Hombre"
Estudiante["edad"] = "34"
Estudiante["estado civil"] = "Soltero"
Estudiante["habilidades"] = ["HTML", "CSS", "Javascript", "Python", "Bash"]
Estudiante["pais"] = "Portugal"
Estudiante["ciudad"] = "Lisboa"
print("Estas son las habilidades del estudiante:", Estudiante["habilidades"])
Estudiante["habilidades"].append("React")
Estudiante["habilidades"].append("NodeJS")
print("Hemos añadido React y NodeJS a sus habilidades:", Estudiante["habilidades"])
print()