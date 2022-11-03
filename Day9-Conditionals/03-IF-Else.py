# Day 9 - Condicionales.
print()
# Condicional If Else
# En el caso anterior, ya que A vale 3, y este es mayor que 0, la sentencia es verdadera y se ejecuta el bloque de código. 
# Sin embargo, si este fuese falso, no se mostraría nada en pantalla. Para poder ver el resultado en caso de que If devuelva 
# un resultado FALSE, podemos hacer otro bloque con la instrucción else.

# En caso de que la condición se cumpla, se ejecutará el primer bloque de codigo.
# Si la condición no se cumple (False) se ejecutará el segundo bloque de código.

# Syntax
"""
    if condición:
        Esta parte del código funciona si la sentencia es verdadera.
    else:
        Esta parte del código se ejecuta si la sentencia es falsa.
"""

A = 3
if A < 0:
    print("A es un número negativo.")
else:
    print("A es un número positivo.")
print()