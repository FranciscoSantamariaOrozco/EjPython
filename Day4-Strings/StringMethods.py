# Metodos para Strings
print()

# capitalize() convierte la primera letra en mayúscula
challenge = "thirty days of python"
print(challenge.capitalize())           #Thirty days of python
print()

# count() indica las veces que se encuentra la cadena indicada en la string.
print(challenge.count("y"))         #3
print(challenge.count("y", 7, 14))  #1
print(challenge.count("th"))        #2
print()

# endswitch() Comprueba si la cadena finaliza con lo que se le ha indicado.
print(challenge.endswith("on"))     #True
print(challenge.endswith("tion"))   #False
print()

# expandtabs() Remplaza tabulaciones con espacios, el espacio por defecto es de 8.
challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs())       #thirty  days    of      python
print(challenge.expandtabs(10))     #thirty    days      of        python
print()

# find() Devuelve el index de la primera coincidencia en una string. Si no se encuentra devuelve -1.
challenge = "thirty days of python"
print(challenge.find('y'))              #5
print(challenge.find('th'))             #0
print()

# rfind() Devuelve el index de la ultima coincidencia en una string. Si no se encuentra devuelve -1.
challenge = "thirty days of python"
print(challenge.rfind("y"))             #16
print(challenge.rfind("th"))            #17
print()

# format() formatea una string en un mejor output.
FirstName = "Francisco"
LastName = "Orozco"
age = "34"
job = "student"
country = "Portugal"
sentence = "I am {} {}. I am a {}. I am {} years old. I live in {}.".format(FirstName, LastName, job, age, country)
print(sentence)     #I am Francisco Orozco. I am a student. I am 34 years old. I live in Portugal.
print()

radius = 10
pi = 3.14
area = pi * radius ** 2
result = "El área de un circulo de radio {} es {}.".format(str(radius), str(area))
print(result)       #El área de un circulo de radio 10 es 314.0.
print()

# index() Devuelve el valor mas bajo encontrado en el index de la substring. los argumentos adicionales indican
# el comienzo y el final de la búsqueda en el index. (default 0 and string length -1). Si la substring no se encuentra
# se devuelve value errror.
challenge = "thirty days of python"
SubString = "da"
print(challenge.index(SubString))        #7
#print(challenge.index(SubString, 9))    #ERROR
print()

# rindex() Devuelve el valor mas alto encontrado en el index de la substring.
challenge = "thirty days of python"
SubString = "da"
print(challenge.rindex(SubString))      #8
#print(challenge.rindex(SubString, 8))   #ERROR
print()

# isalnum() Comprueba si una cadena es alfanumérica
challenge = "ThirtyDaysOfPython"
print(challenge.isalnum())          #True
challenge = "30DaysPython"
print(challenge.isalnum())          #True
challenge = "thirty days of python"
print(challenge.isalnum())          #False, space is not an alphanumeric character
challenge = "thirty days of python 2019"
print(challenge.isalnum())          #False
print()

# isalpha() Comprueba si una cadena contiene sólo caracteres del alfabeto.
challenge = "thirty days of python"
print(challenge.isalpha())      #False, space is once again excluded.
challenge = "ThirtyDaysOfPython"
print(challenge.isalpha())      #True
num = "123"
print(num.isalpha())            #False
print()

# isdecimal() Comprueba si una cadena tiene sólo caracteres decimales.
challenge = "thirty days of python"
print(challenge.isdecimal())        #False
challenge = "123"
print(challenge.isdecimal())        #True
challenge = "\u00b2"
print(challenge.isdecimal())        #False
challenge = "12 3"
print(challenge.isdecimal())        #False, space not allowed
print()

# isdigit() comprueba si una cadena contiene números
challenge = "Thirty"
print(challenge.isdigit())      #False
challenge = "30"
print(challenge.isdigit())      #True
challenge = "\u00b2"
print(challenge.isdigit())      #True
print()

# isnumeric() Comprueba si una cadena contiene números como isdigit pero también acepta ciertos símbolos
num = "10"
print(num.isnumeric())      #True
num = "\u00BD"
print(num.isnumeric())      #True
num = "10.5"
print(num.isnumeric())      #False
print()

# isidentifier() Comprueba si la string puede ser un nombre de variable válido
challenge = "30DaysOfPython"
print(challenge.isidentifier())     #False, because it starts with a number.
challenge = "thirty_days_of_python"
print(challenge.isidentifier())     #True
print()

# islower() Comprueba si todos los caracteres de una string están en minúsculas
challenge = "thirty days of python"
print(challenge.islower())        #True
challenge = "Thirty days of python"
print(challenge.islower())      #False
print()

# isupper() Comprueba si todos los caracteres de una string están en mayúsculas.
challenge = "thirty days of python"
print(challenge.isupper())      #False
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())      #True
print()

# join() Devuelve una string concatenada
WebTech = ["HTML", "CSS", "JavaScript", "React"]
result = ' '.join(WebTech)
print(result)           #HTML CSS JavaScript React

WebTech = ["HTML", "CSS", "JavaScript", "React"]
result = "# ".join(WebTech)
print(result)           #HTML# CSS# JavaScript# React
print()

# strip() Remueve los caracteres indicados de la cadena
challenge = "thirty days of pythoooonnn"
print(challenge.strip("noth"))      #irty days of py
print()

# replace() Reemplaza la substring con la string indicada
challenge = "thirty days of python"
print(challenge.replace("python", "coding"))
print()

# split() corta la string, usa la string dada o el espacio como separador
challenge = "thirty days of python"
print(challenge.split())            #['thirty', 'days', 'of', 'python']
challenge = "thirty, days, of, python"
print(challenge.split(", "))        #['thirty', 'days', 'of', 'python']
print()

# title() Devuelve una string con la primera letra en mayúscula
challenge = "thirty days of python"
print(challenge.title())        #Thirty Days Of Python
print()

# swapcase() Convierte las mayúsculas en minúsculas y viceversa.
challenge = "thirty days of python"
print(challenge.swapcase())         #THIRTY DAYS OF PYTHON
challenge = "Thirty Days Of Python"
print(challenge.swapcase())         #tHIRTY dAYS oF pYTHON
print()

# startswith() Comprueba si la string comienza con la cadena indicada.
challenge = "thirty days of python"
print(challenge.startswith("thirty"))       #True
challenge = "30 days of python"
print(challenge.startswith("thirty"))       #False
print()