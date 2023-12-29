SELECT "year", "HR" FROM "performances" as "per"
JOIN "players" as "p" ON "per"."player_id" = "p"."id"
WHERE "first_name" = "Ken"
AND "last_name" = "Griffey"
AND "birth_year" = 1969
ORDER BY "year" DESC;
