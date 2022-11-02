#Exercises - Day 7
print()

# Sets
ITCompanies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {22, 19, 24, 25, 26, 24, 25, 24}

# L2-5- Incluye A en B o B en A.

C = A.union(B)
print("Podemos juntar A y B en un nuevo set:", C)
A.update(B)
print("O podemos añadir el contenido de A a B:", A )