# Víctor Quirós Pavón

# Vamos a realizar un programa similar al anterior para trabajar con una cola.
# Una cola es una estructura de datos que nos permite guardar un conjunto de variables.
# La característica fundamental es que el primer elemento que se añade al conjunto es el primero que se puede sacar.
# En realizada nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola que es la que tienes que modificar.

from funcion15 import LongitudCola, EstaVaciaCola, EstaLlenaCola, AddCola, SacarDeLaCola, EscribirCola
cola_quiros = []

while True:
    print("1. Añadir elemento a la cola")
    print("2. Sacar elemento de la cola")
    print("3. Longitud de la cola")
    print("4. Mostrar cola")
    print("5. Salir")
    respuesta_quiros = int(input())

    if respuesta_quiros == 1:
        print("Escribe el texto que quieras añadir:")
        texto_quiros = input()
        AddCola(texto_quiros, cola_quiros)
        print(" ")
        

    elif respuesta_quiros == 2:
        SacarDeLaCola(cola_quiros),"\n"

    elif respuesta_quiros == 3:
        print("La longitud de la pila es:",LongitudCola(cola_quiros),"\n")

    elif respuesta_quiros == 4:
        print(EscribirCola(cola_quiros),"\n")

    elif respuesta_quiros == 5:
        break

    else:
        print("Esa opción no es correcta, escribe una entre el rango de números (1-5)\n")