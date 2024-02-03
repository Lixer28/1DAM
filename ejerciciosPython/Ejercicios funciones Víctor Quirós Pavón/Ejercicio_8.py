# Víctor Quirós Pavón

# Crear una función recursiva que permita calcular el factorial
# de un número. Realiza un programa principal donde se lea un
# entero y se muestre el resultado del factorial.

from funcion8 import factorial

print("Escribe un número entero positivo:")
num_quiros = int(input())

respuesta_quiros = factorial(num_quiros)

if num_quiros < 0:
    print("Lo siento, el número es negativo")
else:
    print("El factorial de",num_quiros,"es",factorial(num_quiros))
