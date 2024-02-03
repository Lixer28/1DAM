# Víctor Quirós Pavón

# Vamos a crear un programa que tenga el siguiente menú:

# 1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3. Longitud de la lista: te muestra el número de elementos de la lista.
# 4. Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# 6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# 7. Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# 8. Mostrar números: Muestra los números de la lista
# 9. Salir

menu_quiros = []

while True:
    while True:
        print("\tMENU")
        print("1. Añadir número a la lista")
        print("2. Añadir número de la lista en una posición")
        print("3. Longitud de la lista")
        print("4. Eliminar el último número")
        print("5. Eliminar un número")
        print("6. Contar números")
        print("7. Posiciones de un número")
        print("8. Mostrar números")
        print("9. Salir")
        print ("\nEscribe un número para moverte por el menú:")
        num_quiros = int(input())
        if num_quiros >= 1 or num_quiros <= 9:
            break
        else:
            print("El número debe estar dentro del rango (1-9)")
            break
        
    if num_quiros == 1:
        print("Escribe un número para añadir a la lista:")
        añadirnum1_quiros = int(input())
        menu_quiros.append(añadirnum1_quiros)
        print("\n Lista del menu:","\n",menu_quiros)
    
    elif num_quiros == 2:
        print("Escribe un número:")
        añadirnum2_quiros = int(input())
        print("Escribe una posición:")
        pos_quiros = int(input())

        if pos_quiros <= len(menu_quiros):
            menu_quiros.append(pos_quiros)
            print(menu_quiros)
        else:
            print("La posición no existe dentro de la lista")
    
    elif num_quiros == 3:
        print("La lista tiene",len(menu_quiros),"elementos")
    
    elif num_quiros == 4:
        menu_quiros.pop()
        print(menu_quiros)
    
    elif num_quiros == 5:
        print("Escribe una posición:")
        pos2_quiros = int(input())

        if pos2_quiros <= len(menu_quiros):
            menu_quiros.pop(pos2_quiros-1)
            print(menu_quiros)
        else:
            print("La posición no existe dentro de la lista")
    
    elif num_quiros == 6:
        print("Escribe un número:")
        añadirnum3_quiros = int(input())
        print(menu_quiros.count(añadirnum3_quiros))

    elif num_quiros == 7:
        print("Escribe un número para saber su posición:")
        pos3_quiros = int(input())
        print(menu_quiros.index(pos3_quiros)+1)

    elif num_quiros == 8:
        print(menu_quiros)

    elif num_quiros == 9:
        break
