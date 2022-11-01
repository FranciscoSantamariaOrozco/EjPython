# Day 6 - Tuplas
print()
# Cambiando Tuplas a listas.
# Podemos cambiar una tupla a una lista y una lista a una tupla. La tupla es inmutable, por lo que si
# quieres modificar una tupla, deberás convertirla primero en una lista.

# Sintaxis
Tupla = ('item1', 'item2', 'item3', 'item4')
Lista = list(Tupla)

Fruits = ('banana', 'orange', 'mango', 'lemon')
print("Tupla de frutas:", Fruits)
Fruits = list(Fruits)
print("Lista de frutas", Fruits)
Fruits[0] = 'apple'
print("Cambiamos banana por apple:", Fruits)
Fruits = tuple(Fruits)
print("Y la devolvemos a una tupla, ya modificada:", Fruits)
print()


# Comprobando items en una tupla.
# Podemos comprobar si un item existe o no en una tupla usando in, devolviendonos un valor booleano.

# Syntax
Tupla = ('item1', 'item2', 'item3', 'item4')
print('item2' in Tupla)
print()

Fruits = ('banana', 'orange', 'mango', 'lemon')
print("Se encuentra 'orange' en la tupla frutas? ", 'orange' in Fruits)
print("Se encuentra 'apple' en la tupla frutas? ", 'apple' in Fruits)
print()


# Juntando tuplas.
# Podemos juntar dos o más tuplas usando el operador +.

# Syntax
Tupla1 = ('item1', 'item2', 'item3', 'item4')
Tupla2 = ('item5', 'item6', 'item7', 'item8')
Tupla3 = Tupla1 + Tupla2
print("Tupla 1:", Tupla1)
print("Tupla2:", Tupla2)
print("Tupla3", Tupla3)
print()


Fruits = ('banana', 'orange', 'mango', 'lemon')
Vegetables = ('Tomato', 'Potatoe', 'Cabbage', 'Onion', 'Carrot')
FruitsAndVegetables = Fruits + Vegetables
print("Frutas:", Fruits)
print("Vegetales:", Vegetables)
print("Frutas y vegetales:", FruitsAndVegetables)
print()


# Borrando tuplas.
# No es posible eliminar un solo item de una tupla pero es possible eliminar una tupla usando del.

Tupla1 = ('Item1', 'Item2', 'Item3')
del Tupla1
#print(Tupla1)      # File "c:\Users\nekko\Documents\Programación\EjerciciosPython\Day6-Tuples\04-CambiandoTuplasAListas.py", line 64, in <module>
                    # print(Tupla1)
                    # NameError: name 'Tupla1' is not defined. Did you mean: 'Tupla'?

Fruits = ('banana', 'orange', 'mango', 'lemon')
del Fruits