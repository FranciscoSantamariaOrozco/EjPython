# Day 7 - Sets
print()
# Eliminando items de un set.
# Podemos eliminar items de un set usando el método remove(). Si el item no es encontrado por el método remove(), puede
# dar errores, por lo que es bueno verificar si el item existe en el set indicado.
# Si no, el método discard() no genera errores.

# Syntax
Set = {"item1", "item2", "item3", "item4"}
print("Set original:", Set)
Set.remove("item2")
print("Set tras remover 'item2':", Set)
#Set.remove("item5")    # Si utilizamos .remove() con un item que no se encuentra en la lista, nos dará el siguiente error:
                        # Traceback (most recent call last):
                        #   File "..\Day7-Sets\04-EliminandoItems.py", line 13, in <module>
                        #     Set.remove("item5")
                        # KeyError: 'item5'

Set.discard("item5")    # Con discard no da error si el item5 no existe dentro del set. simplemente no modifica nada.
print("Set sin modificar ya que discard() no encontro 'item5':", Set)
print()


# El método pop() remueve un item aleatorio de la lista.

Frutas = {"banana", "orange", "mango", "lemon"}
Frutas.pop()
print("Frutas con un removido aleatorio", Frutas)
print()
FrutaRemovida = Frutas.pop()        # Si estas interesado en conocer el item que removemos:
print("Ahora removemos otra fruta:", Frutas)
print("Este es el item que hemos eliminado:", FrutaRemovida)
print()