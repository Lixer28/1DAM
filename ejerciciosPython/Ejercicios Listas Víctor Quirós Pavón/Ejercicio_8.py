# Víctor Quirós Pavón

# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:

# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

listanombre_quiros = []
listaedad_quiros = []
medad_quiros = int(0)
maxedad_quiros = int(1)
seguir = True


while seguir == True:
    print("\nEscribe el nombre del alumno")
    nombre_quiros = input()
    if nombre_quiros != "*":
       listanombre_quiros.append(nombre_quiros) 
    else:
        break


    print("Escribe la edad del alumno")
    edad_quiros = int(input())
    if edad_quiros != "*":
        listaedad_quiros.append(edad_quiros)
    else:
        break
    
    if edad_quiros >= 18:
        medad_quiros = medad_quiros + 1

    if edad_quiros > maxedad_quiros:
        maxedad_quiros = edad_quiros
        
    

print("\nLos alumnos mayores de edad son:",medad_quiros)
print("Mayor de los mayores de edad:",maxedad_quiros)



