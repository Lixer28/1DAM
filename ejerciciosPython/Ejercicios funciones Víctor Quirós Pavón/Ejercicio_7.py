# Víctor Quirós Pavón

# Crear una subrutina llamada “Login”, que recibe un nombre
# de usuario y una contraseña y te devuelve Verdadero si el
# nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer
# login y si no se ha podido hacer login incremente este valor.


from funcion7 import login

intentos_quiros = 1

while intentos_quiros <=3:
    print("---Login---")

    print("Escribe nombre de usuario:")
    usuario_quiros = input()

    print("Escribe la contraseña:")
    contraseña_quiros = input()

    respuesta_quiros = login(usuario_quiros, contraseña_quiros, intentos_quiros)

    if respuesta_quiros == True:
        break
    else:
        intentos_quiros = intentos_quiros + 1
    
    print("\n")