SELECT "first_name", "last_name", "salary" FROM "players" as "p"
JOIN "salaries" as "s" ON "s"."player_id" = "p"."id"
WHERE "year" = 2001
ORDER BY "salary" ASC, "first_name" ASC, "last_name" ASC, "player_id" ASC
LIMIT 50;
