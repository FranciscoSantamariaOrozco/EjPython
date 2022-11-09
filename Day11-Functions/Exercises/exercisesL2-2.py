#Exercises - Day 11
print()

# L2-2 - Declara una función llamada Factorial. Esta tomará un número como parámetro y devolverá el factorial del número.
def Factorial(Num):
    i = 1
    Fact = Num
    while i < Num:
        Fact = Fact * i
        i= i + 1
    return Fact
print(Factorial(5))
print(Factorial(10))
print(Factorial(100))