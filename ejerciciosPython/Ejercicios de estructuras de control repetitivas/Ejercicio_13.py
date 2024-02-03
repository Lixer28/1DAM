# Víctor Quirós Pavón

# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas,
# así como el sueldo que recibirá por las horas trabajadas.

total_horadia_quiros = 0
diasem_quiros = int(6)

print("¿Cuánto cobras por horas?")
cobrahora_quiros = int(input())

for i in range(1,7):
    print("¿Cuántas horas trabaja el dia",i,"?")
    horadia_quiros = int (input())
    total_horadia_quiros = total_horadia_quiros+ horadia_quiros


trabajasem_quiros = diasem_quiros * horadia_quiros
sueldo_quiros = total_horadia_quiros * cobrahora_quiros

print ("Total de horas trabajadas en la semana:",trabajasem_quiros)
print ("Sueldo:",sueldo_quiros)