CREATE VIEW "june_vacancies" AS
SELECT "l"."id", "property_type", "host_name", COUNT("date") AS "days_vacant"
FROM "listings" AS "l"
JOIN "availabilities" AS "a" ON "a"."listing_id" = "l"."id"
WHERE "date" LIKE "2023-06-%"
AND "available" = "TRUE"
GROUP BY "l"."id";
