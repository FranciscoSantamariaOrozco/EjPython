#Exercises - Day 11
print()

# L3-4 - Escriba una función que verifique si la variable proporcionada es una variable de Python valida.

def VariableValida(NomVariable):
    if NomVariable.isidentifier() == True:
        return NomVariable, "Es un nombre de variable válido!"
    else:
        return NomVariable, "No es válido como nombre para una variable"
print(VariableValida("30DiasDePython"))
print(VariableValida("treinta_dias_de_python"))