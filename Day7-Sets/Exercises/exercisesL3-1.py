#Exercises - Day 7
print()

# Sets
ITCompanies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {22, 19, 24, 25, 26, 24, 25, 24}
Age = [22, 19, 24, 25, 26, 24, 25, 24]

# L3-1- Convierte la lista Age en un set, y compara sus longitudes. Cual es mayor?

SetAge = set(Age)
print("Esta es la lista Age:", Age)
print("Esta es la lista Age convertida a set:", SetAge)
print("La longitud de la lista Age es:", len(Age))
print("La longitud del set SetAge es:", len(SetAge))
print("Por lo tanto, es Age mayor que SetAge?", len(Age) > len(SetAge))
print()