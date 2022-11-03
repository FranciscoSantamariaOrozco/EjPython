#Exercises - Day 8
print()

# 10- Elimina uno de los items del diccionario

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
print()
Estudiante.pop("estado civil")
print("Diccionario con la llave estado civil eliminada:", Estudiante)
print()