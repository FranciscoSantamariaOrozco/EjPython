# Day 11 - Funciones
print()
# Función con valor retornado
# Si no le damos como retorno un valor a la función, nuestra función devolvera None por efecto. Para devolver un valor con una función
# es necesario utilizar la palabra clave "return" con la variable a retornar. 

# Devolviendo una string

def PrintNombre(Nombre):
    return Nombre
print(PrintNombre("Francisco"))
print()

def PrintNombreCompleto(Nombre, Apellido):
    Espacio = " "
    NomComp = Nombre + Espacio + Apellido
    return NomComp
print(PrintNombreCompleto("Francisco", "Orozco"))
print()


# Devolviendo un número

def DosNumeros(Num1, Num2):
    Total = Num1 + Num2
    return Total
print(DosNumeros(5, 2))
print()

def CalcularEdad(Aact, Anac):
    Edad = Aact - Anac
    return Edad
print(CalcularEdad(2022, 1988))
print()

# Devolviendo un valor booleano

def EsPar(Num):
    if Num % 2 == 0:
        print("Es par")
        return(True)
    return False
print(EsPar(10))
print(EsPar(7))
print()

# Devolviendo una lista

def NumerosPares(n):
    Pares = []
    for i in range(n+1):
        if i % 2 == 0:
            Pares.append(i)
    return Pares
print(NumerosPares(100))
print()