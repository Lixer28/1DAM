# Víctor Quirós Pavón

# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes.
# Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

listames_quiros = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
listadia_quiros = [31,28,31,30,31,30,31,31,30,31,30,31,]

print("Escribe el número de un mes que tenga el año:")
num_quiros = int(input())

if num_quiros >= 1 and num_quiros <= 12:
    print ("Son",listadia_quiros[num_quiros-1],"días y el mes es",listames_quiros[num_quiros-1])