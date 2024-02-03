USE empleados;
/*
1. Calcula la suma del presupuesto de todos los departamentos.
*/

# SELECT SUM(presupuesto) AS "Suma presupuestos" FROM departamento;



/*
2. Calcula la media del presupuesto de todos los departamentos.
*/
# SELECT AVG(presupuesto) AS "Media presupuestos" FROM departamento;

/*
3. Calcula el valor mínimo del presupuesto de todos los departamentos. 
*/
# SELECT MIN(presupuesto) AS "Media presupuestos" FROM departamento;


/*
4. Calcula el nombre del departamento y el presupuesto que tiene asignado,
del departamento con menor presupuesto.
*/
/*
 SELECT nombre, presupuesto FROM departamento
 WHERE presupuesto > (SELECT MIN(presupuesto)FROM departamento);
*/

/*
 5. Calcula el valor máximo del presupuesto de todos los departamentos. 
*/
/*
SELECT nombre, presupuesto FROM departamento
WHERE presupuesto < (SELECT MAX(presupuesto)FROM departamento);
*/

/*
6. Calcula el nombre del departamento y el presupuesto que tiene asignado,
del departamento con mayor presupuesto. 
*/
/*
 SELECT nombre, presupuesto FROM departamento
 WHERE presupuesto = (SELECT MAX(presupuesto)FROM departamento);
*/

/*
7. Calcula el número total de empleados que hay en la tabla empleado.
*/
# MAL
/*
SELECT COUNT(*) AS "Número de empleados" FROM empleado
WHERE nombre = (SELECT * FROM empleado);
*/


/*
8. Calcula el número de empleados que no tienen NULL en su segundo apellido. 
*/

# SELECT COUNT(nombre) AS "Número de empleados" FROM empleado;


