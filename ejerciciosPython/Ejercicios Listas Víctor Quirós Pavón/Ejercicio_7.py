# Víctor Quirós Pavón

# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno,
# pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

print("Escribe 5 valores para la lista 1")
lista1_quiros = []
for i in range (1,6):
    lista1_quiros.append(int(input()))

print("\nEscribe 5 valores para la lista 2")
lista2_quiros = []
for i in range (1,6):
    lista2_quiros.append(int(input()))


lista3_quiros = []

for i in range (0,5):
    lista3_quiros.append (lista1_quiros[i] + lista2_quiros[i])


print("Lista 3:",lista3_quiros)