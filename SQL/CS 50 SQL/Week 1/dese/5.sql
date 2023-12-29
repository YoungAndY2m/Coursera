SELECT "city", COUNT("id") as "count" FROM "schools" AS "s"
WHERE "type" LIKE "Public%"
GROUP BY "city"
HAVING "count" <=3
ORDER BY "count" DESC, "city" ASC;
