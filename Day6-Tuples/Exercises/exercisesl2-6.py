#Exercises - Day 6
print()

# l2.6- Elimina por completo la tupla FoodStaff_tp.

Frutas = ("orange", "apple", "banana", "lemon")
Vegetales = ("Brocoli", "Lechuga", "Tomate")
ProdAnim = ("Carne", "Leche", "Queso")
FoodStuff_tp = Frutas + Vegetales + ProdAnim
FoodStuf_ls = list(FoodStuff_tp)

del FoodStuff_tp
#print(FoodStuff_tp)
                        # File "c:\Users\nekko\Documents\Programación\EjerciciosPython\Day6-Tuples\Exercises\exercisesl2-6.py", line 13, in <module>
                        # print(FoodStuff_tp)
                        # NameError: name 'FoodStuff_tp' is not defined. Did you mean: 'FoodStuf_ls'?
print()