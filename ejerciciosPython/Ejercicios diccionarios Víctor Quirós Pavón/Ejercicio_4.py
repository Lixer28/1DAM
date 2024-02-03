# Víctor Quirós Pavón

# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
# Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y
# los valores serán listas con las notas de cada alumno. El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas
# hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.


diccionario_quiros = {}
notas_quiros = []
print("Escribe cuantos alumnos se van a introducir:")
numalum_quiros = int(input())

for i in range (0,numalum_quiros):
    print("Escribe el nombre del alumno:")
    nombre_quiros = input()

    while True:
        print("Escribe la nota del alumno (negativo para finalizar):")
        nota_quiros = int(input())

        if nota_quiros >= 0:
            notas_quiros.append(nota_quiros)
            
        else:
            diccionario_quiros[nombre_quiros]=nota_quiros
            break

    notamedia_quiros = sum(notas_quiros)/len(notas_quiros)
    print("Nombre del alumno:",nombre_quiros, "\n Nota media del alumno:",notamedia_quiros)