/* Create Database and Table */
CREATE DATABASE IF NOT EXISTS SuperstoreDB;
USE SuperstoreDB;

CREATE TABLE IF NOT EXISTS sales (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate DATE,
    CustomerName VARCHAR(150),
    Product VARCHAR(255),          
    Category VARCHAR(100),         
    Region VARCHAR(50),
    Sales DECIMAL(10, 2),
    Quantity INT
);

/* Insert Sample Data */
INSERT INTO sales (OrderDate, CustomerName, Product, Category, Region, Sales, Quantity)
VALUES
('2024-01-15', 'Alice', 'Laptop', 'Electronics', 'North', 75000, 1),
('2024-02-10', 'Bob', 'Phone', 'Electronics', 'South', 50000, 2),
('2024-03-05', 'Charlie', 'TV', 'Electronics', 'West', 75000, 1),
('2024-03-20', 'David', 'Shoes', 'Fashion', 'East', 3000, 3),
('2024-04-15', 'Eve', 'Washing Machine', 'Home Appliances', 'North', 25000, 1);
