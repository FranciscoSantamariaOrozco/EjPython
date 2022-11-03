#Exercises - Day 9
print()

# L2-3- La sguiente lista contiene algunas frutas.
# Si una fruta no existe en la lista, añadela a la lista e imprime la lista modificada.
# Si la fruta existe, imprime ("Esta fruta ya existe en la lista")

Frutas = ["banana", "orange", "mango", "lemon"]
print("GESTOR DE LISTA DE FRUTAS\n")
NuevaFruta = input("Teclea la fruta a añadir:")
if NuevaFruta in Frutas:
    print("La fruta", NuevaFruta, "ya existe en la lista")
else:
    Frutas.append(NuevaFruta)
    print("La fruta", NuevaFruta, "Ha sido correctamente añadida a la lista:\n",Frutas)
print()