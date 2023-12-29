/*
write a SQL query to explore a question of your choice. This query should:
Involve at least one condition, using WHERE with AND or OR
*/
SELECT COUNT("episode_in_season") FROM "episodes"
WHERE "season" BETWEEN 2 AND 4
AND "topic" LIKE '%fraction%'
OR "topic" LIKE 'fraction%';
