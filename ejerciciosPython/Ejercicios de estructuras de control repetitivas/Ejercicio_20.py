# Víctor Quirós Pavón

# Mostrar en pantalla los N primero número primos.
# Se pide por teclado la cantidad de números primos que queremos mostrar.

print ("Escribe un número para mostrar tantos números primos")
numero_quiros = int(input())
cont_quiros = 0
num_quiros = 2

while cont_quiros < numero_quiros:
    primo_quiros = True
    for i in range(2, num_quiros):
        if num_quiros % i == 0:
            primo_quiros = False
            break
    if primo_quiros == True:
        print (num_quiros,"es primo")
        cont_quiros = cont_quiros + 1
    num_quiros = num_quiros + 1