print ("Introduce un número para asignar un valor a la letra A")
A = int(input())
print ("Introduce un número para asignar un valor a la letra B")
B = int(input())

A , B = B , A

print("El nuevo valor de A es " +str(A))
print("El nuevo valor de B es " +str(B))