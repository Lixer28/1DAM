# Víctor Quirós Pavón

# Diseñar una función que calcule el área y el perímetro de una circunferencia.
# Utiliza dicha función en un programa principal que lea el radio de una
# circunferencia y muestre su área y perímetro.

from funcion6 import areaPerimetro

print("Escribe el radio de la circunferencia:")
radio_quiros = float(input())

perimetro_quiros, area_quiros  = areaPerimetro(radio_quiros)
print("El perímetro es:",perimetro_quiros)
print("El área es:",area_quiros)