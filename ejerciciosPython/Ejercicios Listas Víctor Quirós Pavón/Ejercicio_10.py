# Víctor Quirós Pavón

# Diseñar el algoritmo correspondiente a un programa, que:

# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

import random

tabla_quiros = []

for i in range (5):
    fila_quiros = []
    for j in range(5):
        print(f"Escribe el valor para [{i+1}][{j+1}]: ")
        valor_quiros = random.randint(1,5)
        fila_quiros.append(valor_quiros)
    tabla_quiros.append(fila_quiros)

print(" ")

for fila_quiros in tabla_quiros:
    for valor_quiros in fila_quiros:
        print("",valor_quiros,"\n",)

    print(" ")

for i in range(5):
    suma_fila_quiros = sum(tabla_quiros[i])
    print(f"La suma de la fila {i+1} es: {suma_fila_quiros}")

print(" ")


for j in range(5):
    suma_columna_quiros = sum(tabla_quiros[i][j] for i in range(5))
    print(f"La suma de la columna {j+1} es: {suma_columna_quiros}")