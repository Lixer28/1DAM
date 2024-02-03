# Víctor Quirós Pavón

# Crear un programa que añada números a una lista hasta que introducimos un número negativo.
# A continuación debe crear una nueva lista igual que la anterior pero el iminando los números duplicados.
# Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.


lista_quiros = []

print("Escribe un número")
num_quiros = int(input())

while num_quiros >= 0:
    lista_quiros.append(num_quiros)

    print("Escribe un número")
    num_quiros = int(input())

print(lista_quiros)

lista2_quiros = []
for num_quiros in lista_quiros:
    if num_quiros not in lista2_quiros:
        lista2_quiros.append(num_quiros)

print("Lista sin duplicados:", lista2_quiros)