#Create a Database
"""-- Create a new database
CREATE DATABASE school_db;"""

#Database Use 
#conect to data base
#\c school_db;

#Create a table
"""
-- Create a students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,     -- Auto ID
    name VARCHAR(100),         -- Student name
    age INT,                   -- Age
    marks INT                  -- Marks
);"""

#Insert the data
"""
-- Insert data into table
INSERT INTO students (name, age, marks)
VALUES
('Rahul', 20, 85),
('Anita', 21, 90),
('Suman', 19, 78);"""

#Data Show 
#-- Show all students
#SELECT * FROM students;