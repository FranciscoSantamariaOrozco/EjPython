# Day 4 Listas
# Como crear una lista.
print()

# Usando una funcion built-in 
lst = list()

EmptyList = list()      # Esto es una lista vacía, no hay items en ella.
print(len(EmptyList))

# Usando los corchetes cuadrados
lst = []

EmptyList = []      # Lista vacía.
print(len(EmptyList))
print()

# Haz unas listas con los siguientes valores. Luego utiliza la función len() para ver la longitud de las listas.
Frutas = ["Banana", "Orange", "Mango", "Lemon"]
Vegetales = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
ProductosAnimales = ["Milk", "Meat", "Butter", "Yoghurt"]
WebTech = ["HTML", "CSS", "JS", "React", "Redux", "Node", "MongoDB"]
Paises = ["Finland", "Estonia", "Denmark", "Sweden", "Norway"]

# Print a las listas y a su longitud
print("Frutas: ", Frutas)
print("Número de frutas: ", len(Frutas))
print("Vegetales: ", Vegetales)
print("Número de vegetales: ", len(Vegetales))
print("Productos Animales: ", ProductosAnimales)
print("Número de productos animales: ", len(ProductosAnimales))
print("Tecnologías Web: ", WebTech)
print("Número de tecnologías web: ", len(WebTech))
print("Países: ", Paises)
print("Número de países: ", len(Paises))
print()

# Las listas pueden contener diferentes tipos de datos
lst = ["Francisco", 250, True, {"Country":"Finland", "City":"Helsinki"}]
print(lst)
print(len(lst))