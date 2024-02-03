# Víctor Quirós Pavón

# Escribir dos funciones que permitan calcular:

# La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# Escribe un programa principal con un menú donde se pueda elegir la opción
# de convertir a segundos, convertir a horas, minutos y segundos o salir del programa.


from funcion10 import calcularHora
from funcion10 import calcularSegundos

while True:
    print("----MENÚ----")
    print("1. Pasar a segundos")
    print("2. Pasar a, horas, minutos y segundos")
    print("3. Salir del menú")
    respuesta_quiros = int(input())
    
    if respuesta_quiros == 1:
        print("Escribe las horas:")
        horas_quiros = int(input())

        print("Escribe los minutos:")
        minutos_quiros = int(input())

        print("Escribe los segundos:")
        segundos_quiros = int(input())

        print(calcularSegundos(horas_quiros, minutos_quiros, segundos_quiros),"segundos")
    
    elif respuesta_quiros == 2:
        print("Escribe los segundos:")
        segundos_quiros = int(input())
        
        print(calcularHora(segundos_quiros))
    
    elif respuesta_quiros == 3:
        break
    else:
        print("Esa opción no se puede elegir, por favor elije una entre las opciones")
