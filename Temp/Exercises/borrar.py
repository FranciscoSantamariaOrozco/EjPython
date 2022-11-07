def SumarTodos(*Numeros):
    Total = 0
    for i in Numeros:
        if type(i) != int:
            print("El parámetro", i, "no se trata de un número, no se puede operar.")
            print(type(i))
        else:
            print("OK")
            for i in Numeros:
                Total += i
                return Total
               
print(SumarTodos(5, 7, "A"))
print()
