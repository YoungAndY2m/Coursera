SELECT "name", "per_pupil_expenditure"
FROM "districts" as "d"
JOIN "expenditures" as "e"
ON "d"."id" = "e"."district_id"
WHERE "type" LIKE "public%"
ORDER BY "e"."per_pupil_expenditure" desc
LIMIT 10;
