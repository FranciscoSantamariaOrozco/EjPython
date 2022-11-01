#Exercises - Day 6
print()

# l2.3- Cambia la tupla FoodStuff_tp a la lista FoodStuff_ls
Frutas = ("orange", "apple", "banana", "lemon")
Vegetales = ("Brocoli", "Lechuga", "Tomate")
ProdAnim = ("Carne", "Leche", "Queso")
FoodStuff_tp = Frutas + Vegetales + ProdAnim

print("Tenemos la tupla FoodStuf_tp:", FoodStuff_tp)
FoodStuff_tp = list(FoodStuff_tp)
print("La convertimos a una lista:", FoodStuff_tp)
FoodStuff_ls = FoodStuff_tp
print("Por último modificamos el nombre a FoodStuff_ls:", FoodStuff_ls)
print()