# Víctor Quirós Pavón

# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

print("Escribe una cadena:")
cadena_quiros = input()

diccionario_quiros = {}

for caracter_quiros in cadena_quiros:
    if caracter_quiros in diccionario_quiros:
        diccionario_quiros[caracter_quiros] +=1
    else:
        diccionario_quiros[caracter_quiros] = 1

for caracter_quiros, cantidad_quiros in diccionario_quiros.items():
    print("El caracter",caracter_quiros,"aparece",cantidad_quiros,"veces")