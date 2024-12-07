-- Active: 1728974094210@@127.0.0.1@3306@demo
CREATE DATABASE demo;

SELECT "hello world" AS msg
SELECT 2+2 AS sum

SELECT "hello world" AS msg1,3+2 as sum,10-4 as sub

SET @num1=10;
SET @num2=20;
SET @num3=30;

SELECT @num1+@num2 as sum1,
@num1+@num3 as sum2,
@num1*@num2 as mul1,
@num2*@num3 as mul2

SELECT POWER(@num1,@num3) as powernum1

SELECT SQRT(@num1) as sqrtnum1,SQRT(@num2) as sqrtnum2,SQRT(@num3) as sqrtnum3

SELECT UPPER("hello") as lowercase,REVERSE("hello") as lowercase

SELECT NOW() as currenttime

SELECT datediff('2024-10-20','2024-10-19') as diff

