-- Active: 1728974094210@@127.0.0.1@3306@school_management
CREATE DATABASE school_management;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    first_name VARCHAR(10),
    last_name VARCHAR(10),
    age INT,
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

CREATE TABLE teachers(
    teacher_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    first_name VARCHAR(10),
    last_name VARCHAR(10),
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

CREATE Table classes(
    class_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    class_name VARCHAR(10)
);

CREATE TABLE subjects(
    subject_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    subject_name VARCHAR(10)
);

CREATE TABLE student_subjects (
    student_id INT,
    subject_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

CREATE TABLE teacher_subjects (
    teacher_id INT,
    subject_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

INSERT INTO students (first_name, last_name, age, class_id) VALUES
('John', 'Doe', 14, 1),
('Emma', 'Stone', 13, 2),
('Liam', 'Brown', 15, 3),
('Olivia', 'Johnson', 14, 1),
('Sophia', 'Wilson', 13, 2);

INSERT INTO teachers (first_name, last_name, subject_id) VALUES
('Michael', 'Smith', 1),
('Emily', 'Davis', 2),
('Daniel', 'Garcia', 3),
('Linda', 'Martinez', 4);

INSERT INTO classes (class_name) VALUES
('Grade 1'),
('Grade 2'),
('Grade 3');

INSERT INTO subjects (subject_name) VALUES
('Mathematics'),
('Science'),
('English'),
('History');

INSERT INTO student_subjects (student_id, subject_id) VALUES
(1, 1), (1, 2),
(2, 2), (2, 3),
(3, 1), (3, 3), (3, 4),
(4, 1), (4, 4),
(5, 2), (5, 3);


INSERT INTO teacher_subjects (teacher_id, subject_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(1, 2),
(2, 3);

SELECT first_name, last_name FROM students;

SELECT first_name, last_name, age FROM students WHERE age = 14;

SELECT class_name FROM classes;

SELECT first_name, last_name FROM teachers;

SELECT subject_name FROM subjects;

SELECT students.first_name, students.last_name, classes.class_name
FROM students
JOIN classes ON students.class_id = classes.class_id;

SELECT subjects.subject_name
FROM student_subjects
JOIN subjects ON student_subjects.subject_id = subjects.subject_id
WHERE student_subjects.student_id = 1;

SELECT teachers.first_name, teachers.last_name
FROM teachers
JOIN subjects ON teachers.subject_id = subjects.subject_id
WHERE subjects.subject_name = 'Mathematics';

SELECT classes.class_name, COUNT(students.student_id) AS student_count
FROM students
JOIN classes ON students.class_id = classes.class_id
GROUP BY classes.class_name;

SELECT students.first_name, students.last_name
FROM students
JOIN student_subjects ON students.student_id = student_subjects.student_id
JOIN subjects ON student_subjects.subject_id = subjects.subject_id
WHERE subjects.subject_name = 'Science';