# Víctor Quirós Pavón

# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2.
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B,
# se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

print ("Especifica el tipo de uva (A o B) y el tamaño (1 o 2)")
tipo = str(input())
tam = int(input())

precio = float()
precio = 15

if tipo == "A":
    
    if tam == 1:
        precio = precio + 0.20
        print ("El precio es" ,precio , "euros")
    elif tam == 2:
        precio = precio + 0.30
        print ("El precio es" ,precio , "euros")

elif tipo == "B":
    if tam == 1:
        precio = precio - 0.30
        print ("El precio es" ,precio , "euros")
    elif tam == 2:
        precio = precio - 0.50
        print ("El precio es" ,precio , "euros")

else:
    print("El tipo introducido no es correcto")