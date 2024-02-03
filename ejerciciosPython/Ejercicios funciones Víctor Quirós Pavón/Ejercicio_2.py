#Víctor Quirós Pavón

#Crea un programa que pida dos números enteros al usuario y
# diga si alguno de ellos es múltiplo del otro.
# Crea una función EsMultiplo que reciba los dos números,
# y devuelve si el primero es múltiplo del segundo.

from funcion2 import es_multiplo as multiplo

print("Escribe un número:")
num1_quiros = int(input())

print("Escribe otro número:")
num2_quiros = int(input())



if multiplo(num1_quiros, num2_quiros) == True:
    print("El primer número ES múltiplo del segundo")
else:
    print("El primer número NO ES múltiplo del segundo")