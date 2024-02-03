# Víctor Quirós Pavón

# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

print ("Escribe un número")
num1_quiros = int(input())
print ("Escribe un número mayor que el anterior")
num2_quiros = int(input())

for i in range (num1_quiros, num2_quiros +1):
    if  i % 2==0:
        print ("El número",i,"es par")