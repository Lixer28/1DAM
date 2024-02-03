# Víctor Quirós Pavón

# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero;
# además, se quiere saber cuánto lleva ahorrado cada mes.

totalcobra_quiros = 0
for i in range(1, 12 + 1):
    print ("Escriba cuánto cobra al mes")
    cobrames_quiros = int(input())
    totalcobra_quiros = totalcobra_quiros + cobrames_quiros
    print ("En el mes",i,"has ahorrado",totalcobra_quiros)

print ("Has ahorrado en todo el año un total de",totalcobra_quiros,"euros")