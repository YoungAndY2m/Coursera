SELECT "p"."first_name", "p"."last_name"
FROM "players" AS "p"
JOIN "salaries" AS "s" ON "p"."id" = "s"."player_id"
JOIN "performances" AS "per" ON "p"."id" = "per"."player_id"
WHERE "s"."year" = "per"."year"
AND "s"."year" = 2001
AND "per"."H" > 0
AND "per"."RBI" > 0
AND "s"."salary"/"per"."H" in (
    SELECT "s"."salary"/"per"."H" as "average" FROM "salaries" as "s"
    JOIN "performances" AS "per" ON "s"."player_id" = "per"."player_id"
    WHERE "s"."year" = "per"."year"
    AND "s"."year" = 2001
    AND "per"."H" > 0
    ORDER BY "average" ASC
    LIMIT 10
)
AND "s"."salary"/"per"."RBI" in (
    SELECT "s"."salary"/"per"."RBI" as "average" FROM "salaries" as "s"
    JOIN "performances" AS "per" ON "s"."player_id" = "per"."player_id"
    WHERE "s"."year" = "per"."year"
    AND "s"."year" = 2001
    AND "per"."RBI" > 0
    ORDER BY "average" ASC
    LIMIT 10
)
ORDER BY "p"."id" ASC, "first_name" ASC, "last_name" ASC
LIMIT 10;
