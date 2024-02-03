def MCD(num1, num2):
    resto = num1 % num2
    if resto == 0:
        return num2
    else:
        return MCD(num2, num1 % num2)