SELECT "name", SUM("H") as "total hits" FROM "teams" as "t"
JOIN "performances" as "per" ON "per"."team_id" = "t"."id"
WHERE "per"."year" = 2001
GROUP BY "name"
ORDER BY "total hits" DESC
LIMIT 5;
