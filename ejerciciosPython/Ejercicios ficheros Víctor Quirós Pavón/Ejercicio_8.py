# Víctor Quirós Pavón

# Escribe un programa en python que lea el fichero json colores.json con datos de colores,
# deberá mostrar en la terminal todos los nombres de colores, sus códigos rgba y hexadecimal respectivamente.

import json

with open("colores.json", "r") as f_quiros:
    colores_quiros = json.load(f_quiros)

    for color in colores_quiros["colors"]:
        nomcolor = color["color"]
        rgba = color["code"]["rgba"]
        hex_code = color["code"]["hex"]

        print("Color:",nomcolor)
        print("RGBA:",rgba)
        print("Hexadecimal:", hex_code)
        print()
        
