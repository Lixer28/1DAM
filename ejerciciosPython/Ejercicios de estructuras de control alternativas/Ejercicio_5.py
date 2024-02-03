# Víctor Quirós Pavón

# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

print ("Escribe nombre de usuario")
nombre = str(input())

if nombre == "pepe":
    print ("Escribe una contraseña")
    contra = str(input())
    if contra == "asdasd":
        print ("Has entrado al sistema")
    else:
      print ("Error al intentar entrar al sistema")  
else:
    print ("Error al intentar entrar al sistema")