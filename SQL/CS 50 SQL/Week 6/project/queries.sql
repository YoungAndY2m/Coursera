-- INSERT data into players
-- Add new players - Gryffindor
INSERT OR IGNORE INTO "players" 
("first_name", "last_name", "year", "position", "captain", 
"broomstick", "start_date", "house_id", "team_id") VALUES 
('Harry', 'Potter', 7, 'seeker', 1, 'Firebolt', CURRENT_TIMESTAMP, 1, 1),
('Ron', 'Weasley', 7, 'keeper', 0, 'Cleansweep Five', CURRENT_TIMESTAMP, 1, 1),
('Hermione', 'Granger', 7, 'chaser', 0, 'Nimbus 2000', CURRENT_TIMESTAMP, 1, 1),
('Ginny', 'Weasley', 7, 'beater', 0, 'Cleansweep Eleven', CURRENT_TIMESTAMP, 1, 1),
('Neville', 'Longbottom', 7, 'chaser', 0, 'Nimbus 2001', CURRENT_TIMESTAMP, 1, 1),
('Fred', 'Weasley', 7, 'beater', 0, 'Firebolt', CURRENT_TIMESTAMP, 1, 1),
('George', 'Weasley', 7, 'chaser', 0, 'Firebolt', CURRENT_TIMESTAMP, 1, 1);
-- Add new players - Hufflepuff
INSERT OR IGNORE INTO "players" ("first_name", "last_name", "house_id", "year", "team_id", "position", "captain", "broomstick", "start_date")
VALUES 
('Cedric', 'Diggory', 2, 7, 2, 'seeker', 1, 'Firebolt', CURRENT_TIMESTAMP),
('Ernie', 'Macmillan', 2, 7, 2, 'beater', 0, 'Comet 260', CURRENT_TIMESTAMP),
('Hannah', 'Abbott', 2, 7, 2, 'chaser', 0, 'Cleansweep Seven', CURRENT_TIMESTAMP),
('Justin', 'Finch-Fletchley', 2, 7, 2, 'beater', 0, 'Comet 260', CURRENT_TIMESTAMP),
('Susan', 'Bones', 2, 7, 2, 'chaser', 0, 'Nimbus 2001', CURRENT_TIMESTAMP),
('Zacharias', 'Smith', 2, 7, 2, 'chaser', 0, 'Nimbus 2000', CURRENT_TIMESTAMP),
('Wayne', 'Hopkins', 2, 7, 2, 'keeper', 0, 'Nimbus 2000', CURRENT_TIMESTAMP);
-- Add new players - Ravenclaw
INSERT OR IGNORE INTO "players" ("first_name", "last_name", "house_id", "year", "team_id", "position", "captain", "broomstick", "start_date")
VALUES 
('Cho', 'Chang', 3, 7, 3, 'seeker', 1, 'Nimbus 2001', CURRENT_TIMESTAMP),
('Padma', 'Patil', 3, 7, 3, 'chaser', 0, 'Cleansweep Eleven', CURRENT_TIMESTAMP),
('Terry', 'Boot', 3, 7, 3, 'beater', 0, 'Comet 260', CURRENT_TIMESTAMP),
('Luna', 'Lovegood', 3, 7, 3, 'chaser', 0, 'Nimbus 2000', CURRENT_TIMESTAMP),
('Michael', 'Corner', 3, 7, 3, 'beater', 0, 'Cleansweep Five', CURRENT_TIMESTAMP),
('Roger', 'Davies', 3, 7, 3, 'chaser', 0, 'Nimbus 2000', CURRENT_TIMESTAMP),
('Mandy', 'Brocklehurst', 3, 7, 3, 'keeper', 0, 'Cleansweep Eleven', CURRENT_TIMESTAMP);
-- Add new players - Slytherin
INSERT OR IGNORE INTO "players" ("first_name", "last_name", "house_id", "year", "team_id", "position", "captain", "broomstick", "start_date")
VALUES 
('Draco', 'Malfoy', 4, 7, 4, 'seeker', 1, 'Nimbus 2001', CURRENT_TIMESTAMP),
('Pansy', 'Parkinson', 4, 7, 4, 'beater', 0, 'Firebolt', CURRENT_TIMESTAMP),
('Theodore', 'Nott', 4, 7, 4, 'chaser', 0, 'Cleansweep Seven', CURRENT_TIMESTAMP),
('Vincent', 'Crabbe', 4, 7, 4, 'beater', 0, 'Comet 260', CURRENT_TIMESTAMP),
('Millicent', 'Bulstrode', 4, 7, 4, 'chaser', 0, 'Cleansweep Eleven', CURRENT_TIMESTAMP),
('Blaise', 'Zabini', 4, 7, 4, 'chaser', 0, 'Nimbus 2000', CURRENT_TIMESTAMP),
('Marcus', 'Flint', 4, 7, 4, 'keeper', 0, 'Nimbus 2000', CURRENT_TIMESTAMP);


-- INSERT data into houses
INSERT OR IGNORE INTO "houses" ("name") 
VALUES ('Gryffindor'), ('Hufflepuff'), ('Ravenclaw'), ('Slytherin');


-- INSERT data into teams
INSERT OR IGNORE INTO "teams" ("name", "house_cup_wins", "house_id", "captain_id") 
VALUES ('Gryffindor Team', 3, 1, 1), ('Hufflepuff Team', 1, 2, 8),
('Ravenclaw Team', 4, 3, 15), ('Slytherin Team', 2, 4, 22);


-- INSERT data into matches
INSERT OR IGNORE INTO "matches" ("date", "location", "winner") 
VALUES (CURRENT_TIMESTAMP, "Quidditch pitch", "Gryffindor Team"), (CURRENT_TIMESTAMP, "Forbidden Forest", "Ravenclaw Team"),
(CURRENT_TIMESTAMP, "Quidditch pitch", "Slytherin Team"), (CURRENT_TIMESTAMP, "Quidditch pitch", "Hufflepuff Team");


-- INSERT data into leaderboards
INSERT OR IGNORE INTO "matches" ("team_id", "match_id") 
VALUES (1, 1), (2, 1), (1, 2), (3, 2), (3, 3), (4, 3), (4, 4), (2, 4);

-- Find all players who plays particular position
SELECT * FROM "players" WHERE "position" = "seeker";

-- Find all winner count
SELECT "winner", COUNT("winner") AS "winning counts" FROM "matches" 
GROUP BY "winner";
