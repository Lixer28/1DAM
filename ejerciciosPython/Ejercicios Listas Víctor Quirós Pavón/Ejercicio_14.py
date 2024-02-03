# Víctor Quirós Pavón

# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:

# Las cantidades totales de cada articulo.
# La cantidad de artículos en la sucursal 2.
# La cantidad del articulo 3 en la sucursal 1.
# La recaudación total de cada sucursal.
# La recaudación total de la empresa.
# La sucursal de mayor recaudación.

listaprecio_quiros = []
listacantidad_quiros = []

for i in range (0,6):
    print("Escribe el precio del articulo",i)
    precio_quiros = int(input())
    listaprecio_quiros.append(precio_quiros)

    print("Escribe la cantidad del articulo",i)
    cantidad_quiros = int(input())
    listacantidad_quiros.append(cantidad_quiros)

len(listaprecio_quiros)
print (listaprecio_quiros)