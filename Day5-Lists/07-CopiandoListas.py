# Copiando listas
print()
# Es posible copiar una lista reasignandola como una nueva variable de la siguiente manera: lista1 = lista2.
# Ahora, lista2 es una referencia a lista1, cualquier cambio que hagamos en lista2 tambien modificara el original, lista1.
# Pero puede haber un montón de casos en los que no queremos modificar el original, y que la copia pueda ser diferente.
# Una de las maneras es con la funcion copy()

Fruits = ['banana', 'orange', 'mango', 'lemon']
FruitsCopy = Fruits.copy()
print('Lista Frutas: ', Fruits)
print('Copia: ', FruitsCopy)
print() 



# Insertando listas
# Hay varias formas de unir, o concatenar, dos o más listas en python.
# Con operador Plus (+)

PositiveNumbers = [1,2,3,4,5]
Zero = [0]
NegativeNumbers = [-5, -4, -3, -2, -1]
Integrales = NegativeNumbers +  Zero + PositiveNumbers
print(Integrales)
print()

Fruits = ['banana', 'orange', 'mango', 'lemon']
Vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
FruitsAndVegetables = Fruits + Vegetables
print(FruitsAndVegetables)
print()



# Podemos unir listas utilizando el método extend() para unir una lista al final de otra.
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Números: ', num1)
NegativeNumbers = [-5, -4, -3, -2, -1]
PositiveNumbers = [1, 2, 3, 4, 5]
Zero = [0]
NegativeNumbers.extend(Zero)
NegativeNumbers.extend(PositiveNumbers)
print('Integrales: ', NegativeNumbers)
print()

Fruits = ['banana', 'orange', 'mango', 'lemon']
Vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot',]
Fruits.extend(Vegetables)
print('Frutas y vegetales: ', Fruits)
print()