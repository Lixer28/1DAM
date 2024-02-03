# Víctor Quirós Pavón

# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

print ("Escribe una palabra")
palabra = str(input())

if palabra[0] == str.upper(palabra[0]):
    print ("La primera letra es mayúscula")
else:
    print ("La primera letra es minúscula")