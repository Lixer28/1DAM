# Víctor Quirós Pavón

# Algoritmo que pida números hasta que se introduzca un cero.
# Debe imprimir la suma y la media de todos los números introducidos.

suma_quiros = float(0)
media_quiros = float(0)
cierto_quiros = bool (True)
cont_quiros = 0

print ("Escribe una serie números")
while cierto_quiros == True:
    num_quiros = float(input())
    if num_quiros == 0:
        break
    else:
        suma_quiros = suma_quiros + num_quiros
        cont_quiros = cont_quiros + 1

media_quiros = suma_quiros / cont_quiros
print ("La suma de los números es:",suma_quiros)
print ("La media de los números es:",media_quiros)