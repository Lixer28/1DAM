# Víctor Quirós Pavón

# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia.
# No se puede utilizar el operador de potencia.

resultado_quiros = 1

print ("Escribe la base de la potencia")
base_quiros = int(input())
print ("Escribe el exponente de la potencia")
expo_quiros = int(input())

for i in range (1, expo_quiros + 1):
    resultado_quiros = resultado_quiros * base_quiros

print (resultado_quiros)