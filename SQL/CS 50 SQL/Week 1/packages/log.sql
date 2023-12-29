
-- *** The Lost Letter ***
SELECT "type", "address" FROM "scans"
LEFT JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
LEFT JOIN "packages" ON "scans"."package_id" = "packages"."id"
WHERE "address" = "2 Finnigan Street"
AND "to_address_id" = "addresses"."id"
AND "contents" LIKE "congrat%";

-- *** The Devious Delivery ***
SELECT "contents", "type" FROM "scans"
JOIN "packages" ON "scans"."package_id" = "packages"."id"
JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
WHERE "from_address_id" IS NULL
AND "action" = "Drop";

-- *** The Forgotten Gift ***
SELECT * FROM "scans" AS "s"
JOIN "packages" AS "p" ON "s"."package_id" = "p"."id"
JOIN "drivers" AS "d" ON "s"."driver_id" = "d"."id"
WHERE "from_address_id" = (
    SELECT "id" FROM "addresses"
    WHERE "address" = '109 Tileston Street'
)
AND "to_address_id" = (
    SELECT "id" FROM "addresses"
    WHERE "address" = '728 Maple Place'
);
