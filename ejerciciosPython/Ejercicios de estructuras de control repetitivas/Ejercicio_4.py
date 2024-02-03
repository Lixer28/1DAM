# Víctor Quirós Pavón

# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.


mayor_quiros = 0
menor_quiros = 0
igual_quiros = 0

print ("Cuántos números desea introducir")
cantnum_quiros = int(input())
print ("Escribe los",cantnum_quiros,"números")


for i  in range (cantnum_quiros):
    num_quiros = int(input())

    if num_quiros > 0:
        mayor_quiros = mayor_quiros + 1
    elif num_quiros < 0:
        menor_quiros = menor_quiros + 1
    else:
        igual_quiros = igual_quiros + 1

print ("La cantidad de números mayores que 0 es",mayor_quiros)
print ("La cantidad de números menores que 0 es",menor_quiros)
print ("La cantidad de números iguales que 0 es",igual_quiros)