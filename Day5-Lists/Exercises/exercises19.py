#Exercises - Day 5
print()

# 19- Corta los 3 últimos items de la lista.

IT_Companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Lista original: ", IT_Companies)
# IT_Companies.pop()
# del IT_Companies[-1]
# IT_Companies.remove("IBM")
del IT_Companies[-3:]
print("Lista cortada: ", IT_Companies)
print()