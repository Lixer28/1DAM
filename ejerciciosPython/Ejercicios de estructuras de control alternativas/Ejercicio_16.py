# Víctor Quirós Pavón

# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura,
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos,
# y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
# en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.


print ("Indique el tiempo (en minutos) que duró su llamada")
tiem = float(input())
print ("Indique el día de la llamada de la semana (1 al 7)")
dia = int(input())
print ("Indique si la llamada se realizó en el turno de mañana (1) o tarde (2) ")
turno = int(input())

precio = float(0)
impuestos = float


# En cuanto al precio de las llamadas, al no estar seguro de lo que se refiere el ejercicio,
# si pasados los 5 minutos el precio se incrementa en 80 céntimos por cada minuto o se incrementa por los 3 próximos,
# he escogido uno de estos casos, en concreto el segundo.


if tiem <= 5:
    precio = precio + 1
elif (tiem >5) and (tiem <=8):
    precio = precio + 1.80
elif (tiem >8) and (tiem <=10):
    precio = precio + 2.50
else:
    precio = precio + 3.00

if dia == 7:
    impuestos = precio * 0.3
    precio = precio + impuestos
else:
    if turno == 1:
        impuestos = precio * 0.15
        precio = precio + impuestos
    elif turno == 2:
        impuestos = precio * 0.10
        precio = precio + impuestos

print ("Deberá pagar por la llamada deberá pagar "+ str(precio) +" euros")