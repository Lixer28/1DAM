# Víctor Quirós Pavón

# Escribe un programa en python que lea el fichero *movies.json con datos de películas.
# A continuación deberá crear un fichero primerapellido_peliculasaventuras.json con los títulos de las películas cuyo género incluya aventura.

import json
peliculasAventura_quiros = []

with open ("movies.json","r") as f_quiros:
    movies_quiros = json.load(f_quiros)

    for i in movies_quiros:
        if "Adventure" in i["genres"]:
            peliculasAventura_quiros.append(i["title"])

with open ("quiros_peliculasAventura_quiross.json","w") as f_quiros:
    json.dump(peliculasAventura_quiros, f_quiros, indent=4)