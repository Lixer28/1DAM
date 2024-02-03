# Víctor Quirós Pavón

# Escribir una función que pida un número entero entre 1 y 10, lea el fichero primerapellido-n.txt
# con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla.
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

print("Escribe un número entre 1 y 10:")
n = int(input())

nombre_quiros = "quiros-" + str(n)+ ".txt"

with open (nombre_quiros,'w') as f_quiros:
    for i in range (1,11):
        
        print(n,"x",i,"=",n*i, file= f_quiros)
