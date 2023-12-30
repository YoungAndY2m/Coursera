-- docker container run --name mysql -p 3306:3306 -v /workspaces/$RepositoryName:/mnt -e MYSQL_ROOT_PASSWORD=crimson -d mysql
-- mysql -h 127.0.0.1 -P 3306 -u root -p # crimson
-- CREATE DATABASE `linkedin`;
-- USE `linkedin`;

CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR(32),
    `last_name` VARCHAR(32),
    `username` VARCHAR(32),
    `password` VARCHAR(32),
    PRIMARY KEY(`id`)
);
CREATE TABLE `schools` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(32),
    `type` VARCHAR(32),
    `location` VARCHAR(32),
    `year` INT,
    PRIMARY KEY(`id`)
    );
CREATE TABLE `companies` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(32),
    `industry` VARCHAR(32),
    `location` VARCHAR(32),
    PRIMARY KEY(`id`)
    );
ALTER TABLE `users` MODIFY COLUMN `password` VARCHAR(128);
ALTER TABLE `schools` MODIFY COLUMN `type` ENUM('Primary', 'Secondary', 'Higher Education');
ALTER TABLE `companies` MODIFY COLUMN `industry` ENUM('Technology', 'Education', 'Business');

CREATE TABLE `people_connection` (
    `id` INT AUTO_INCREMENT,
    `follower` INT,
    `followee` INT,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`follower`) REFERENCES `users`(`id`),
    FOREIGN KEY(`followee`) REFERENCES `users`(`id`)
    );
CREATE TABLE `school_connection` (
    `id` INT AUTO_INCREMENT,
    `student_id` INT,
    `school_id` INT,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`student_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `schools`(`id`)
    );
ALTER TABLE `school_connection` ADD COLUMN `start` DATETIME ;
ALTER TABLE `school_connection` ADD COLUMN `end` DATETIME ;
ALTER TABLE `school_connection` ADD COLUMN `degree` VARCHAR(32) ;

CREATE TABLE `company_connection` (
    `id` INT AUTO_INCREMENT,
    `employee_id` INT,
    `company_id` INT,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`employee_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`company_id`) REFERENCES `companies`(`id`)
);
ALTER TABLE `company_connection` ADD COLUMN `start` DATETIME ;
ALTER TABLE `company_connection` ADD COLUMN `end` DATETIME ;
