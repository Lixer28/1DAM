# Víctor Quirós Pavón

# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:

# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.

listamin_quiros = []
listamax_quiros = []
cont_quiros = 0
tempmin_quiros = int(0)
tempmax_quiros = int(0)

for i in range (1,6):
    print("Introduzca temperatura minima del día",i,":")
    minima_quiros = int(input())

    print("Introduzca temperatura maxima del día",i,":")
    maxima_quiros = int(input())

    listamin_quiros.append(minima_quiros)
    listamax_quiros.append(maxima_quiros)
    
    media_quiros = (listamin_quiros[cont_quiros] + listamax_quiros[cont_quiros]) /2
    cont_quiros = cont_quiros + 1

    if minima_quiros > tempmin_quiros:
        tempmin_quiros = minima_quiros
    if maxima_quiros > tempmax_quiros:
        tempmax_quiros = maxima_quiros
print(" ")

for i in range (1,6):
    print("La media del día",i,"es",media_quiros)



print("El día con el mínimo de temperatura es",min(listamin_quiros))




print("\nEscribe una temperatura")
temperatura_quiros = int(input())

diastemperatura_quiros = []

for i in range(len(listamax_quiros)):
    if listamax_quiros[i] == temperatura_quiros:
        diastemperatura_quiros.append(i + 1)

if diastemperatura_quiros == temperatura_quiros:
    print("Los días que coinciden con la temperatura son:", diastemperatura_quiros)
else:
    print("No hay ningún día con esa temperatura máxima.")

