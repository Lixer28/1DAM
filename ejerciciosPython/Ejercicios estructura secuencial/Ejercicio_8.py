#Vendedor de sueldo base con 10% extra por comisión de ventas - preguntar
print ("Escribe tu sueldo base")
sueldobase = int(input())
print ("Escribe el precio de la primera venta")
venta1 = int(input())
print ("Escribe el precio de la segunda venta")
venta2 = int(input())
print ("Escribe el precio de la tercera venta")
venta3 = int(input())

comision = (venta1+venta2+venta3)*0.10
sueldototal = sueldobase + comision

print ("Dinero obtenido por comisiones: " +str(comision))
print ("El sueldo base es: " +str(sueldobase))
print ("El sueldo en total es: " +str(sueldototal))