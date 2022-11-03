#Exercises - Day 9
print()

# L2-2- Comprueba si la estación es otoño, invierno, primavera o verano. Si el usuario introduce:
# Septiembre, octubre o noviembre, la estación es otoño. Diciembre enero y febrero serán invierno. Marzo, abril o mayo seran primavera
# y junio, julio y agosto será verano.

print("CALENDARIO DE ESTACIONES\n")
print("Seleccione un mes:\n1-Enero\n2-Febrero\n3-Marzo\n4-Abril\n5-Mayo\n6-Junio\n7-Julio\n8-Agosto\n9-Septiembre\n10-Octubre\n11-Noviembre\n12-Diciembre\n")
Mes = input("Introduzca el número de mes en el que estamos:")
Mes = int(Mes)
if Mes < 1:
    print("Error; introduzca un mes del 1 al 12")
elif Mes > 12:
    print("Error; introduzca un mes del 1 al 12")
elif Mes == 12 or Mes == 1 or Mes == 2:
    print("Estamos en invierno")
elif Mes == 3 or Mes == 4 or Mes == 5:
    print("Estamos en primavera")
elif Mes == 6 or Mes == 7 or Mes == 8:
    print("Estamos en verano")
else:
    print("Estamos en otoño")
print()

"""
print("CALENDARIO DE ESTACIONES\n")
print("Seleccione un mes:\n1-Enero\n2-Febrero\n3-Marzo\n4-Abril\n5-Mayo\n6-Junio\n7-Julio\n8-Agosto\n9-Septiembre\n10-Octubre\n11-Noviembre\n12-Diciembre\n")
Mes = input("Introduzca el número de mes en el que estamos:")
Mes = int(Mes)
if Mes < 1:
    print("Error; introduzca un mes del 1 al 12")
elif Mes > 12:
    print("Error; introduzca un mes del 1 al 12")
elif Mes < 4:
    print("Estamos en invierno")
elif Mes < 7:
    print("Estamos en primavera")
elif Mes < 10:
    print("Estamos en verano")
else:
    print("Estamos en otoño")
print()
"""