def LongitudCola(cola):
    return len(cola)

def EstaVaciaCola(cola):
    return len(cola) == 0

def EstaLlenaCola(cola):
    return max(len(cola))

def AddCola(texto, cola):
    return cola.append(texto)

def SacarDeLaCola(cola):
    if EstaVaciaCola(cola):
        print("La cola está vacía")
    else:
        return cola.pop(0)
    
def EscribirCola(cola):
    print(cola)