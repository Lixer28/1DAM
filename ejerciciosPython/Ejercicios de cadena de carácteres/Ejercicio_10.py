# Víctor Quirós Pavón

# Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.

print ("Escribe una cadena")
cadena_quiros = input()

invertir_quiros = cadena_quiros[::-1]
print(invertir_quiros)

if cadena_quiros == invertir_quiros:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")