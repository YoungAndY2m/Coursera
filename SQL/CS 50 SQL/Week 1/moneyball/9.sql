SELECT "name", AVG("salary") AS "average salary" FROM "teams" as "t"
JOIN "salaries" as "s" ON "t"."id" = "s"."team_id"
WHERE "s"."year" = 2001
GROUP BY "name"
ORDER BY "average salary" ASC
LIMIT 5;
