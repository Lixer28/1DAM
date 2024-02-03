# Víctor Quirós Pavón

# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores),
# y posterior ordene los elementos de menor a mayor.

import random

lista_quiros = []

for i in range (1,11):
    random_quiros = random.randint(1,10)
    lista_quiros.append(random_quiros)

lista_quiros.sort()

for i in lista_quiros:
    print(i)