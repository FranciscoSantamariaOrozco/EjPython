# Day 10 - Loops.
print()
# For anidado
# Puedes anidar distintos bucles for dentro de otros.
"""
    for x in y:
        for t in x:
            print(t)
"""
Persona = {
    "Nombre":"Francisco",
    "Apellido":"Orozco",
    "Edad":"34",
    "Pais":"Portugal",
    "Casado":False,
    "Skills":["Javascript", "React", "Node", "MongoDB", "Python"],
    "Direccion":{
        "Calle":"Av. Padre Manuel Nóbrega",
        "CP":"1000-223"
    }
}
for Key in Persona:
    print()
    print(Key)
    if Key == "Skills":
        for Skill in Persona["Skills"]:
            print(Skill)
print()