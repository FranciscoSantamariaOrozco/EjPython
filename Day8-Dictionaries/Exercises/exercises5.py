#Exercises - Day 8
print()

# 5- Obtén el valor del campo habilidades, y comprueba su tipo de datos. Debe ser una lista.

Estudiante = {}
Estudiante["nombre"] = "Francisco"
Estudiante["apellido"] = "Orozco"
Estudiante["genero"] = "Hombre"
Estudiante["edad"] = "34"
Estudiante["estado civil"] = "Soltero"
Estudiante["habilidades"] = ["HTML", "CSS", "Javascript", "Python", "Bash"]
Estudiante["pais"] = "Portugal"
Estudiante["ciudad"] = "Lisboa"
Values = Estudiante["habilidades"]
print("La lista de habilidades del estudiante es:", Values)
print("Y el tipo de dato de Values es:", type(Values))
print()