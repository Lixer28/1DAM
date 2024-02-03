# Víctor Quirós Pavón

#Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

# Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# Eliminar: Me pide una cadena, y la elimina de la lista.
# Mostrar: Muestra la lista de cadenas
# Terminar

lista_quiros = []

print("Escribe el número de cadenas a introducir dentro de la lista: ")
cant_quiros = int(input())

print("Escribe las cadenas")
while cant_quiros != 0:
    print("Cadena",cant_quiros,":")
    cad_quiros = input()
    lista_quiros.append(cad_quiros)
    cant_quiros = cant_quiros - 1

print("\tMENU")
print("1. Contar ")
print("2. Modificar")
print("3. Eliminar")
print("4. Mostrar")
print("5. Salir")


num_quiros = int(input())

while num_quiros != 5:
    if num_quiros == 1:
        print("Escribe una cadena para contar las veces que aparece:")
        cad_quiros = input()
        veces_quiros = lista_quiros.count(cad_quiros)
        print("Esta cadena aparece",veces_quiros,"veces en la lista")
    if num_quiros == 2:
        print("Escribe una cadena para que se cambie por otra que escribas:")
        cad_quiros = input ()
        print("Escribe la cadena que vas a cambiar:")
        cambia_quiros = input()
        for i in range(len(lista_quiros)):
            if lista_quiros[i] == cad_quiros:
                lista_quiros[i] = cambia_quiros
        lista_quiros = lista_quiros.append(cad_quiros)
        print("")
    if num_quiros == 3:
        print("Escribe una cadena para eliminar:")
        cad_quiros = input()
        for i in range (len(lista_quiros)):
            if lista_quiros[i] == cad_quiros:
                lista_quiros = lista_quiros.pop(i)
        print("La cadena se ha eliminado")
        print(lista_quiros)
    if num_quiros == 4:
        print(lista_quiros)
        print("")

    if num_quiros == 5:
        break

    print("\tMENU")
    print("1. Contar ")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Salir")
    num_quiros = int(input("\n"))