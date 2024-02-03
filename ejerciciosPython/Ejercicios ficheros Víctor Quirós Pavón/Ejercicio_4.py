# Víctor Quirós Pavón

# El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo al final del curso (convocatoria ordinaria). Realiza un programa que haga lo siguiente:

# Reciba el fichero de calificaciones.csv y devuelva una lista de listas, donde cada lista contiene
# la información de los exámenes y la asistencia de un alumno. Para ordenar la lista vamos a utilizar una función lambda:

            # ordenados = sorted(csv_reader,key=lambda x:x[0])
import csv

with open ("calificaciones.csv", "r") as f_quiros:
    contenido_quiros = csv.reader(f_quiros, delimiter=',')
    ordenados_quiros = sorted(contenido_quiros,key=lambda x:x[0])
    datos_quiros = list(ordenados_quiros)
    print(datos_quiros[1])
    print(datos_quiros[0])
    
    for i in range(2,17):
        print(datos_quiros[i])