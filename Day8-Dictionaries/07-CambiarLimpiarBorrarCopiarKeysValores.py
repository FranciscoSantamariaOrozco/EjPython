# Day 8 - Diccionarios.
print()
# Cambiar diccionarios a una lista de items.
# El método items() puede cambiar el diccionario por una lista de tuplas.

Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
print("Diccionario original:", Diccionario)
print("Estas son las parejas de valores del diccionario:", Diccionario.items())
print()


# Limpiando un diccionario
# Si no queremos tener los items en el diccionario, podemos limpiarlo usando el método clear().

print("Diccionario original:", Diccionario)
Diccionario.clear()
print("Ahora hemos limpiado el diccionario con .clear():", Diccionario)
print()


# Eliminando un diccionario
# Si no vamos a usar más un diccionario, podemos eliminarlo por completo con del.

Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
del Diccionario
#print(Diccionario)         # ERROR
                            # Traceback (most recent call last):
                            #   File "c:\Users\Francisco.Orozco\Documents\Programacion\EjPython\Day8-Dictionaries\07-CambiarLimpiarBorrarCopiarKeysValores.py", line 27, in <module>
                            #     print(Diccionario)
                            # NameError: name 'Diccionario' is not defined 
print()


# Copiando un diccionario
# Podemos copiar diccionarios usando el método copy(). Usar la copia nos puede evitar tener que modificar el diccionario original.

Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
DiccionarioCopia = Diccionario.copy()
print("Esta es la copia del diccionario:", DiccionarioCopia)
print()


# Obteniendo la lista de llaves de un diccionario
# Podemos obtener las llaves de un diccionario en forma de lista con el método keys()
Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
Keys = Diccionario.keys()
print("Estas son las llaves del diccionario:", Keys)
print()


# Obteniendo la lista de valores de un diccionario
# Podemos obrener la lista de valores de un diccionario con el método .values()
Diccionario = {"llave1":"valor1", "llave2":"valor2", "llave3":"valor3", "llave4":"valor4"}
Values = Diccionario.values()
print("Estos son los valores del diccionario", Values)
print()