# Víctor Quirós Pavón

# Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150,
# los coches tienen sentido opuesto y tienen la misma velocidad.
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

km1_quiros = 70
km2_quiros = 150

while km1_quiros != km2_quiros:
    km1_quiros = km1_quiros +1
    km2_quiros = km2_quiros -1

print ("Ambas personas se encontrarán en el km",km2_quiros)