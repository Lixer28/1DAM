# Víctor Quirós Pavón

# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado,
# y los valores sean los cuadrados de las claves.

print("Escribe un número")
num_quiros = int(input())

diccionario_quiros = {}

for i in range(1, num_quiros +1):
    diccionario_quiros[i] = i ** 2
    print(diccionario_quiros)