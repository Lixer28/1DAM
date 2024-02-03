# Víctor Quirós Pavón

# Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

# Vamos a crear las siguientes funciones para trabajar con funciones:

# Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
# Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
# Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
# Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
# Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
# Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:

# Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
# Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
# Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
# Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
# Salir

from funcion13 import LeerFraccion, MCD, SimplificarFraccion, SumarFracciones, RestarFracciones, MultiplicarFracciones, DividirFracciones, escribirFraccion


while True:
    print("1. Sumar dos fracciones")
    print("2. Restar dos fracciones")
    print("3. Multiplicar dos fracciones")
    print("4. Dividir dos fracciones")
    print("5. Salir")
    opcion_quiros = int(input())

    
    numerador1_quiros, denominador1_quiros = LeerFraccion()
    numerador2_quiros, denominador2_quiros = LeerFraccion()

    if opcion_quiros == 1:
        numerador_quiros, denominador_quiros = SumarFracciones(numerador1_quiros, denominador1_quiros, numerador2_quiros, denominador2_quiros)
        escribirFraccion(numerador_quiros, denominador_quiros)
    elif opcion_quiros == 2:
        numerador_quiros, denominador_quiros = RestarFracciones(numerador1_quiros, denominador1_quiros, numerador2_quiros, denominador2_quiros)
        escribirFraccion(numerador_quiros, denominador_quiros)
    elif opcion_quiros == 3:
        numerador_quiros, denominador_quiros = MultiplicarFracciones(numerador1_quiros, denominador1_quiros, numerador2_quiros, denominador2_quiros)
        escribirFraccion(numerador_quiros, denominador_quiros)
    elif opcion_quiros == 4:
        numerador_quiros, denominador_quiros = DividirFracciones(numerador1_quiros, denominador1_quiros, numerador2_quiros, denominador2_quiros)
        escribirFraccion(numerador_quiros, denominador_quiros)
        
    if opcion_quiros == 5:
        break
    
    else:
        print("No es una opción válida")