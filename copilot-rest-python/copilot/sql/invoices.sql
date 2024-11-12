--Create a database called Invoice
CREATE DATABASE Invoice;
--Use the database Invoice
USE Invoice;
--Create a table called Invoices
CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY,
    CustomerID INT,
    InvoiceDate DATE,
    Total DECIMAL(10, 2)
);
--Insert data into the Invoices table
INSERT INTO Invoices (InvoiceID, CustomerID, InvoiceDate, Total)
VALUES (1, 1, '2020-01-01', 100.00),
       (2, 2, '2020-01-02', 200.00),
       (3, 3, '2020-01-03', 300.00);
--Select all data from the Invoices table
SELECT * FROM Invoices;
-- add more tables to Invoice database
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(50)
);
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(50),
    Price DECIMAL(10, 2)
);
CREATE TABLE InvoiceItems (
    InvoiceItemID INT PRIMARY KEY,
    InvoiceID INT,
    ProductID INT,
    Quantity INT
);
