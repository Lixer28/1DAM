# Víctor Quirós Pavón

# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre primer apellido-n.txt
# la tabla de multiplicar de ese número, donde n es el número introducido.

print("Escribe un número entero entre 1 y 10:")
respuesta_quiros = int(input())

nombre_quiros = "quiros-" + str(respuesta_quiros)+ ".txt"

with open(nombre_quiros,'w') as f_quiros:
    for i in range (1,11):
        print(respuesta_quiros,"x",i,"=",respuesta_quiros*i, file= f_quiros)