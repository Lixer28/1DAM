# Víctor Quirós Pavón

# Algoritmo que pida un número y diga si es positivo, negativo o 0.


print ("Escribe un número para saber si es positivo, negativo o 0")
num1 = int(input())

if num1 < 0:
    print ("El número es negativo")
elif num1 == 0:
        print ("El número es igual que 0")
else:
    print ("El número es positivo")