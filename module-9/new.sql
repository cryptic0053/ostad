-- Active: 1728974094210@@127.0.0.1@3306@neww
CREATE DATABASE neww;


CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `employees` (`id`, `name`, `salary`, `designation`, `city`) VALUES
(1, 'John Doe', 55000.00, 'Software Engineer', 'New York'),
(2, 'Jane Smith', 62000.50, 'Project Manager', 'San Francisco'),
(3, 'Michael Brown', 45000.00, 'Data Analyst', 'Chicago'),
(4, 'Emily Davis', 70000.00, 'Senior Developer', 'Austin'),
(5, 'William Johnson', 48000.00, 'UI/UX Designer', 'Seattle'),
(6, 'Sophia Martinez', 53000.00, 'QA Engineer', 'Los Angeles'),
(7, 'Olivia Wilson', 60000.00, 'Database Administrator', 'Denver'),
(8, 'James Anderson', 80000.00, 'DevOps Engineer', 'Houston'),
(9, 'Liam Thomas', 52000.00, 'Front-End Developer', 'Dallas'),
(10, 'Emma Hernandez', 68000.00, 'Back-End Developer', 'Boston'),
(11, 'Benjamin Moore', 73000.00, 'Product Manager', 'Miami'),
(12, 'Amelia Taylor', 49000.00, 'Technical Writer', 'Phoenix'),
(13, 'Lucas Harris', 62000.00, 'Network Engineer', 'San Diego'),
(14, 'Mason Clark', 52000.00, 'Software Engineer', 'Las Vegas'),
(15, 'Harper Lewis', 47000.00, 'Data Scientist', 'Orlando'),
(16, 'Ethan Walker', 55000.00, 'Web Developer', 'Portland'),
(17, 'Ava Young', 51000.00, 'Security Analyst', 'Philadelphia'),
(18, 'Alexander King', 57000.00, 'Cloud Architect', 'Atlanta'),
(19, 'Isabella Scott', 69000.00, 'Mobile Developer', 'Charlotte'),
(20, 'Daniel Adams', 54000.00, 'Full-Stack Developer', 'Columbus'),
(21, 'Charlotte Baker', 61000.00, 'Machine Learning Engineer', 'Indianapolis'),
(22, 'Elijah Allen', 75000.00, 'AI Specialist', 'San Antonio'),
(23, 'Mia White', 66000.00, 'Software Engineer', 'San Jose'),
(24, 'Henry Martinez', 50000.00, 'IT Support', 'Baltimore'),
(25, 'Evelyn Rodriguez', 52000.00, 'System Administrator', 'Kansas City'),
(26, 'Logan Lee', 47000.00, 'DevOps Specialist', 'Milwaukee'),
(27, 'Avery Hill', 58000.00, 'Business Analyst', 'Tampa'),
(28, 'Jackson Green', 67000.00, 'IT Consultant', 'Salt Lake City'),
(29, 'Grace Cooper', 64000.00, 'Software Architect', 'Nashville'),
(30, 'Lucas Perez', 75000.00, 'Cloud Engineer', 'Oklahoma City');

ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--select all row
SELECT * FROM employees;

--select specific column
SELECT ID,NAME,salary FROM employees;

SELECT ID,NAME,salary FROM employees WHERE salary>60000.00 AND salary<70000.00

--order by
SELECT * FROM employees order BY salary ASC;

INSERT INTO employees(ID,NAME,salary,designation,city) VALUES(31,"Cryptic0053",56000.00,"Manager","Rajshahi")

UPDATE employees SET salary=80000 WHERE NAME="Anirban Ghosh"

DELETE FROM employees WHERE ID=30

SELECT COUNT(*) AS salary_up_to_100k FROM employees WHERE salary<70000;