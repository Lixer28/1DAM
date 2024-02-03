def LongitudPila(pila):
    return len(pila)

def EstaVaciaPila(pila):
    return len(pila) == 0

def EstaLlenaPila(pila):
    return max(len(pila))

def AddPila(texto, pila):
    return pila.append(texto)

def SacarDeLaPila(pila):
    if EstaVaciaPila(pila):
        print("La pila está vacía")
    else:
        return pila.pop()
    
def EscribirPila(pila):
    print(pila)