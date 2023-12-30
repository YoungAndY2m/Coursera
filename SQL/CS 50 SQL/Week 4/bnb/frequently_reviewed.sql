CREATE VIEW "frequently_reviewed" AS
SELECT "l"."id", "property_type", "host_name", COUNT("comments") AS "reviews"
FROM "listings" AS "l"
JOIN "reviews" AS "r" ON "r"."listing_id" = "l"."id"
GROUP BY "host_name"
ORDER BY "reviews" DESC, "property_type" ASC, "host_name" ASC
LIMIT 100;
