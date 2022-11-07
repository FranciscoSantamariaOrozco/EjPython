#Exercises - Day 11
print()

# 3- Crea una función llamada sumar todos los números que tome un número arbitrario de argumentos y los sume todos entre ellos. 
# Comprueba que todos los items de la lista sean del tipo de dato número. Si no es así muestra un mensaje de error válido.

def SumarTodos(*Numeros):
            Total = 0
            for i in Numeros:
                Total += i
            return Total
print(SumarTodos(10, 15, 1))
print