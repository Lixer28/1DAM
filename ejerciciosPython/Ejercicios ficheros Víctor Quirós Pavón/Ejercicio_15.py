# Víctor Quirós Pavón

# Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería,
# recibe por teclado un límite inferior y superior para el precio y muestre en la terminal todos los
# libros cuyo precio esta en ese intervalo.

import json

with open ("libreria.json","r") as f_quiros:
    libreria_quiros = json.load(f_quiros)

    print("Escribe el límite inferior de precio:")
    linferior_quiros = float(input())

    print("Escribe el límite superior de precio:")
    lsuperior_quiros = float(input())

    libros_quiros = libreria_quiros["bookstore"]["book"]

    print()
    for i in libros_quiros:
        precio_quiros = float(i["price"])
    
        if linferior_quiros <= precio_quiros and precio_quiros <= lsuperior_quiros:
            print("Título:", i['title']['__text'])
            print("Precio:", precio_quiros,"\n")