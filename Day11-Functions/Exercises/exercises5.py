#Exercises - Day 11
print()

# 5- Escribe una función llamada "CompruebaEstaciones", que tome como parámetro un mes, y devuelva la estación en la que nos encontramos.

MesActual = input("Introduce el mes en el que estamos: ")
def CompruebaEstaciones(Mes):
    if Mes == "Diciembre" or Mes == "Enero" or Mes == "Febrero" or Mes == "diciembre" or Mes == "enero" or Mes == "febrero":
        return "Nos encontramos en invierno"
    elif Mes == "Marzo" or Mes == "Abril" or Mes == "Mayo" or Mes == "marzo" or Mes == "abril" or Mes == "mayo":
        return "Nos encontramos en primavera"
    elif Mes == "Junio" or Mes == "Julio" or Mes == "Agosto" or  Mes == "junio" or Mes == "julio" or Mes == "agosto":
        return "Nos encontramos en verano"
    elif Mes == "Septiembre" or Mes == "Octubre" or Mes == "Noviembre" or Mes == "septiembre" or Mes == "octubre" or Mes == "noviembre":
        return "Nos encontramos en otoño"
    else:
        return "Seguro que has escrito bien el mes?"
print(CompruebaEstaciones(MesActual))