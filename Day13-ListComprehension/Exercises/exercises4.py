#Exercises - Day 13
print()

# 4 - Aplana la siguiente lista a una nueva lista:
"""
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    output:
    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
ListaPlana = [(number[0].upper(), number[0][0:3].upper() ,number[1].upper(),) for row in countries for number in row]

print(ListaPlana)
print()