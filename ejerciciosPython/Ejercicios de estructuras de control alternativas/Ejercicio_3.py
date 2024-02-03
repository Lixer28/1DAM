# Víctor Quirós Pavón

# Escribe un programa que lea un número e indique si es par o impar.


print ("Escribe un primer número")
num = int(input())

if  num % 2 == 0:
    print ("El número " +str(num) +" es par")
else:
    print ("El número " +str(num) +" es impar")