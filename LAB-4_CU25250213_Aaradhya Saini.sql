-- LAB 4
-- Database Schema using DDL
-- Primary Key and Foreign Key Constraints

CREATE DATABASE LibraryDB;

USE LibraryDB;

CREATE TABLE Author (
    Author_ID INT PRIMARY KEY,
    Author_Name VARCHAR(50) NOT NULL,
    Country VARCHAR(50)
);

CREATE TABLE Book (
    Book_ID INT PRIMARY KEY,
    Book_Name VARCHAR(100) NOT NULL,
    Price DECIMAL(8,2),
    Author_ID INT,
    FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID)
);

INSERT INTO Author VALUES
(1, 'R.K. Sharma', 'India'),
(2, 'Anita Verma', 'India'),
(3, 'John Smith', 'USA');

INSERT INTO Book VALUES
(101, 'Database Fundamentals', 450.00, 1),
(102, 'Learning SQL', 550.00, 2),
(103, 'Advanced Programming', 650.00, 3);

-- DIsplay Data
SELECT * FROM Author;
SELECT * FROM Book;
