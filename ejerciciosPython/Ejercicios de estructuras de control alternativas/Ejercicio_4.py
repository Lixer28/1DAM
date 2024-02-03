# Víctor Quirós Pavón

# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.


print ("Escribe un primer número")
num1 = int(input())
print ("Escribe un primer número")
num2 = int(input())

if num2 > 0:
    division = num1 / num2
    print ("La división es " +str(division))
elif num2 == 0:
    print ("Una división no se puede hacer entre 0")