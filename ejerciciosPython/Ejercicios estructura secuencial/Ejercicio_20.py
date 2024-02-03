print ("Escribe cuantas monedas tienes de 2 euros")
euro1 = int(input())
print ("Escribe cuantas monedas tienes de 1 euros")
euro2 = int(input())
print ("Escribe cuantas monedas tienes de 50 cenitmos")
cent50 = int(input())
print ("Escribe cuantas monedas tienes de 20 cenitmos")
cent20 = int(input())
print ("Escribe cuantas monedas tienes de 10 centimos")
cent10 = int(input())

eurostotal = euro2*2 + euro1
centtotal = cent50*50 + cent20*20 + cent10*10
eurostotal = eurostotal + (centtotal/ 100)
centtotal = centtotal % 100

print ("Tienes " +str(eurostotal) +" euros y " +str(centtotal) +" centimos")