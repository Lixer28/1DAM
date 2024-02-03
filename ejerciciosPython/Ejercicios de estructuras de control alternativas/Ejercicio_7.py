# Víctor Quirós Pavón

# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

print ("Escribe la base de la potencia")
base = int(input())
print ("Escribe el exponente de la potencia")
expo = int(input())

potencia = base ** expo

if  expo > 0:
    print ("La potencia es " +str(potencia))
elif expo == 0:
    print ("La potencia es 1")
elif expo < 0:
    resultado = 1/potencia
    print ("La potencia es " +str(potencia))