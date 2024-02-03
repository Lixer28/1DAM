print ("Escribe la hora de salida")
horasal = int(input())
print ("Escribe los minutos de salida")
minsal = int(input())
print ("Escribe los segundos de salida")
segsal = int(input())
print ("Tiempo que tardas en llegar (segundos)")
T = int(input())

segin = int (horasal*3600)+(minsal*60)+segsal
segfin = int (segin + T)

horalleg = int(segfin/3600)
minlleg = int(segfin%3600/60)     
seglleg = int(segfin%3600)%60    

print ("La hora de llegada es " + str(horalleg) +":" +str(minlleg) +":" +str(seglleg))