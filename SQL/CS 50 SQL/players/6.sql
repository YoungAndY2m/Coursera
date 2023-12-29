SELECT "first_name", "last_name", "debut" FROM "players"
WHERE "birth_state" = 'PA'
AND "birth_city" = 'Pittsburgh'
ORDER BY "debut" DESC, "last_name" ASC;
