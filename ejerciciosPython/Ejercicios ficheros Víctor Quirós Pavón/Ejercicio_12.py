# Víctor Quirós Pavón

# Escribe un programa en python que lea el fichero *movies.json con datos de películas.
# A continuación deberá crear un fichero primerapellido_pelicula1994.json con los títulos de las películas que se hayan estrenado en 1994.

import json
peliculas_quiros = []

with open ("movies.json","r") as f_quiros:
    movies_quiros = json.load(f_quiros)
    
    for i in movies_quiros:
        if i["year"] == "1994":
            peliculas_quiros.append(i["title"])

with open ("quiros_pelicula1994.json","w") as f_quiros:
    json.dump(peliculas_quiros, f_quiros, indent=4)