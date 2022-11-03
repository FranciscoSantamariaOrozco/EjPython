#Exercises - Day 9
print()

# 1- Haz que el usuario introduzca un imput ("Introduce tu edad"). Si el usuario tiene 18 o es mayor, 
# devuelve el mensaje: "Eres suficientemente mayor para aprender a conducir)"
# Si no, le indica los años que le faltan para poder comenzar.

Age = input("Introduce tu edad:")
Age = int(Age)

if Age >= 18:
    print("Eres suficientemente mayor para aprender a conducir!")
elif (18 - Age) <= 1: 
    print("Sólo te falta 1 año para poder aprender a conducir!")
else:
    print("Todavía te faltan", 18 - Age, "años para poder aprender a conducir...")
print()

# A mayores, como me parecia que quedaba feo que si el usuario tenia 17 años indicase "te faltan 1 años para aprender a conducir", 
# he añadido un elif para que si el usuario tiene 17 años, muestre un mensaje distinto animandole :)