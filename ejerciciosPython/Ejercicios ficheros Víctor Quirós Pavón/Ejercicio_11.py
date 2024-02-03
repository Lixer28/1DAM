# Víctor Quirós Pavón


# Escribe un programa en python que lea el fichero gazpacho.json con datos su origen e ingredientes,
# a continuación deberá crear otro fichero primerapellido_ingredientes.json con los todos los datos de sus ingredientes.

import json

with open("gazpacho.json","r") as f_quiros:
    gazpacho_quiros = json.load(f_quiros)
    ingredientes_quiros = gazpacho_quiros["ingredientes"]

    with open ("quiros_ingredientes.json","w") as f_quiros:
        json.dump(ingredientes_quiros, f_quiros, indent=4)