# Buscando y ordenando listas.
print()
# Contar items
# El método count() devuelve el numero de veces que un item aparece en una lista.

Fruits = ['banana', 'orange', 'mango', 'lemon']
print(Fruits.count('orange'))               # 1
Ages = [22,19,24,25,26,24,25,24]
print(Ages.count(24))                       # 3
print()



# Localizar un item de la lista
# El método index() devuelve el valor del index de un elemento concreto de la lista.

Fruits = ['banana', 'orange', 'mango', 'lemon']
print("Lista ordenada: ", Fruits)
Fruits.reverse()
print("Lista a la inversa: ", Fruits)
print()

Ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("Edades: ", Ages)
Ages.reverse()
print("Edades invers.: ", Ages)
print()



# Ordenando items
# Para ordenar listas podemos utilizar el método sort() o sorted().
# El método sort reordena los elementos de la lista en orden ascendente, y modifica la lista original.
# Si lleva un argumento de reverse igual a verdadero, ordenará la lista en orden descendente.

Fruits = ['banana', 'orange', 'mango', 'lemon']
print("Lista de frutas: ", Fruits)
Fruits.sort()
print("Lista ordenada: ", Fruits)
Fruits.sort(reverse=True)
print("Lista des. inversa: ", Fruits)
print()
Ages = [22, 19, 24, 25, 26, 24, 25, 24]
Ages.sort()
print(Ages)
print()

# Con sorted()
# Devuelve la lista ordenada sin modificar la original

Fruits = ['banana', 'orange', 'mango', 'lemon']
print("Lista de frutas ordenada: ", sorted(Fruits))
# Reverse order:
print("Lista de frutas ord. invers.: ", sorted(Fruits,reverse=True))
print("Lista original: ", Fruits)
print()


# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]