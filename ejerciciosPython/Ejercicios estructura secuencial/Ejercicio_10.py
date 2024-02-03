print ("Escriba las notas de los parciales para conocer su calificación final")
caliparcial1 = float(input())
caliparcial2 = float(input())
caliparcial3 = float(input())

media= (caliparcial1 + caliparcial2 + caliparcial3) / 3
media = media*0.55

print ("Escribe la califiación obtenida en el examen final")
caliexamen = float(input())
caliexamen = caliexamen*0.30

print ("Escribe la califiación obtenida en el trabajo final")
calitrab = float(input())
calitrab = calitrab*0.15

print ("El promedio de las 3 calificaciones parciales, con un 55 por ciento de la "
       "nota es de "+str(media))
print ("La calificación del examen final con un 30 por ciento de la nota es de "+str(caliexamen))
print ("La calificación del trabajo final con un 15 por ciento de la nota es de "+str(calitrab))