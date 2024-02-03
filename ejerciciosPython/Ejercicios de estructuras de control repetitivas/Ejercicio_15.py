# Víctor Quirós Pavón

# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

precio_quiros = int
precio_quiros = 10

preciotot_quiros = int
preciotot_quiros = 0


for i in range (1, 21):
    print ("El mes",i,"paga",precio_quiros, "euros")
    preciomes_quiros = precio_quiros * 2
    preciotot_quiros = preciotot_quiros + precio_quiros
    precio_quiros = precio_quiros * 2
    

print ("Al final de los 20 meses paga",preciotot_quiros,"euros")