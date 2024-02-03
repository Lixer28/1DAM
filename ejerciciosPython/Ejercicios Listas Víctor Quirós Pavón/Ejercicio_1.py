# Víctor Quirós Pavón

# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente
# muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random
lista_quiros = []

print ("Número", end= "        ")
print ("Cuadrado", end= "          ")
print ("Cúbico", end= "        \n")

for i in range(1, 11):
    random_quiros = random.randint(1,10)
    lista_quiros.append(random_quiros)
    print (random_quiros,end="                ")
    print ((random_quiros*2),end="               ")
    print ((random_quiros*3),end="\n")