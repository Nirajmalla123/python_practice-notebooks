/* 
Multi-line comment
*/

-- Comment for single line alter

/*
To Create database

CREATE DATABASE db_name;  -- it is case insensative

*/

CREATE DATABASE python;
USE python;




/*
DataTypes : int,varchar(n),char(n), float, date, boolean-- n is the length of character

varchar(50)

*/

/* TO Create table
CREATE TABLE TABLE_NAME(
column_name datatype,
column_name datatype
);
*/

CREATE TABLE student(
id int,
name VARCHAR(50),
age int,
city VARCHAR(50)
);

-- deleting table 
DROP TABLE student;

-- deleting column 
ALTER TABLE student DROP COLUMN city;

-- deleting database
DROP DATABASE python;
drop table student_info;

/* 
renaming column

ALTER TABLE table_name
CHANGE old_column_name new_column_name datatype;student
*/


alter table student
change city address varchar(50);


-- renaming table
rename table student to student_info;

-- adding new column in existing table 
alter table student add email varchar(50);


-- inserting data in table 
insert into student(id,name,age,city,email)
value(1,"Ram",21,"Kathmandu","ram@gmail.com");

-- for multiples values 
insert into student(id,name,age,city,email)
values
(2,"Rem",25,"Kathmandu","rem@gmail.com"),
(3,"hari",22,"banke","hari@gmail.com"),
(4,"shyam",24,"pokhara","shyam@gmail.com");


-- to view a table or data
SELECT * FROM student; -- fetch every data 
select name,age from student; -- fetch data according to column given

-- where clause -> used to filter data 
SELECT * FROM student WHERE age>24;
-- Note: We do not use the WHERE clause with INSERT statements, but we use it with other SQL operations such as UPDATE, DELETE, and SELECT.
SELECT * FROM student WHERE city ="kathmandu";

/* 
updating existing data 

syntax:
UPDATE table_name
SET column1 = new_value, column2=new_vlaue
WHERE condition
*/

UPDATE student SET city='Bhaktapur' WHERE id=2;


/* 
deleting records 

syntax:
DELETE FROM table_name
WHERE condition;
*/


DELETE FROM student 
WHERE id =6;

/*
Constraints

primary key: it cannot be null and must be unique
not null: cannot be null 
unique: must be unique
check: checks certain condition before inserting
default:set default value to a column
foreign key : links two table ( maintain relationship)
*/

-- constraints 
CREATE TABLE users(
	id int primary key auto_increment,
	name varchar(50) not null, 
	email varchar(50) unique,
    age int,
	city varchar(50) default 'kathmandu'
);

drop table users;

INSERT INTO users(name,email,age,city)
VALUES
("ram","ram@gmail.com",23,"lalitput"),
("shyam","shyam@gmail.com",24,"Bhaktapur");

SELECT * FROM users;


/* 
Aggregate functions: count(),sum(),avg(),min(),max()
*/

CREATE TABLE employee(
id int primary key auto_increment,
name varchar(50),
age int,
salary int check(salary>24000),
city varchar(50) default "Pokhara"
);

INSERT INTO employee(name,age,salary,city)
VALUES
("ram",22,25000,"Kathmandu"),
("shyam",26,26000,"Lalitpur"),
("hari",24,28000,"Bhaktapur"),
("Geeta",25,29000,"Banke");

INSERT INTO employee(name,age,salary)
VALUES
("mohan",22,25000),
("bikram",34,26000),
("biki",22,28000),
("bibek",23,29000);

SELECT count(*) from employee where city="Pokhara";
SELECT count(*) from employee where age between 23 and 26;
SELECT count(*) from employee where age >= 23 and age <= 26;
select sum(salary) from employee  where city = "Kathmandu";
SELECT avg(salary) from employee where city="pokhara";

SELECT min(salary) from employee;
SELECT max(salary) from employee;

SELECT name,salary 
from employee where salary=(SELECT min(salary) from employee);
SELECT *
from employee where salary=(SELECT max(salary) from employee);

-- GROUP BY: divide records into groups and perform aggregate calculation on each groups
-- count employee in each city 
SELECT city,count(*)
from employee 
GROUP BY city;

-- total salary by city 
SELECT city,sum(salary) as total_salary
from employee 
GROUP BY city;

-- average salary by city 
SELECT city, avg(salary) as average_salary
from employee 
GROUP BY city;


-- minimum and maximum salary in each city 
SELECT city, min(salary), max(salary)
FROM employee 
GROUP BY city;