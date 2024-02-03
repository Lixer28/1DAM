# Víctor Quirós Pavón

# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia.
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

# Zona	Ubicación	     Costo/gramo
# 1	América del Norte	 24.00 euros
# 2	América Central	 20.00 euros
# 3	América del Sur	 21.00 euros
# 4	Europa	           10.00 euros
# 5	Asia	                18.00 euros
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

print ("Indique el peso (en gramos) del paquete")
peso = float(input())

if peso >= 5000:
    print ("Tanto peso no puede ser transportado")
else:
    print ("Indique hacia donde va dirigido el paquete "
       + "América (del Norte, Central, del Sur), "
       + "Europa o Asia")
    destino = str(input())

    if   destino == "América del Norte":
         precio = peso * 24
         print ("El precio del transporte es: " +str(precio) +" euros")

    elif destino == "América Central":
         precio = peso * 20
         print ("El precio del transporte es: " +str(precio) +" euros")

    elif destino == "América del Sur":
         precio = peso * 21
         print ("El precio del transporte es: " +str(precio) +" euros")

    elif destino == "Europa":
         precio = peso * 10
         print ("El precio del transporte es: " +str(precio) +" euros")

    elif destino == "Asia":
         precio = peso * 18
         print ("El precio del transporte es: " +str(precio) +" euros")

    