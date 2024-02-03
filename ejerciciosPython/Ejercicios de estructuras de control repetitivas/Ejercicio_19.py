# Víctor Quirós Pavón

# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

num_quiros = 0

while num_quiros != 4:
    print ("MENÚ PRINCIPAL")
    print ("Se encuentra en el menú, seleccione las distintas opciones:")
    print ("1. TELEVISIÓN")
    print ("2. RADIO")
    print ("3. APLICACIONES")
    print ("4. Salir")
    num_quiros = int(input())

    if num_quiros == 1:
        print ("MENÚ DE LA PRIMERA OPCIÓN - CANALES TELEVISIÓN")
        print ("Antena 3")
        print ("Telecinco")
        print ("4. Volver al menú principal")
        num2_quiros = int(input())

    elif num_quiros == 2:
        print ("MENÚ DE LA SEGUNDA OPCIÓN - CADENA DE RADIO")
        print ("CAD-100")
        print ("Los40")
        print ("4. Volver al menú principal")
        num3_quiros = int(input())
    
    elif num_quiros == 3:
        print ("MENÚ DE LA SEGUNDA OPCIÓN - APLICACIONES")
        print ("Netflix")
        print ("Disney+")
        print ("4. Volver al menú principal")
        num4_quiros = int(input())