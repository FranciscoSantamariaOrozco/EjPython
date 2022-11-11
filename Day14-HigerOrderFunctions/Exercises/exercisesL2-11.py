#Exercises - Day 13
print()

# L2-11 - Usa reduce() para concatenar todos los países y producir la siguiente sentencia: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def SumDosStr(x, y):
    LastIndex = len(countries)-1
    LastCountry = countries[LastIndex]
    if y == LastCountry:
        return str(x) + " and " + str(y) + " are north European countries."
    else:
        return str(x) + ", " + str(y)

Frase = reduce(SumDosStr, countries)
print(Frase)
print()