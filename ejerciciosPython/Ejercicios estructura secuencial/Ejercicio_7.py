print ("Escribe los minutos para saber cuantas horas y minutos son")

minutos = int(input())

horas = minutos//60
min_restantes = minutos %60

print ("Los minutos escritos son " +str(horas) +" horas" +" y " +str(min_restantes) +" minutos")