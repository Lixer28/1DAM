# Víctor Quirós Pavón

# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

print ("Escribe un primer número")
num1 = int(input())
print ("Escribe un segundo número")
num2 = int(input())
print ("Escribe un tercer número")
num3 = int(input())

if num1 > num2:
    if num1 > num3:
        
        print ("El número mayor es " +str(num1))
    else:
        
        print ("El número mayor es " +str(num3))
else:
    if num2 > num3:

        print ("El número mayor es " +str(num2))
    else:
        print ("El número mayor es " +str(num3))