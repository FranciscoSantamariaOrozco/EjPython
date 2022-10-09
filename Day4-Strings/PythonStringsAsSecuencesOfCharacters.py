# Desempaquetando una string como secuencia de caracteres.
print()
language = "Python"
a, b, c, d, e, f = language # Desempaqueta la secuencia dentro de las variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print()


# Accediendo por el Index
language = "Python"
FirstLetter = language[0]
print(FirstLetter)
SecondLetter = language[1]
print(SecondLetter)
LastIndex = len(language) -1
LastLetter = language[LastIndex]
print(LastLetter)
print()

# Puedes usar el Index negativo si necesitas acceder desde la derecha del string. -1 es el ultimo Index.
language = "Python"
LastLetter = language[-1]
print(LastLetter)
SecondLast = language[-2]
print(SecondLast)
print()