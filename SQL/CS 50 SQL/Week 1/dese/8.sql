SELECT "name", SUM("pupils") FROM "districts" as "d"
JOIN "expenditures" as "e"
ON "d"."id" = "e"."district_id"
GROUP BY "d"."id";
