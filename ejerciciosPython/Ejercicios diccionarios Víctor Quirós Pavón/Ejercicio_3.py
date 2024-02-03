# Víctor Quirós Pavón

# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario.
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

seguir_quiros = True
diccionario_quiros = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}


while seguir_quiros == True:

    print("Escribe el nombre de la fruta:")
    fruta_quiros = input()
    print("Escribe la cantidad que se ha vendido de esa fruta:")
    cantfruta_quiros = float(input())
    

    if fruta_quiros not in diccionario_quiros:
        print("La fruta no existe")
    else:
        preciototal_quiros = diccionario_quiros[fruta_quiros] * cantfruta_quiros
        print("El precio final de la fruta es:",preciototal_quiros,"\n")
    
    print("¿Desea hacer otra consulta? 1 Si - 2 No")
    respuesta_quiros = int(input())
    if respuesta_quiros == 1:
        seguir_quiros = True
    elif respuesta_quiros == 2:
        seguir_quiros = False