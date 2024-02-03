# Víctor Quirós Pavón

# Crea una función “calcularMaxMin” que recibe una lista con
# valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo
# y el mínimo, utilizando la función anterior.

from funcion5 import calcularMaxMin

print("¿Cuántos valores desea introducir?")
numvalor_quiros = int(input())

lista_quiros = []
for i in range (numvalor_quiros):
    print("Escribe el valor %d: "%(i+1))
    valor_quiros = int(input())
    lista_quiros.append(valor_quiros)

print("El valor máximo y mínimo son:",calcularMaxMin(lista_quiros))