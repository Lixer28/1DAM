# Víctor Quirós Pavón

# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import time

horas_quiros = 0
minutos_quiros = 0
segundos_quiros = 0

print ("Escribe un número que no sea 0")
inicia_quiros = int(input())

while inicia_quiros != 0:
    segundos_quiros = segundos_quiros + 1
    if segundos_quiros == 60:
        segundos_quiros = 0
        minutos_quiros = minutos_quiros + 1
        if minutos_quiros == 60:
            minutos_quiros = 0
            horas_quiros = horas_quiros + 1

    time.sleep(1)
    print (horas_quiros,":",minutos_quiros,":",segundos_quiros)