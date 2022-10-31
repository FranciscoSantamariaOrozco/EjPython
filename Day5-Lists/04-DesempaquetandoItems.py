# Desempaquetando items de una lista
print()

lst1 = ['item1', 'item2', 'item3', 'item4', 'item5']
FirstItem, SecondItem, ThirdItem, *rest = lst1
print(FirstItem)        # Item1
print(SecondItem)       # Item2
print(ThirdItem)        # Item3
print(rest)             # ['item4', 'item5']
print()

# Primer ejemplo
Fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
FirstFruit, SecondFruit, ThirdFruit, *rest = Fruits
print(FirstFruit)       # banana
print(SecondFruit)      # orange
print(ThirdFruit)        # mango
print(rest)             # ['lemon', 'lime', 'apple']
print()

# Segundo ejemplo
First, Second, Third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(First)
print(Second)
print(Third)
print(rest)
print(tenth)
print()

# Tercer ejemplo
Countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = Countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)