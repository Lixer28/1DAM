# Víctor Quirós Pavón

# Escribe un programa en python que lea el fichero json pedidos.json con datos de ordenes, a continuación deberá
# crear otro fichero primerapellido_clientes.json con los todos los datos de los clientes.

import json
clientes_quiros = []

with open ("pedidos.json", "r") as f_quiros:
    pedidos_quiros = json.load(f_quiros)

    for orden in pedidos_quiros["ordenes"]:
        clientes_quiros.append(orden["cliente"])
    
    with open("quiros_clientes.json", "w") as f_quiros:
        json.dump(clientes_quiros, f_quiros, indent=4)