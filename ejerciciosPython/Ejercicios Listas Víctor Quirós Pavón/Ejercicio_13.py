# Víctor Quirós Pavón

# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
  # Nombre: Lista para guardar los nombres de los conductores.
  # kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

km_quiros = []
kms_quiros = []
nombre_quiros = []
kms_total_quiros = []
dias_quiros = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
nombreconductor_quiros = []

kmdia_quiros = []

while True:
    print("Escribe los conductores que hay en la empresa:")
    numeroconductores_quiros = int(input())

    if numeroconductores_quiros > 0:
        break

for i in range(1, numeroconductores_quiros + 1):
    print(f"Escribe el nombre del conductor {i}:")
    nombre_conductor = input()
    nombreconductor_quiros.append(nombre_conductor)
    
    kmdia_quiros = []
    
    for dia in dias_quiros:
        km_dia = int(input(f"Escribe los kilómetros realizados el día {dia} por {nombre_conductor}: "))
        kmdia_quiros.append(km_dia)
    
    km_quiros.append(kmdia_quiros)


for i in km_quiros:
    kms_total_quiros.append(sum(i))


for nombre_quiros, kms_total_quiros in zip(nombreconductor_quiros, kms_total_quiros):
    print(f"{nombre_quiros} ha realizado {kms_total_quiros} kilómetros")