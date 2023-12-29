SELECT DISTINCT "name" FROM "teams" as "t"
JOIN "performances" as "per" ON "per"."team_id" = "t"."id"
JOIN "players" as "p" ON "per"."player_id" = "p"."id"
WHERE "first_name" = "Satchel"
AND "last_name" = "Paige";
