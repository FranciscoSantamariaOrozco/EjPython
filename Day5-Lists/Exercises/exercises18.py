#Exercises - Day 5
print()

# 18- Corta fuera los 3 primeros items de la lista

IT_Companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Lista original: ", IT_Companies)
# del IT_Companies[0]
# IT_Companies.pop(0)
# IT_Companies.remove("Microsoft")
del IT_Companies[:3]
print("Lista cortada: ", IT_Companies)
print()