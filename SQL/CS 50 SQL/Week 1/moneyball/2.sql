SELECT "year", "salary" FROM "salaries" as "s"
JOIN "players" as "p" ON "s"."player_id" = "p"."id"
WHERE "first_name" = "Cal"
AND "last_name" = "Ripken"
ORDER BY "year" DESC;
