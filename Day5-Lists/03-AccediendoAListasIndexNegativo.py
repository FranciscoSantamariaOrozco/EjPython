print()

# Desempaquetando items de la lista
Lst = ['item1', 'item2', 'item3', 'item4', 'item5']
FirstItem, SecondItem, ThirdItem, *Rest = Lst
print(FirstItem)
print()

# Primer Ejemplo
Frutas = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
FirstFruit, SecondFruit, ThirdFruit, *Rest = Frutas
print(FirstFruit)       # banana
print(SecondFruit)      # orange
print(ThirdFruit)       # mango
print(Rest)             # ['lemon', 'lime', 'apple']
print()

# Segundo ejemplo sobr desempaquetar listas
First, Second, Third, *Rest, Tenth = [1,2,3,4,5,6,7,8,9,10]
print(First)         # 1
print(Second)        # 2
print(Third)         # 3
print(Rest)          # [4,5,6,7,8,9]
print(Tenth)         # 10
print()

# Tercer ejemplo sobre desempaquetar listas
Countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, est = Countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(est)
print()