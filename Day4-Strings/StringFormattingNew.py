# New String format (v3+)
print()


FirstName = "Francisco"
LastName = "Orozco"
Language = "Python"
FormatedStringName = "I am {} {}. I teach {}".format(FirstName, LastName, Language)
print(FormatedStringName)
print()

# With numbers
a = 4
b = 3

print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b)) # Float limitado a dos dígitos
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
print()


# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
FormatedStringArea = "El area de un circulo con radio {} es de {:.2f}".format(radius, area)
print(FormatedStringArea)
print()


# String interpolation
# Una nueva manera de dar formato a strings es la interpolación o las f-strings. 
# Empiezan con f y pueden inyectar directamente la información.
a = 4
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}") 
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
print()