CREATE VIEW "available" AS
SELECT "l"."id", "property_type", "host_name", "date"
FROM "listings" AS "l"
JOIN "availabilities" AS "a" ON "a"."listing_id" = "l"."id"
WHERE "available" = "TRUE";
