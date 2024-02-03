# Víctor Quirós Pavón

# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

lista_quiros=[]

for i in range(1,6):
    print ("Escribe la cadena",i)
    cadena_quiros = input()
    lista_quiros.append(cadena_quiros)



lista_quiros.reverse()
print (lista_quiros)