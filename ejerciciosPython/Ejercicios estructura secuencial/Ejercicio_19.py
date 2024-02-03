print ("Escribe tus respuestas correctas")
correctas = int(input())
print ("Escribe tus respuestas incorrectas")
incorrectas = int(input())
print ("Escribe tus respuestas en blanco")
blanco = int(input())

nota = (correctas*5) + (incorrectas*-1)
print ("Tu nota es: " +str(nota))