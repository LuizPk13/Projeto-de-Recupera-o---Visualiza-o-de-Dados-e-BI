-- Query 1: Comparação de Salários por Departamento e Cargo
-- Objetivo: relacionar cada funcionário ao seu departamento e cargo,
-- permitindo observar quais cargos e departamentos possuem os maiores salários.

SELECT
    e.EMPLOYEE_ID,
    e.FIRST_NAME,
    e.LAST_NAME,
    e.SALARY,
    d.DEPARTMENT_ID,
    d.DEPARTMENT_NAME,
    j.JOB_ID,
    j.JOB_TITLE
FROM EMPLOYEES e
LEFT JOIN DEPARTMENTS d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN JOBS j ON e.JOB_ID = j.JOB_ID
WHERE e.SALARY > 3000
ORDER BY d.DEPARTMENT_NAME, e.SALARY DESC;
