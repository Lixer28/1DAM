# Víctor Quirós Pavón

# Crear una función que calcule la temperatura media de un día
# a partir de la temperatura máxima y mínima. Crear un programa
# principal, que utilizando la función anterior, vaya pidiendo 
# la temperatura máxima y mínima de cada día y vaya mostrando
# la media. El programa pedirá el número de días que se van a introducir.


from funcion3 import tempmedia as media_quiros

print("¿Cuántos días quieres introducir?")
dias_quiros = int(input())

for i in range(dias_quiros):

    print("\nEscribe la temperatura máxima del día",(i+1),":")
    maxima_quiros = float(input())

    print("Escribe la temperatura mínima del día",(i+1),":")
    minima_quiros = float(input())

    print("La media de las temperaturas es:",media_quiros(maxima_quiros,minima_quiros),"ºC")