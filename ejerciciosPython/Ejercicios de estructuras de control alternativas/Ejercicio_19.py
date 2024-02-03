# Víctor Quirós Pavón

# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

print ("Escribe un número del 1 al 12 para saber cuantos días tiene ese mes")


mes = int(input())
if mes == 1:
    print ("31")
elif mes == 2:
    print ("28, 29 si es bisiesto")
elif mes == 3:
    print ("31")
elif mes == 4:
    print ("30")
elif mes == 5:
    print ("31")
elif mes == 6:
    print ("30")
elif mes == 7:
    print ("31")
elif mes == 8:
    print ("31")
elif mes == 9:
    print ("30")
elif mes == 10:
    print ("31")
elif mes == 11:
    print ("30")
elif mes == 12:
    print ("31")
else:
    mes < 12
    print ("El número de mes introducido no es válido, el intervalo es entre 1 y 12")
