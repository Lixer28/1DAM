# Víctor Quirós Pavón

# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:

# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
# de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?


numequipos_quiros = 2
equipos_quiros = []
resultados_quiros = []

for i in range(1, numequipos_quiros + 1):
    print(f"Escriba el nombre del equipo 1 del partido {i}: ")
    equipo1_quiros = input()
    print(f"Escriba el nombre del equipo 2 del partido {i}: ")
    equipo2_quiros = input()
    equipos_quiros.append((equipo1_quiros, equipo2_quiros))

    print(f"Introduce los goles anotados por el",equipo1_quiros)
    goles_equipo1_quiros = int(input())
    print(f"Introduce los goles anotados por el",equipo2_quiros)
    goles_equipo2_quiros = int(input())
    resultados_quiros.append((goles_equipo1_quiros, goles_equipo2_quiros))

print("Apuestas")

for (equipo1_quiros, equipo2_quiros), (goles1_quiros, goles2_quiros) in zip(equipos_quiros, resultados_quiros):
    print(f"{equipo1_quiros} - {equipo2_quiros}:", end=" ")

    if goles1_quiros > goles2_quiros:
        print("-> 1")
    elif goles1_quiros < goles2_quiros:
        print("-> 2")
    else:
        print("-> X")