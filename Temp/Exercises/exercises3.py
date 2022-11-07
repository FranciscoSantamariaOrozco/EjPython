#Exercises - Day 11
print()

# 3- Crea una función llamada sumar todos los números que tome un número arbitrario de argumentos y los sume todos entre ellos. 
# Comprueba que todos los items de la lista sean del tipo de dato número. Si no es así muestra un mensaje de error válido.

def SumarTodos(*Numeros):
    Total = 0                                               # Creamos la variable "Total" para almacenar el total de la suma, FUERA del bucle for.
    for i in Numeros:                                       # Creamos un bucle for que itere por la longitud de "Numeros"
        if type(i) != int and type(i) != float:             # Comprobara si es distinto de int y de float. Si es distinto de estos dos tipos, se mostrara el siguiente mensaje:
            print("El parámetro", "\"", i, "\"", "no se trata de un número \"int\" o \"float\", no se puede operar.", type(i))
            return "No se puede realizar la operación"      # Y se mostrara el siguiente mensaje de error
        else:                                               
            Total += i                                      # Si todo es correcto, se sumará el valor del parámetro a la variable Total.
    return Total                                            # Se retorna el valor de la variable "Total" una vez sumados todos los parámetros.
print(SumarTodos(5, 3, 1.5, "francisco"))
print()