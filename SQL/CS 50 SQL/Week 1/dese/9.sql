SELECT "name"
FROM "districts" AS "d"
JOIN "expenditures" AS "e" ON "d"."id" = "e"."district_id"
GROUP BY "d"."id", "d"."name"
HAVING SUM("e"."pupils") = (
    SELECT MIN("sum_pupils")
    FROM (
        SELECT SUM("pupils") AS "sum_pupils"
        FROM "expenditures"
        GROUP BY "district_id"
    ) AS "subquery"
);
