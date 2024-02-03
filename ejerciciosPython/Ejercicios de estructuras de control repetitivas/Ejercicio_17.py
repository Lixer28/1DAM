# Víctor Quirós Pavón

# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto,
# se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar
# el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

cierto_quiros = bool(True)
pagoempresa_quiros = 0

while cierto_quiros == True:
    print("¿Añadir trabajador? 1-si 2-no")
    trabajador_quiros = int(input())
    if trabajador_quiros == 1:
        print("Escribe cuantos días trabajaste en la semana")
        diatrab_quiros = int(input())
        print("Escribe cuantas horas trabajaste al día")
        horasdia_quiros = int(input())

        sueldosem_quiros = diatrab_quiros * horasdia_quiros
        pagoempresa_quiros = pagoempresa_quiros + sueldosem_quiros
        print("El sueldo semanal del trabajador es",sueldosem_quiros)
    else:
        cierto_quiros = False

print("La empresa debe pagar por los empleados:",pagoempresa_quiros)