# Víctor Quirós Pavón

# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

print ("Escribe una serie de letras")
letras_quiros = str(input())

vocal_quiros = ["a","e","i","o","u"]

if letras_quiros in vocal_quiros:
    print ("La letra es vocal")
else:
    print ("La letra no es vocal, es una consonante")

while letras_quiros != (" "):
    letras_quiros = str(input())
    if letras_quiros in vocal_quiros:
        print ("La letra es vocal")
    else:
        print ("La letra no es vocal, es una consonante")