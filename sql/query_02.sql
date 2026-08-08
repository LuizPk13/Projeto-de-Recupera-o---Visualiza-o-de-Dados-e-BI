-- Query 2: Distribuição dos Funcionários por Localidade
-- Objetivo: identificar em quais cidades, países e regiões os funcionários
-- estão alocados, relacionando-os aos seus departamentos e locais de trabalho.

SELECT
    e.EMPLOYEE_ID,
    e.FIRST_NAME,
    e.LAST_NAME,
    d.DEPARTMENT_NAME,
    l.CITY,
    c.COUNTRY_NAME,
    r.REGION_NAME
FROM EMPLOYEES e
LEFT JOIN DEPARTMENTS d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN LOCATIONS l ON d.LOCATION_ID = l.LOCATION_ID
LEFT JOIN COUNTRIES c ON l.COUNTRY_ID = c.COUNTRY_ID
LEFT JOIN REGIONS r ON c.REGION_ID = r.REGION_ID
WHERE r.REGION_NAME IS NOT NULL
ORDER BY r.REGION_NAME, c.COUNTRY_NAME, l.CITY;
