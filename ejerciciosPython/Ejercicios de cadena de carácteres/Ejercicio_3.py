# Víctor Quirós Pavón

# Pide una cadena y un carácter por teclado (valida que sea un carácter)
# y muestra cuantas veces aparece el carácter en la cadena.

print ("Escribe una cadena")
cadena_quiros = input()

print ("Escribe un carácter")
caracter_quiros = input()

while len(caracter_quiros) != 1:
    print ("Has escrito más de un carácter. Escribe solo uno")
    print ("Escribe un carácter")
    caracter_quiros = input()

aparece_quiros = cadena_quiros.count(caracter_quiros)
print (aparece_quiros)