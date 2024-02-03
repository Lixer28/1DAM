# Víctor Quirós Pavón

# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número,
# y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

contador_quiros = 1

print("Escribe un número entre 1 y 10:")
n = int(input())

print("Escribe otro número entre 1 y 10:")
m = int(input())


nombre_quiros = "quiros-" + str(n)+ ".txt"

with open (nombre_quiros, 'r') as f_quiros:
    
    for i in f_quiros:
        if contador_quiros == m:
            print(i)
        contador_quiros = contador_quiros + 1