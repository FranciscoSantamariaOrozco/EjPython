#Exercises - Day 13
print()

# 1 - Filtra los números negativos y el cero usando listcomprehension

numbers = [-11, -4, -3, -2, -1, 0, 2, 4, 6]

Negativos = [i for i in range(-20,20) if i <= 0 and numbers.count(i) >= 1]
print(Negativos)
print()