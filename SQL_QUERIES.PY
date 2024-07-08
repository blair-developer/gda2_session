##create database as instructed with the video

##Create the Employee table
CREATE TABLE Employee (
    id INTEGER NOT NULL UNIQUE,
    employee_id INTEGER NOT NULL UNIQUE,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    name VARCHAR(100),
    gender VARCHAR(10),
    location VARCHAR(100),
    PRIMARY KEY(id AUTOINCREMENT)
);
##Insert rows of data
INSERT INTO Employee (employee_id, firstname, lastname, name, gender, location) VALUES
(1001, 'John', 'Doe', 'John Doe', 'Male', 'New York')