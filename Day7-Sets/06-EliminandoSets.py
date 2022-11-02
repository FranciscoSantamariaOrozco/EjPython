# Day 7 - Sets
print()
# Eliminando sets
# Si queremos eliminar un set podemos usar el operador del().

# Syntax

Set = {"item1", "item2", "item3", "item4"}
print("Set original:", Set)
del Set
#print(Set)     # Si intentamos imprimir el set, nos dará un mensaje de error indicando que esta vacío:
                # Traceback (most recent call last):
                #  File "c:\Users\Francisco.Orozco\Documents\Programacion\EjPython\Day7-Sets\06-EliminandoSets.py", line 11, in <module>
                #    print(Set)
                # NameError: name 'Set' is not defined. Did you mean: 'set'?
print()

Frutas = {"banana", "orange", "mango", "lemon"}
del Frutas