# Víctor Quirós Pavón

# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

print ("Introduce un número para asignar el valor a cada letra (A, B y C)")
A = int(input())
B = int(input())
C = int(input())

if (A^2 + B^2) == C^2:
    print ("El triángulo es rectángulo")
elif (A == B) and (B == C):
    print ("El triángulo es equilátero")
elif (A == B) or (A == C) or (B == C):
    print ("El triángulo es isósceles")
else:
    print ("El triángulo es escaleno")
    