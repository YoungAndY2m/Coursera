SELECT "name", "per_pupil_expenditure", "graduated"
FROM "schools" as "s"
JOIN "graduation_rates" as "g" ON "s"."id" = "g"."school_id"
JOIN "expenditures" as "e" ON "s"."district_id" = "e"."district_id"
ORDER BY "per_pupil_expenditure" DESC, "name" ASC;
