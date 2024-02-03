# Víctor Quirós Pavón

# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número
# (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

nmayor_quiros = int
nmenor_quiros = int


num_quiros = random.randrange(1,100)

for i in range(1,10 + 1):
    
    print ("Escribe un número:")
    num2_quiros = int(input())
    print(" ")
    
    print("Este es el intento",i,"de 10")
    if  num_quiros > num2_quiros:
            print ("El número es mayor")
            num2_quiros = nmenor_quiros
            
    elif num2_quiros == num_quiros:
        print ("Has acertado")
        break
    else:
        print ("El número es menor")
        num2_quiros = nmayor_quiros

if i >= 10:
    print ("El número a adivinar era el",num_quiros)
else:
    print ("Has adivinado el número en",i,"intentos")