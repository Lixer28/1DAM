# Víctor Quirós Pavón

# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

diccionario_quiros = {}

while True:
    print("\nMenú:")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    

    print("Elige una opción (1-4):")
    opcion_quiros = int(input())

    if opcion_quiros == 1:
        print("Escribe un nombre")
        nombre_quiros = input()
        if nombre_quiros in diccionario_quiros:
            print("El número de teléfono asignado a", nombre_quiros, "es", diccionario_quiros[nombre_quiros])
            print("Quieres cambiar el número de teléfono (1-Si / 2-No)")
            modificar_quiros = int(input())
            if modificar_quiros == 1:
                telefono_quiros = input("Escribe el nuevo número de teléfono:")
                diccionario_quiros[nombre_quiros] = telefono_quiros
                print("El número de teléfono asignado a", nombre_quiros, "es", diccionario_quiros[nombre_quiros])
            
        else:
            print("El contacto no está registrado")
            print("Escribe el número de teléfono que se asignará a",nombre_quiros,":")
            telefono_quiros = int(input())
            diccionario_quiros[nombre_quiros] = telefono_quiros
            print("El contacto",nombre_quiros,"ha sido añadido a la agenda")

    elif opcion_quiros == 2:
        print("Escribe una cadena para buscarla en la agenda:")
        cadena_quiros = input()
        for nombre_quiros in diccionario_quiros:
            if nombre_quiros.startswith(cadena_quiros):
                print("Nombre:", nombre_quiros)
                print("Número de teléfono:", diccionario_quiros[nombre_quiros])

    elif opcion_quiros == 3:
        print("Escribe el nombre del contacto:")
        nombre_quiros = input()
        if nombre_quiros in diccionario_quiros:
            print("¿Quieres borrar de la agenda a",nombre_quiros,"? (1-Si / 2-No):")
            confirmacion_quiros = int(input())
            if confirmacion_quiros == 1:
                del diccionario_quiros[nombre_quiros]
                print(nombre_quiros, "ha sido eliminado de la agenda")
        else:
            print("En la agenda no está",nombre_quiros)


    elif opcion_quiros == 4:
        if diccionario_quiros.keys():
            print("Contactos guardados:")
            for nombre_quiros, telefono_quiros in diccionario_quiros.items():
                print("Nombre:", nombre_quiros)
                print("Número de teléfono:", diccionario_quiros[nombre_quiros],"\n")
        else:
            print("La agenda está vacía")