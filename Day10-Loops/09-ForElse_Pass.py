# Day 10 - Loops.
print()
# For Else.
# Si queremos ejecutar algun mensaje cuando el bucle termina, podemos usar else.

# Syntax
"""
    for i in range(start, end, step)
        codigo
    else
        print("El bucle ha terminado")
"""
for i in range(11):
    print(i)
else:
    print("El bucle ha terminado en", i)
print()


# Pass
# En python cuando se requiere una declaración (después de los 2 puntos) pero no queramos ejecutar ningún código ahí, 
# podemos escribir la palabra clave "pass" para evitar errores.
# También puede ser usada como marcador, para futuras declaraciones.
"""
    for i in range(8)
        pass
"""