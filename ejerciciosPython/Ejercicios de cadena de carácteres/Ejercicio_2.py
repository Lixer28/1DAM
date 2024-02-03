# Víctor Quirós Pavón

# Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.


print ("Escribe una subcadena")
subcadena_quiros = input()

print ("\nEscribe una cadena")
cadena_quiros = input()

if cadena_quiros.startswith(subcadena_quiros):
    print ("\nLa cadena empieza por la subcadena")
else:
    print ("\nLa cadena no empieza por la subcadena")