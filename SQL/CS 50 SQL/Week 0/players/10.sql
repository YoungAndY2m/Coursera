SELECT count("first_name") AS "Number of players" FROM "players"
WHERE "final_game" LIKE '2022%'
ORDER BY "first_name", "last_name" DESC;
