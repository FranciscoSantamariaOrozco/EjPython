#Exercises - Day 7
print()

# Sets
ITCompanies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {22, 19, 24, 25, 26, 24, 25, 24}
Age = [22, 19, 24, 25, 26, 24, 25, 24]

# L3-2- "I am a teacher and i love to inspire and teach people."
# Cuantas palabras únicas se han utilizado en esta sentencia? utiliza el método split y set para obtener las palabras únicas.

Frase = "i am a teacher and i love to inspire and teach people"
Palabra1 = Frase[:1]
Palabra2 = Frase[2:4]
Palabra3 = Frase[5:6]
Palabra4 = Frase[7:14]
Palabra5 = Frase[15:18]
Palabra6 = Frase[19:20]
Palabra7 = Frase[21:25]
Palabra8 = Frase[26:28]
Palabra9 = Frase[29:36]
Palabra10 = Frase[37:40]
Palabra11 = Frase[41:46]
Palabra12 = Frase[47:53]

Lista = [Palabra1, Palabra2, Palabra3, Palabra4, Palabra5, Palabra6, Palabra7, Palabra8, Palabra9, Palabra10, Palabra11, Palabra12]
Set = set(Lista)
print("Las palabras únicas en la frase:\n", Frase, "\nson las siguientes:\n", Set)
print()
print("Por lo tanto hay", len(Set), "palabras únicas en la frase dada.")
print()