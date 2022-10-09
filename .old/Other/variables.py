# Ejercicio dia 2

# Declara una variable para el nombre, y asignale un valor.
nombre = "Francisco"

# Declara una variable para el apellido y asignale un valor
apellido = "Orozco"

# Declara una variable para el pais
pais = "Portugal"

# Declara una variable para la ciudad
ciudad = "Lisboa"

# Declara una variable para la edad
edad = 34

# Declara una variable para el año de nacimiento
nacimiento = 1988

# Declara una variable para el estado civil
casado = False

# Declara una variable de los datos son correctos
los_datos_son_correctos = True

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Pais:", pais)
print("Ciudad:", ciudad)
print("Edad:", edad)
print("Año de nacimiento", nacimiento)
print("Casado:", casado)
print("Son los datos correctos?", los_datos_son_correctos)
print()

# Declara todas las variables en una única linea.
nombre, apellido, pais, ciudad, edad, nacimiento, casado, los_datos_son_correctos = "Francisco2", "Orozco2", "Portugal2", "Lisboa2", 35, 1988, False, True 

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Pais:", pais)
print("Ciudad:", ciudad)
print("Edad:", edad)
print("Año de nacimiento", nacimiento)
print("Casado:", casado)
print("Son los datos correctos?", los_datos_son_correctos)
print()

# Comprueba el tipo de datos de todas tus variables

print("Nombre:", nombre)
print(type(nombre))
print()

print("Apellido:", apellido)
print(type(apellido))
print()

print("Pais:", pais)
print(type(pais))
print()

print("Ciudad:", ciudad)
print(type(ciudad))
print()

print("Edad:", edad)
print(type(edad))
print()

print("Año de nacimiento", nacimiento)
print(type(nacimiento))
print()

print("Casado:", casado)
print(type(casado))
print()

print("Son los datos correctos?", los_datos_son_correctos)
print(type(los_datos_son_correctos))
print()

# Usa la funcion len() para conocer la longitud de tu nombre.

print("La longitud de mi nombre es:")
print(len(nombre))
print("")

# Compara la longitud de tu nombre con la de tu apellido:

print("La longitud del nombre es:")
print(len(nombre))
print("y la longitud del apellido es:")
print(len(apellido))
print("La diferencia entre el nombre y el apellido es de:")
print(len(nombre) - len(apellido))
print("")

# Declara las variables "num_one" y "num_two como 5 y 4 respectivamente"

num_one = 5
num_two = 4
print("num_one es:", num_one)
print("num_two es:", num_two)
print("")

total = ((num_one) + (num_two))
print("la suma de 'num_one' y 'num_two' es:")
print(total)
print("")

print("la diferencia de 'num_one' y 'num_two' es:")
diff = (num_one - num_two)
print(diff)
print()

print("la multiplicación de 'num_one' por 'num_two' es:")
product = (num_one * num_two)
print(product)
print()

print("la división de 'num_one' entre 'num_two' es:")
division = (num_one / num_two)
print(division)

print("el resto de la división es:")
remainder = (num_one % num_two)
print(remainder)
print()

print("'num_one' elevado a 'num_two' es igual a:")
exp = (num_one ** num_two)
print(exp)
print()

print("la floor division es :")
floor_division = (num_one // num_two)
print(floor_division)
print()