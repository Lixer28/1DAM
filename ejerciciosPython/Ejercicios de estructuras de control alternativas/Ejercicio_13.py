# Víctor Quirós Pavón

# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

print ("Escribe una fecha (dia, mes y año) para saber si es correcta")
dia = int(input())
mes = int(input())
año = int(input())

if mes == 2:
    if dia > 0 and dia <=28:
        print ("La fecha " +str(dia) +"-" +str(mes) +"-" +str(año),"es correcta")
    elif  dia > 0 and dia <=29:
            print ("La fecha " +str(dia) +"-" +str(mes) +"-" +str(año),"es correcta siempre que el año sea bisiesto")
else:

    if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
        if dia > 0 and dia <=31:
            print ("La fecha " +str(dia) +"-" +str(mes) +"-" +str(año),"es correcta")
    else:
        if dia > 0 and dia <=30:
            print ("La fecha " +str(dia) +"-" +str(mes) +"-" +str(año),"es correcta")
        else:
            print ("Esa fecha no es valida, el mes elegido no tiene 31 días")

