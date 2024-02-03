# Víctor Quirós Pavón

# Escribe un programa en python que lea el fichero json pedidos.json con datos de órdenes,
# deberá mostrar en la terminal todos las órdenes de pedidos que no se hayan entregado.

import json

with open ("pedidos.json", "r") as f_quiros:
    pedidos_quiros = json.load(f_quiros)

    for orden in pedidos_quiros["ordenes"]:
        if orden["delivery"] == False:
            print(orden,end=" ")
            print()