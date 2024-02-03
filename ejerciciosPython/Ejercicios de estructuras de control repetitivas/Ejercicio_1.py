# Víctor Quirós Pavón

# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1
# y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).

print("Introduce un número para calcular su factorial")
factorial_quiros = int(input())

print("Factorial:")
for i in range (factorial_quiros , 0, -1):
    resultado = factorial_quiros * i
    print (factorial_quiros,"x",i,"=",resultado)