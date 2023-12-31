-- Hogwarts Quidditch Management System

-- Represent players in the Quidditch
CREATE TABLE IF NOT EXISTS "players" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "year" INTEGER NOT NULL,
    "position" TEXT CHECK ("position" IN ('chaser', 'seeker', 'beater', 'keeper')),
    "captain" INTEGER CHECK ("captain" IN (1, 0)),
    "broomstick" TEXT,
    "start_date" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "house_id" INTEGER NOT NULL,
    "team_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("house_id") REFERENCES "houses"("id") ON DELETE CASCADE,
    FOREIGN KEY("team_id") REFERENCES "teams"("id") ON DELETE CASCADE
);

-- Represent teams in the Quidditch
CREATE TABLE IF NOT EXISTS "teams" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "house_cup_wins" INTEGER DEFAULT 0,
    "house_id" INTEGER NOT NULL,
    "captain_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("house_id") REFERENCES "houses"("id") ON DELETE CASCADE,
    FOREIGN KEY("captain_id") REFERENCES "players"("id") ON DELETE CASCADE
);

-- Represent houses in the Quidditch
CREATE TABLE IF NOT EXISTS "houses" (
    "id" INTEGER,
    "name" TEXT NOT NULL CHECK ("name" IN ('Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin')),
    PRIMARY KEY("id")
);

-- Represent matches in the Quidditch
CREATE TABLE IF NOT EXISTS "matches" (
    "id" INTEGER,
    "date" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "location" TEXT NOT NULL,
    "winner" TEXT NOT NULL,
    PRIMARY KEY("id")
);

-- Represent matches result played by teams
CREATE TABLE IF NOT EXISTS "leaderboards" (
    "id" INTEGER,
    "team_id" INTEGER,
    "match_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("team_id") REFERENCES "teams"("id") ON DELETE CASCADE,
    FOREIGN KEY("match_id") REFERENCES "matches"("id") ON DELETE CASCADE
);

-- Create indexes to speed common searches
CREATE INDEX IF NOT EXISTS "player_name_search" ON "players" ("first_name", "last_name");
CREATE INDEX IF NOT EXISTS "player_position_search" ON "players" ("position");
CREATE INDEX IF NOT EXISTS "performance_search" ON "matches" ("winner");