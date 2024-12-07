-- Active: 1728314377960@@127.0.0.1@3306@ABC123

CREATE TABLE employees(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR (100),
    city VARCHAR(100),      
    designation VARCHAR(100),  
    salary DECIMAL(10,2)
)


DROP TABLE employees