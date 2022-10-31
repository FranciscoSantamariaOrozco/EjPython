# Removiendo items de listas
# el método remove() remueve un item especificado de una lista.
print()

Fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
print(Fruits)
Fruits.remove('banana')
print(Fruits)
Fruits.remove('lemon')
print(Fruits)
print()



# Removiendo items usando Pop
# El método pop() remueve el index especificado (o el último index, si este no es especificado)
Fruits = ['banana', 'orange', 'mango', 'lemon']
print(Fruits)
Fruits.pop()
print(Fruits)               # ['banana', 'orange', 'mango']
Fruits.pop(0)
print(Fruits)               # ['orange', 'mango']
print()



# Removiendo items usando Del
# La keyword "del" remueve el index especificado y también puede eliminar index de un rango determinado.
# También puede eliminar la lista por completo.

Fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
print('lista original: ', Fruits)
del Fruits[0]
print('del Fruits[0]: ', Fruits)                # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del Fruits[1]
print('del Fruits[1]: ', Fruits)                # ['orange', 'lemon', 'kiwi', 'lime']
del Fruits[1:3]                                 # Esto elimina los items entre los index facilitados, pero no elimina el ultimo item! (index3)
print('del Fruits[1:3]: ',Fruits)               # ['orange', 'lime']
del Fruits
# print('del Fruits: ',Fruits)                    # Este debe dar el siguiente error: NameError: name 'Fruits' is not defined
print()



# Limpiando los items de una lista
# El método clear permite vaciar una lista:

Fruits= ['banana', 'orange', 'mango', 'lemon']
print(Fruits)
Fruits.clear()      # []
print(Fruits)
print()