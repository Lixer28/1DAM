# Víctor Quirós Pavón

# Vamos a mejorar el ejercicio anterior haciendo una
# función para validar la fecha. De tal forma que al
# leer una fecha se asegura que es válida.


from funcion11 import LeerFecha
from funcion11 import Calcular_Dia_Juliano



d_quiros,m_quiros,a_quiros = LeerFecha()
print("Día Juliano: ",Calcular_Dia_Juliano(d_quiros,m_quiros,a_quiros))