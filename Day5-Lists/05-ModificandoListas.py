# Modificando listas.
# las listas son modificables. Vamos a probar:
print()

Fruits = ['banana', 'orange', 'mango', 'lemon']
Fruits[0] = 'avocato'
print(Fruits)
print()


# Comprobando los items de una lista
# Comprobar si un item es miembro de una lista utilizando el operador "in".
Fruits = ['banana', 'orange', 'mango', ' lemon']
DoesExist = 'banana' in Fruits
print(DoesExist)                # True
DoesExist = 'lime' in Fruits
print(DoesExist)                # False
print()


# Añadir items a una lista
# Para Añadir items al final de una lista existente podemos usar el método append()
print()
# lst = list()
# lst.append(item)
Fruits = ['banana', 'orange', 'mango', 'lemon']
Fruits.append('apple')
print(Fruits)                   # ['banana', 'orange', 'mango', 'lemon', 'apple']
Fruits.append('lime')
print(Fruits)                   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print()


# Insertar items en una lista
# Se puede usar el método insert() para insertar un item suelto en el index especificado en una lista.
# El resto de los items serán movidos hacia la derecha.
# El método insert() toma dos argumentos: index y el item a insertar.
Fruits = ['banana', 'orange', 'mango', 'lemon']
Fruits.insert(2, 'apple')       # Inserta apple entre orange y mango
print(Fruits)
Fruits.insert(3, 'lime')
print(Fruits)
print()