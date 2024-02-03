# Víctor Quirós Pavón

# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo.

cierto_quiros = bool (True)
verdad_quiros = bool (True)
suma_quiros = int(0)
mayor_quiros = int(0)
fuerarango_quiros = int(0)
igualrango_quiros = int(0)

print ("Escribe un número (límite inferior del rango)")
num1_quiros = int(input())

while verdad_quiros == True:
    print ("Escribe un número (límite superior del rango)")
    num2_quiros = int(input())
    if num2_quiros > num1_quiros:
        verdad_quiros == False
        break
    else:
        print ("El número",num1_quiros,"es mayor que el",num2_quiros,"debe ser al revés")
 
 
for i in range (num1_quiros, num2_quiros + 1):
    suma_quiros = sum(range(num1_quiros, num2_quiros +1))

        
print ("Escribe una serie de números para recopilar datos (escribir 0 para salir)")
while cierto_quiros == True:
    num_quiros = float(input())
    if num_quiros == 0:
        cierto = False
        break
    elif num_quiros < num1_quiros:
        fuerarango_quiros = fuerarango_quiros + 1
    elif num_quiros > num2_quiros:
        fuerarango_quiros = fuerarango_quiros + 1
    elif num_quiros == num1_quiros:
        igualrango_quiros = igualrango_quiros + 1
    elif num_quiros == num2_quiros:
        igualrango_quiros = igualrango_quiros + 1
    
print ("Suma de números del intervalo:",suma_quiros)
print ("Números introducidos fuera de rango:",fuerarango_quiros)
print ("Números introducidos igual al número del rango:",igualrango_quiros)