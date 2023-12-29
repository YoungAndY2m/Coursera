SELECT "year", ROUND(AVG("salary"), 2) AS "average salary" FROM "salaries" as "s"
GROUP BY "year"
ORDER BY "year" DESC;
