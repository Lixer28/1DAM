# Víctor Quirós Pavón

# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
# circunferencias y las clasifique en uno de estos estados:

# exteriores
# tangentes exteriores
# secantes
# tangentes interiores
# interiores
# concéntricas

import math

print ("Escribe los puntos centrales x1, y1, x2, y2")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print ("Escribe los radios de 2 circunferencias, r1, r2")
r1 = int(input())
r2 = int(input())

dist = math.sqrt((x2-x1)^2 + (y2-y1)^2)

if dist > (r1 + r2):
    print ("Exteriores")
elif dist < (x1+x2) and dist > (x1-x2):
    print ("Secantes")
elif dist > 0 and dist < (r1+r2):
    print ("Interiores")
elif dist == (x1+x2):
    print ("Tangentes Exteriores")
elif dist == (r1-r2):
    print ("Tangentes Interiores")
elif dist == 0:
    if dist == 0 and r1 != r2:
        print ("Son concéntricas")
    elif dist == 0 and r1 == r2:
        print ("Son iguales")
