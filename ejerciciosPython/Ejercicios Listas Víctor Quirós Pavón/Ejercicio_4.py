# Víctor Quirós Pavón

# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo.
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

lista_quiros=[]

print("Escribe números y uno negativo para detener el programa")
num_quiros = int(input())
while num_quiros > 0:
    if num_quiros > 0:
        num_quiros = int(input())
        lista_quiros.append(num_quiros)

lista_quiros.pop()
print(lista_quiros)