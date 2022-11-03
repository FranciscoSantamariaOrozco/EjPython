#Exercises - Day 8
print()

# 8- Obten la lista de valores del diccionario.

Estudiante = {}
Estudiante["nombre"] = "Francisco"
Estudiante["apellido"] = "Orozco"
Estudiante["genero"] = "Hombre"
Estudiante["edad"] = "34"
Estudiante["estado civil"] = "Soltero"
Estudiante["habilidades"] = ["HTML", "CSS", "Javascript", "Python", "Bash"]
Estudiante["pais"] = "Portugal"
Estudiante["ciudad"] = "Lisboa"
Values = Estudiante.values()
print("La lista de valores del diccionario es:", Values)
print()