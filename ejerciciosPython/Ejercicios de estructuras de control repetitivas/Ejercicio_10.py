# Víctor Quirós Pavón

# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

num_quiros = int(1)

for i in range (0, 5):
    
    for i in range (1, 11):
        resultado_quiros = num_quiros * i
        print (num_quiros,"x",i,"=",resultado_quiros,)
        
    num_quiros = num_quiros + 1
    print ("")