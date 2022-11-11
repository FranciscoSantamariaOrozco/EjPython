#Exercises - Day 13
print()

# L2-8 - Encadena dos o mas iteradores de lista  (eg. arr.map(callback).filter(callback).reduce(callback))
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Países que contengan exactamente seis letras convertidos a mayúsculas
def Mayusc(Pais):
    return Pais.upper()

def PaisesSeisLetras(Pais):
    if len(Pais) == 6:
        return True
    return False

ListaPersonalizada = filter(PaisesSeisLetras, map(Mayusc, countries) ) 
print(list(ListaPersonalizada))
print()