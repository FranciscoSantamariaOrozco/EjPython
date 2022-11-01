#Exercises - Day 6
print()

# l2.4- Haz slice de los items de enmedio de la tupla o lista.

Frutas = ("orange", "apple", "banana", "lemon")
Vegetales = ("Brocoli", "Lechuga", "Tomate")
ProdAnim = ("Carne", "Leche", "Queso")
FoodStuff_tp = Frutas + Vegetales + ProdAnim
FoodStuf_ls = list(FoodStuff_tp)

MiddleTwo_tp = FoodStuff_tp[5:7]
print("Las dos de enmedio de la tupla son:", MiddleTwo_tp)
MiddleTwo_ls = FoodStuf_ls[5:7]
print("Las dos de enmedio de la lista son:", MiddleTwo_ls)
print()