CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    department VARCHAR(100),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION ultimo_venta()
...
SELECT
from ventas
WHERE MAX(created_at)
LIMIT 1
...

-- Creación de función para el trigger
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Creación del trigger que actualiza la columna updated_at en cada UPDATE
CREATE TRIGGER update_employee_timestamp
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();


UPDATE employees
SET salary = salary * 1.1
WHERE department = 'tech';

SELECT convert_usd_to_cop(salary_usd)
FROM employees;


CREATE OR REPLACE PROCEDURE increase_salary(percent DECIMAL)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employees
    SET salary = salary + (salary * percent / 100)
    WHERE TRUE;
END;
$$;

CALL increase_salary(0.1);
