#Exercises - Day 5
print()

# T2-1- Dada la siguiente lista de 10 edades de estudiantes:

Edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordena la lista y encuentra la edad máxima y mínima

Edades.sort()
print("Edades ordenadas:", Edades)
print("La persona más joven tiene:", Edades[0], "Años")
print("La persona más mayor tiene:", Edades[-1], "Años")
print()

# Añade la edad minima y la edad maxima de nuevo a la lista

Edades.append(Edades[-1])
Edades.insert(0, Edades[0])
print("Mas joven y mas mayor añadidos de nuevo:", Edades)
print()

# Encuentra la edad media (uno o dos items de la mitad)

Longitud = len(Edades)
Media = int(Longitud / 2)
print("La edad media es", Edades[Media], "-", Edades[Media+1], "Años" )
print()

# Encuentra la edad media verdadera (la suma de todos los items dividida por su número)

Longitud = len(Edades)
print("Tenemos", Longitud, "Alumnos.")
Suma = sum(Edades)
print("La suma de sus edades es de", Suma, "Años.")
MediaVerdadera = Suma / Longitud
print("La media verdadera de edad es:", MediaVerdadera)
print()

# Encuentra el rango de edad (Máximo menos mínimo)

MaxEdad = max(Edades)
MinEdad = min(Edades)
RangoEdad = MaxEdad - MinEdad
print("Tenemos alumnos que van desde los", MinEdad, "Hasta los", MaxEdad, "Años de edad.")
print("El rango de edades que abarcamos es de hasta", MaxEdad - MinEdad, "Años.")
print()

# Compara los valores del (minimo-medio) y (maximo-medio) con el método abs()

