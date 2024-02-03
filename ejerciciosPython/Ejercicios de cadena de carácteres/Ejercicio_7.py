# Víctor Quirós Pavón

# Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.

print("Escribe una cadena")
cadena_quiros = input()
print("Escribe un primer carácter")
caracter1_quiros = input()
print("Escribe un segundo carácter")
caracter2_quiros = input()

while len(caracter1_quiros) != 1:
    print ("Has escrito más de un carácter, escribe solo uno")
    print ("Escribe el primer carácter")
    caracter1_quiros = input()

while len(caracter2_quiros) != 1:
    print ("Has escrito más de un carácter, escribe solo uno")
    print ("Escribe el segundo carácter")
    caracter2_quiros = input()


for caracter in cadena_quiros:
    if caracter == caracter1_quiros:
        print (caracter2_quiros, end="")
    else:
        print(caracter,end="")