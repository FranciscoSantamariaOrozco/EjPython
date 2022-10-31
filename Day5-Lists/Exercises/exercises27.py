#Exercises - Day 5
print()

# 27- Copia la lista en una variable llamada FullStack. Después inserta Python y SQL despues de redux.

FrontEnd = ["HTML", "CSS", "JavaScript", "React", "Redux"]
print("FrontEnd: ", FrontEnd)
BackEnd = ["Node", "Express", "MongoDB"]
print("BackEnd: ", BackEnd)
Fullstack = FrontEnd + BackEnd
print("Fullstack: ", Fullstack)
print("Añadiendo Python y SQL después de  Redux................")
Fullstack.insert(5, "Python")
print("Añadiendo Python...: ", Fullstack)
Fullstack.insert(6, "SQL")
print("Añadiendo SQL...: ", Fullstack)
print()