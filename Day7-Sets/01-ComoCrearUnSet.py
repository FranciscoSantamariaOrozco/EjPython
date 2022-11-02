# Day 7 - Sets
print()
# Como crear un set.
"""
    Un set es una coleccion de items. En concreto, es una colección de elementos únicos, desordenados y no-indexados.
    En python los sets son utilizados para guardar items unicos, y es posible encontrarlos con find, intersection,
    diference, subset, super set y disjoint set.
"""

# Creando un set
# Se usan los corchetes curvados o la función set().

# Syntax
# Creando un set vacío

Set = {}
# o
Set = set()

# Creando un set con items iniciales

Set = {"item1", "item2", "item3", "item4"}
Frutas = {"banana", "orange", "mango", "lemon"}


# Obteniendo la longitud de un set

Set = {"item1", "item2", "item3", "item4"}
len(Set)
print("La longitud del set es de:", len(Set))
print()

Frutas = {"banana", "orange", "mango", "lemon"}
print("La longitud del set 'frutas' es:", len(Frutas))
print()

# Accediendo a items en un set.
# Usaremos los bucles para acceder a los items. Veremos más en la sección de loops.
