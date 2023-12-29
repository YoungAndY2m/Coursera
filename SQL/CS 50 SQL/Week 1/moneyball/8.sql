SELECT "salary" FROM "players" as "p"
JOIN "salaries" as "s" ON "p"."id" = "s"."player_id"
JOIN "performances" as "per" ON "p"."id" = "per"."player_id"
WHERE "HR" = (
    SELECT MAX("HR") FROM "performances"
    WHERE "year" = 2001
)
AND "s"."year" = 2001;
