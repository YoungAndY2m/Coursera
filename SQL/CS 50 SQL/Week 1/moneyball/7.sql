SELECT "first_name", "last_name" FROM "players" as "p"
JOIN "salaries" as "s" ON "p"."id" = "s"."player_id"
WHERE "salary" = (
    SELECT MAX("salary") FROM "salaries"
);
