SELECT "city", COUNT("id") as "count" FROM "schools" AS "s"
WHERE "type" LIKE "Public%"
GROUP BY "city"
ORDER BY "count" DESC, "city" ASC
LIMIT 10;
