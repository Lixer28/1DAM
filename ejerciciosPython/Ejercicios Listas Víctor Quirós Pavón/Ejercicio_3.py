# Víctor Quirós Pavón

# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notamax_quiros = int(0)
notamin_quiros = int(0)
notasum_quiros = int(0)
notamedia_quiros = float(0)


lista_quiros=[]
for i in range (1,6):
    print ("Escribe la nota", i)
    nota_quiros = float(input())
    lista_quiros.append(nota_quiros)
    notasum_quiros = notasum_quiros + nota_quiros

if nota_quiros < 0 and nota_quiros > 10:
    print ("Número no válido, debe ser entre 0 y 10")

print("\n")
print ("Las notas introducidas son:",lista_quiros)
print("\n")

for i in range(0,11):
    notamax_quiros = max(lista_quiros)
    notamin_quiros = min(lista_quiros) 


notamedia_quiros = notasum_quiros / 5

print ("La nota máxima es:",notamax_quiros)
print ("La nota minima es:",notamin_quiros)
print ("La nota media es:",notamedia_quiros)