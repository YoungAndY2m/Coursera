CREATE TABLE IF NOT EXISTS "ingredients" (
    "id" INTEGER,
    "name" TEXT,
    "type" TEXT,
    "price" INTEGER,
    PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "donuts" (
    "id" INTEGER,
    "name" TEXT,
    "gluten-free" BOOLEAN,
    "price" INTEGER,
    PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "orders" (
    "id" INTEGER,
    "order_number" INTEGER,
    "customer_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("customer_id") REFERENCES "customers"("id")
);
CREATE TABLE IF NOT EXISTS "customers" (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "donut_ingredient" (
    "donut_id" INTEGER,
    "ingredient_id" INTEGER,
    PRIMARY KEY("donut_id", "ingredient_id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id")
);
CREATE TABLE IF NOT EXISTS "order_donut" (
    "student_id" INTEGER,
    "school_id" INTEGER,
    PRIMARY KEY("student_id", "school_id"),
    FOREIGN KEY("student_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")
);
