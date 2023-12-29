CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "username" TEXT,
    "password" TEXT,
    PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "schools" (
    "id" INTEGER,
    "name" TEXT,
    "type" TEXT,
    "location" TEXT,
    "year" INTEGER,
    PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "companies" (
    "id" INTEGER,
    "name" TEXT,
    "industry" TEXT,
    "location" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "user_connections" (
    "follower" INTEGER,
    "followee" INTEGER,
    PRIMARY KEY("follower", "followee"),
    FOREIGN KEY("follower") REFERENCES "users"("id"),
    FOREIGN KEY("followee") REFERENCES "users"("id")
);
CREATE TABLE IF NOT EXISTS "school_connections" (
    "student_id" INTEGER,
    "school_id" INTEGER,
    PRIMARY KEY("student_id", "school_id"),
    FOREIGN KEY("student_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")
);
CREATE TABLE IF NOT EXISTS "company_connections" (
    "employee_id" INTEGER,
    "company_id" INTEGER,
    PRIMARY KEY("employee_id", "company_id"),
    FOREIGN KEY("employee_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "companies"("id")
);
