# Víctor Quirós Pavón

# Realice un programa que reciba de nuevo el fichero calificaciones.csv para añadir a cada lista de cada alumno un nuevo elemento,
# será la Nota Final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.
# Si el alumno ha realizado alguna recuperación ordinaria, para el cálculo de la nota final se tomará esta como última nota del alumno.
# Se deberá mostrar finalmente en la terminal la lista ordenada y será guardada en un fichero que se llamará calificacionfinal.csv

import csv
lista_quiros = []
alumno_quiros = []

cabecera_quiros = ["Apellidos","Nombre","Asistencia","Parcial1","Parcial2","Ordinario1","Ordinario2","Practicas","OrdinarioPracticas","NotaFinal"]

with open("calificaciones.csv", "r") as f_quiros:
    csv_reader = csv.reader(f_quiros, delimiter=',')
    lista_quiros = list(csv_reader)

    for alumno_quiros in lista_quiros:
        teoria_quiros = (float(alumno_quiros[3]) + float(alumno_quiros[4])) * 0.3
        practicas = float(alumno_quiros[7]) * 0.4

        if alumno_quiros[8]:
            notafinal_quiros = float(alumno_quiros[8])
        else:
            notafinal_quiros = max(teoria_quiros, practicas)
        
        alumno_quiros.append(str(notafinal_quiros))
        

with open('calificacionfinal.csv', 'w') as f_quiros:
    for i in alumno_quiros:
        for i in range(len(i)):
            if i != len(i) - 1:
                f_quiros.write(i[i] + ',')
            else:
                f_quiros.write(i[i] + '\n')