# Víctor Quirós Pavón

# Escribe un programa en python que lea el fichero json libreria.json con datos de
# nuestra librería y muestre en la terminal cuántos libros hay en la librería.

import json

with open ("libreria.json","r") as f_quiros:
    libreria_quiros = json.load(f_quiros)
    
    libros = libreria_quiros["bookstore"]["book"]
    numlibros_quiros = len(libros)

    print("\nEn la librería hay",numlibros_quiros,"libros\n")