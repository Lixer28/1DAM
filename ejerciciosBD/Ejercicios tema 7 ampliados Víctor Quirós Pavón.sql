# 4.1.- Determinar el salario máximo para el conjunto de todos los empleados. 

# SELECT MAX(SALAR) FROM temple;

# 4.2.- Averiguar el salario máximo para los empleados del departamento 100.
# SELECT MAX(SALAR) FROM temple
# WHERE NUMDE = 100;


# 4.4.- Hallar el nombre, la fecha de ingreso y los días trabajados hasta la fecha
# actual de cada empleado del departamento 110, de mayor a menor.
/*
SELECT temple.NOMEM, temple.FECIN, DATEDIFF(NOW(), temple.FECIN)
AS "DITRAB" FROM temple
WHERE temple.NUMDE = 110
ORDER BY temple.NOMEM DESC;
*/


/*
4.5.- Averiguar, de cada empleado del departamento 110: el nombre, la fecha
de ingreso y los días trabajados hasta el 01-11-2010, ordenados de más a
menos antigüedad.
*/
/*
SELECT temple.NOMEM, temple.FECIN, DATEDIFF('2010-11-01', temple.FECIN)
AS "DITRAB FECHA" FROM temple
WHERE temple.NUMDE = 110
ORDER BY temple.FECIN DESC;


/*
4.6.- Obtener el número de semanas de diferencia entre el empleado que entró
primero y el que entró último en 1988.
*/


/*
4.7.- Determinar la edad en años cumplidos del empleado más viejo del
departamento 110.
*/

SELECT NOMEM, FECNA, TRUNCATE(DATEDIFF(NOW(), FECNA/365.25,0)) AS "Edad" FROM temple
WHERE NUMDE = 110 ORDER BY "Edad" DESC LIMIT 1;



/*
4.8.- Contar el número de empleados de la empresa.
*/

# SELECT COUNT(*) FROM temple;

/*
4.9.- Hallar el número de empleados y de extensiones telefónicas (téngase en
cuenta que muchos empleados comparten teléfono) del departamento 112 .
*/

# SELECT COUNT(NOMEM), COUNT(EXTEL) FROM temple;


/*
4.10.- Calcular cuántos empleados hay cuya fecha de nacimiento sea anterior al
año 1980.
*/

/*
SELECT COUNT(NOMEM) FROM temple
WHERE FECNA < 01-01-1980;
*/




