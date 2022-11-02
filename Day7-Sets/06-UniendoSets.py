# Day 7 - Sets
print()
# Uniendo sets
# Podemos unir dos sets usando el método union()
# El método unión nos devolverá un nuevo set.

# Syntax

Set1 = {"item1", "item2", "item3", "item4"}
print("Este es el set 1:", Set1)
Set2 = {"item5", "item6", "item7"}
print("Este es el set 2:", Set2)
Set3 = Set1.union(Set2)
print("Unimos ambos, y generamos Set3:", Set3)
print()


Frutas = {"banana", "orange", "mango", "lemon"}
print("Estas son las frutas:", Frutas)
Vegetales = {"tomato", "potato", "cabbage", "onion", "carrot"}
print("Estos son los vegetales:", Vegetales)
print("Y esto son las frutas y los vegetales juntos:", Frutas.union(Vegetales))
print()


# Con el método update() podemos insertar un set dentro de otro

Set1 = {"item1", "item2", "item3", "item4"}
print("Este es el set 1", Set1)
Set2 = {"item5", "item6", "item7"}
print("Este es el set 2:", Set2)
Set1.update(Set2)
print("Ahora el Set1 contiene también los datos del Set2:", Set1)
print()

Frutas = {"banana", "orange", "mango", "lemon"}
print("Estas son las frutas:", Frutas)
Vegetales = {"tomato", "potato", "cabbage", "onion", "carrot"}
print("Estos son los vegetales:", Vegetales)
Frutas.update(Vegetales)
print("Ahora el set Frutas también contiene los vegetales:", Frutas)
print()