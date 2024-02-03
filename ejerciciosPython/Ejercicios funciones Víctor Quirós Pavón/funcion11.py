def LeerFecha():
    print("Escribe el día:")
    d = int(input())

    print("Escribe el mes:")
    m = int(input())

    print("Escribe el año:")
    a = int(input())
    return d, m, a

def EsBisiesto(año):
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False






def DiasDelMes(mes, año):
    if mes in [1,3,5,7,8,10,12]:
        return 31
    elif mes in [4,6,9,11]:
        return 30
    elif mes == 2:
        if EsBisiesto(año):
            return 29
        else:
            return 28

        


def Calcular_Dia_Juliano(d, m, a):
    juliano = 0
    for mes in range(1, m):
        juliano = juliano + DiasDelMes(mes, a)
    juliano = juliano + d
    return juliano