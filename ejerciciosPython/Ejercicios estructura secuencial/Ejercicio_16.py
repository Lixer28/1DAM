print("Escribe la velocidad (km/h) del primer vehiculo")
v1 = float(input())
print("Escribe la velocidad (Km/h) del segundo vehiculo (es más lenta que el anterior)")
v2 = float(input())
print("Escribe la distancia entre los coches (Km)")
d = float(input())

tiempo = d/(v1-v2)
tiempo = tiempo * 60

print ("El segundo vehiculo alcanzará al primero en " +str(tiempo) +" minutos")