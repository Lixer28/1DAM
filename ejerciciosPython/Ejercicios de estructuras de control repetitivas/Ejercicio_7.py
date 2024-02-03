# Víctor Quirós Pavón

# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

resultado_quiros = int

print ("Escribe un número para saber su tabla de multiplicar")
num_quiros = int(input())


for i in range (1, 11):
    resultado_quiros = num_quiros * i
    print (num_quiros,"x",i,"=",resultado_quiros)