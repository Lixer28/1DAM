def LeerFraccion():
    print("Escribe el numerador:")
    numerador = int(input())
    print("Escribe el denominador:")
    denominador = int(input())
    return numerador, denominador

def MCD(num1, num2):
    resto = num1 % num2
    if resto == 0:
        return num2
    else:
        return MCD(num2, num1 % num2)
    

def SimplificarFraccion(numerador, denominador):
    mcd = MCD(numerador, denominador)
    return numerador // mcd, denominador // mcd

def escribirFraccion(numerador, denominador):
    if denominador == 1:
        print(numerador)
    else:
        print(numerador,"/",denominador,"\n")

def SumarFracciones(numerador1, denominador1, numerador2, denominador2):
    return SimplificarFraccion(numerador1*denominador2 + denominador1*numerador2, denominador1*denominador2)

def RestarFracciones(numerador1, denominador1, numerador2, denominador2):
    return SimplificarFraccion(numerador1*denominador2 - denominador1*numerador2, denominador1*denominador2)

def MultiplicarFracciones(numerador1, denominador1, numerador2, denominador2):
    return SimplificarFraccion(numerador1*denominador2, denominador1*denominador2)
    
def DividirFracciones(numerador1, denominador1, numerador2, denominador2):
    return SimplificarFraccion(numerador1*denominador2, denominador1*numerador2)
