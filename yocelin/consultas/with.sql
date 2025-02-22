SELECT LENGHT(name) len_names
FROM names
ORDER BY 1 DESC
LIMIT 1


SELECT apellido
FROM apellidos
WHERE LENGHT(apellido) = (
    SELECT LENGHT(name) len_names
    FROM names
    ORDER BY 1 DESC
    LIMIT 1
)
AND SDASS = (
    SELECT LENGHT(name) len_names
    FROM names
    ORDER BY 1 DESC
    LIMIT 1
);


SELECT ...
FROM (
    SELECT ..
    FROM t1_inner
    WHERE ...
) t1
JOIN (
    SELECT ..
    FROM t2_inner
    WHERE ...
) t2 ON t2.id = t1.id_t2;

WITH
    -- esta subconsulta es para ....
    t1 AS (
        SELECT ..
        FROM t1_inner
        WHERE ...
    ),
    -- esta subconsulta es para ....
    t2 AS (
        SELECT ..
        FROM t2_inner
        WHERE ...
    )
SELECT ...
FROM t1
JOIN t2 ON t2.id = t1.id_t2;


WITH
    d AS (
        SELECT
            department, 
            SUM(salary) total_salary_by_department
        FROM employees
        GROUP BY 1
    )
SELECT 
    employee_id, 
    department, 
    salary, 
FROM employees e
JOIN d ON d.department = e.department

SELECT 
    employee_id, 
    department, 
    salary, 
    SUM(salary) OVER (PARTITION BY department) AS total_salary_by_department
FROM employees;

-- 1, tech, 100, 300
-- 2, tech, 100, 300
-- 3, tech, 100, 300
-- 4, RH, 200, 400
-- 5, RH, 200, 400
