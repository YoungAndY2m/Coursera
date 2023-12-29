CREATE TABLE IF NOT EXISTS "passengers" (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" INTEGER,
    PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "check_ins" (
    "id" INTEGER,
    "passenger_id" INTEGER,
    "date_time" NUMERIC,
    "flight" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id")
    FOREIGN KEY("flight") REFERENCES "flights"("id")
);
CREATE TABLE IF NOT EXISTS "airlines" (
    "id" INTEGER,
    "name" TEXT,
    "concourse" TEXT,
    PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "flights" (
    "id" INTEGER,
    "flight_number" INTEGER,
    "airline_id" INTEGER,
    "from_airport" TEXT,
    "to_airport" TEXT,
    "departure_date_time" NUMERIC,
    "arrival_date_time" NUMERIC,
    PRIMARY KEY("id"),
    FOREIGN KEY("airline_id") REFERENCES "airlines"("id")
);


