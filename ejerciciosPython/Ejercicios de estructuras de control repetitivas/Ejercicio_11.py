# Víctor Quirós Pavón

# Escribe un programa que diga si un número introducido por teclado es o no primo.
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import math
esprimo_quiros = True

print ("Escribe un número para saber si es primo")
num_quiros = int(input())

for i in range (2, int(math.sqrt(num_quiros))+ 1):
    if num_quiros % i == 2:
        esprimo_quiros = False

if esprimo_quiros == True:
    print("El número es primo")
else:
    print("El número no es primo")