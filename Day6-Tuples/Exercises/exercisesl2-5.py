#Exercises - Day 6
print()

# l2.5- Haz slice de los 3 primeros y últimos items de la lista FoodStaff_lt

Frutas = ("orange", "apple", "banana", "lemon")
Vegetales = ("Brocoli", "Lechuga", "Tomate")
ProdAnim = ("Carne", "Leche", "Queso")
FoodStuff_tp = Frutas + Vegetales + ProdAnim
FoodStuf_ls = list(FoodStuff_tp)

ThreeFirst = FoodStuf_ls[:3]
ThreeLast = FoodStuf_ls[-3:]
print("Tres primeros items:", ThreeFirst)
print("Tres últimos items:", ThreeLast)
print()