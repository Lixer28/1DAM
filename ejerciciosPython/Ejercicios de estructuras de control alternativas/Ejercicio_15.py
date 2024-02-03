# Víctor Quirós Pavón

# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y 
# cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, 
# el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, 
# el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

print ("Escribe cuántos alumnos irán al viaje de estudios")
alumnos = int(input())
costo = float(0)

if alumnos >= 100:
    costo = costo + 65
    print ("El alumno debe pagar 65 euros")

elif alumnos >=50 and alumnos <=99:
    costo = costo + 70
    print ("El alumno debe pagar 70 euros")

elif alumnos >=30 and alumnos <= 49:
    costo = costo + 95
    print ("El alumno debe pagar 95 euros")

else:
    costo = costo + 4000

costo = costo*alumnos
print ("A la compañía de viajes habrá que pagarle",costo,"euros")