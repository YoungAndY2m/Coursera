SELECT "name", "per_pupil_expenditure", "exemplary" FROM "districts" AS "d"
JOIN "expenditures" as "e" ON "d"."id" = "e"."district_id"
JOIN "staff_evaluations" as "s" ON "d"."id" = "s"."district_id"
WHERE "per_pupil_expenditure" < (
    SELECT AVG("per_pupil_expenditure")
    FROM "expenditures"
)
AND "exemplary" < (
    SELECT AVG("exemplary")
    FROM "staff_evaluations"
)
AND "type" LIKE "Public%"
ORDER BY "exemplary" DESC, "per_pupil_expenditure" DESC;
