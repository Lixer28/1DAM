# Víctor Quirós Pavón

# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.


print ("Escribe una subcadena")
subcadena_quiros = input()

print ("Escribe una cadena")
cadena_quiros = input()


if subcadena_quiros in cadena_quiros:
    print ("La subcadena",'"'+subcadena_quiros+'"',"está dentro de la cadena")
else:
    print ("La subcadena",subcadena_quiros,"no está dentro de la cadena")