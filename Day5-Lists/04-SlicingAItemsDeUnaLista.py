# Cortar items de una lista
print()
"""
Con indexación positiva: Nosotros podemos especificar un rango de index positivos 
especificando el comienzo, el final, y el salto. Los valores devueltos
pueden ser una nueva lista. 
(Valores por defecto: start=0, end =len(lst)-1 [last item], step=1)
"""
Frutas = ['banana', 'orange', 'mango', 'lemon']
AllFruits = Frutas[0:4]         # Esto devuelve todas las frutas
print(AllFruits)
AllFruits = Frutas[0:]          # Esto también devuelve todas las frutas
print(AllFruits)
OrangeAndMango = Frutas[1:3]    # Esto devuelve las frutas de la una a la 3 (sin contar esta última) ['orange', 'mango']
print(OrangeAndMango)
OrangeMangoLemon = Frutas[1:]   # Empieza a contar desde el index 1
print(OrangeMangoLemon)
OrangeAndLemon = Frutas[::2]    # El tercer argumento es el paso, o salto. Aqui va a saltar de 2 en 2.
print(OrangeAndLemon)
print()

"""
Con indexación negativa: Nosotros podemos especificar un rango de index negativos 
especificando el comienzo, el final, y el salto. Los valores devueltos
pueden ser una nueva lista. 
"""
Frutas = ['banana', 'orange', 'mango', 'lemon']
AllFruits = Frutas[-4:]         # Esto devuelve toda las frutas
print(AllFruits)
OrangeAndMango = Frutas[-3:-1]  # Empieza a contar desde -3, pero se para en -2 por que hemos excluido el último index.
print(OrangeAndMango)
OrangeMangoLemon = Frutas[-3:]  # Esta orden comienza desde -3, hasta el final ['orange', 'mango', 'lemon']
print(OrangeMangoLemon)
ReverseFruits =  Frutas[::-1]   # Un step negativo toma la lista en orden inverso
print(ReverseFruits)