#Exercises - Day 13
print()

# 5 - Cambia la siguiente lista a una lista de diccionarios.
"""
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    output:
    [{'country': 'FINLAND', 'city': 'HELSINKI'},
    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
    {'country': 'NORWAY', 'city': 'OSLO'}]
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
ListaPlana = [{"Country:":number[0].upper(), "City:":number[1].upper()} for row in countries for number in row]
print(ListaPlana)