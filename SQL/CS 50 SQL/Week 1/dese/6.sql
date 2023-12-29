SELECT "name" FROM "schools" AS "s"
LEFT JOIN "graduation_rates" as "g" ON "s"."id" = "g"."school_id"
WHERE "graduated" = 100;
