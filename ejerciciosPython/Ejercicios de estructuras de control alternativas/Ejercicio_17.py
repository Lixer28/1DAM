# Víctor Quirós Pavón

# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.


print ("Escribe el número obtenido al tirar el dado")
num = int(input())

if (num == 1):
    print("Seis")
elif (num == 2):
    print ("Cinco")
elif (num == 3):
    print ("Cuatro")
elif (num == 4):
    print ("Tres")
elif (num == 5):
    print ("Dos")
elif (num == 6):
    print ("Uno")
else:
    print ("ERROR: número incorrecto")

