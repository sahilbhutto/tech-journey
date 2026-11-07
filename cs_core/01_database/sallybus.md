#  DBMS Salybus 2026


## Phase 01 - Database Foundations

-   [ ] What is data?
-   [ ] What is a database?
-   [ ] What is a DBMS?
-   [ ] What is an RDBMS?
-   [ ] Database vs DBMS vs RDBMS
-   [ ] Why do applications need databases?
-   [ ] File system vs database
-   [ ] Advantages and disadvantages of DBMS
-   [ ] Types of databases: relational, document, key-value, graph
-   [ ] SQL vs NoSQL --- basic differences
-   [ ] Database users and roles --- basic
-   [ ] Database server and database client --- basic

### Practical work

-   [ ] Install or open your existing Oracle database setup.
-   [ ] Open SQL Developer.
-   [ ] Connect to your database.
-   [ ] Understand tables, schemas, and database connections.


## Phase 02 - Relational Database Concepts

-   [ ] What is a relational database?
-   [ ] Tables
-   [ ] Rows / records
-   [ ] Columns / attributes
-   [ ] Fields and values
-   [ ] Domains and data types
-   [ ] Primary key (PK)
-   [ ] Foreign key (FK)
-   [ ] Candidate key
-   [ ] Super key --- basic
-   [ ] Composite key
-   [ ] Alternate key
-   [ ] NULL values
-   [ ] Constraints
-   [ ] Entities and relationships
-   [ ] Referential integrity

### Practical work

-   [ ] Create a `students` table.
-   [ ] Create a `departments` table.
-   [ ] Add primary keys.
-   [ ] Add foreign keys.
-   [ ] Insert sample records.
-   [ ] Identify relationships between tables.


## Phase 03 - SQL Fundamentals

### 3.1 SQL introduction

-   [ ] What is SQL?
-   [ ] SQL commands and their categories
-   [ ] DDL, DML, DQL, DCL, TCL
-   [ ] SQL syntax and statements

### 3.2 Database and table operations

-   [ ] `CREATE TABLE`
-   [ ] `ALTER TABLE`
-   [ ] `DROP TABLE`
-   [ ] `TRUNCATE TABLE`
-   [ ] `RENAME`
-   [ ] `INSERT INTO`
-   [ ] `UPDATE`
-   [ ] `DELETE`
-   [ ] `DB creation diff b/w Oracle and PostgreSQL`

### 3.3 Data types

-   [ ] `INTEGER` / `NUMBER`
-   [ ] `VARCHAR` / `VARCHAR2`
-   [ ] `CHAR`
-   [ ] `DATE`
-   [ ] `TIMESTAMP`
-   [ ] `DECIMAL` / `NUMERIC` concepts
-   [ ] `BOOLEAN` --- understand database differences

### 3.4 Retrieving data

-   [ ] `SELECT`
-   [ ] `SELECT DISTINCT`
-   [ ] `WHERE`
-   [ ] `AND` / `OR` / `NOT`
-   [ ] `IN` / `NOT IN`
-   [ ] `BETWEEN`
-   [ ] `LIKE`
-   [ ] `IS NULL` / `IS NOT NULL`
-   [ ] `ORDER BY`
-   [ ] `ASC` / `DESC`
-   [ ] `FETCH FIRST` / `LIMIT` concept
-   [ ] Column aliases
-   [ ] Arithmetic operators
-   [ ] Comparison operators

### 3.5 SQL functions

-   [ ] `COUNT()`
-   [ ] `SUM()`
-   [ ] `AVG()`
-   [ ] `MIN()`
-   [ ] `MAX()`
-   [ ] `UPPER()` / `LOWER()`
-   [ ] `LENGTH()`
-   [ ] `ROUND()`
-   [ ] `TRUNC()`
-   [ ] `SYSDATE` --- Oracle
-   [ ] Date calculations
-   [ ] `NVL()` --- Oracle
-   [ ] `COALESCE()` --- portable SQL concept

### Practical work

-   [ ] Write 30 `SELECT` queries.
-   [ ] Practice 20 `WHERE`-condition problems.
-   [ ] Perform CRUD operations.
-   [ ] Practice filtering, sorting, and aggregation.


## Phase 04 - Intermediate SQL

### 4.1 Aggregate queries

-   [ ] `GROUP BY`
-   [ ] `HAVING`
-   [ ] `WHERE` vs `HAVING`
-   [ ] Aggregate functions with conditions
-   [ ] `GROUP BY` with multiple columns

### 4.2 Joins

-   [ ] Why joins are needed
-   [ ] `INNER JOIN`
-   [ ] `LEFT JOIN`
-   [ ] `RIGHT JOIN`
-   [ ] `FULL OUTER JOIN`
-   [ ] `CROSS JOIN` --- basic
-   [ ] `SELF JOIN`
-   [ ] Joining three or more tables
-   [ ] Joining through primary and foreign keys

### 4.3 Subqueries

-   [ ] What is a subquery?
-   [ ] Single-row subquery
-   [ ] Multiple-row subquery
-   [ ] Nested subqueries
-   [ ] Correlated subqueries --- basic
-   [ ] `EXISTS` / `NOT EXISTS`
-   [ ] `IN` with subqueries

### 4.4 Conditional and reusable queries

-   [ ] `CASE WHEN`
-   [ ] `COALESCE`
-   [ ] `NULLIF`
-   [ ] `UNION`
-   [ ] `UNION ALL`
-   [ ] `INTERSECT`
-   [ ] `MINUS` --- Oracle
-   [ ] `EXCEPT` --- PostgreSQL
-   [ ] Common Table Expressions (CTEs)
-   [ ] `WITH` clause

### 4.5 Window functions --- learn the basics

-   [ ] `OVER()`
-   [ ] `PARTITION BY`
-   [ ] `ROW_NUMBER()`
-   [ ] `RANK()`
-   [ ] `DENSE_RANK()`
-   [ ] `LAG()` / `LEAD()` --- basic

### Practical work

-   [ ] Solve 20 JOIN problems.
-   [ ] Solve 10 subquery problems.
-   [ ] Write queries involving 3--4 tables.
-   [ ] Find the top 5 students by marks.
-   [ ] Find employees earning more than their department average.
-   [ ] Calculate department-wise salary averages.


## Phase 05 - Database Design and ER Modeling

### 5.1 Database design fundamentals

-   [ ] What is database design?
-   [ ] Requirements analysis
-   [ ] Entities
-   [ ] Attributes
-   [ ] Relationships
-   [ ] One-to-One (1:1)
-   [ ] One-to-Many (1:M)
-   [ ] Many-to-Many (M:N)
-   [ ] Cardinality
-   [ ] Participation constraints
-   [ ] Strong and weak entities

### 5.2 ER diagrams

-   [ ] What is an ER diagram?
-   [ ] Entity representation
-   [ ] Attribute representation
-   [ ] Primary key representation
-   [ ] Relationship representation
-   [ ] Cardinality notation
-   [ ] Convert ER diagrams into tables
-   [ ] Convert many-to-many relationships into junction tables

### 5.3 Real-world modeling

-   [ ] Student enrollment system
-   [ ] E-commerce database
-   [ ] University management database
-   [ ] Banking database --- basic
-   [ ] Blog application database

### Practical work

-   [ ] Draw an ER diagram for a university.
-   [ ] Design students, departments, and courses.
-   [ ] Design enrollments using a junction table.
-   [ ] Convert the ER diagram into SQL tables.
-   [ ] Add primary and foreign key constraints.


## Phase 06 - Database Normalization

-   [ ] What is normalization?
-   [ ] Why normalization is needed
-   [ ] Database anomalies
-   [ ] Insertion anomaly
-   [ ] Update anomaly
-   [ ] Deletion anomaly
-   [ ] Functional dependency
-   [ ] Partial dependency
-   [ ] Transitive dependency
-   [ ] First Normal Form (1NF)
-   [ ] Second Normal Form (2NF)
-   [ ] Third Normal Form (3NF)
-   [ ] BCNF --- basic understanding
-   [ ] Denormalization --- basic concept

### Practical work

-   [ ] Convert an unnormalized table into 1NF.
-   [ ] Convert 1NF into 2NF.
-   [ ] Convert 2NF into 3NF.
-   [ ] Identify database anomalies.
-   [ ] Normalize a student enrollment database.


## Phase 07 - Transactions and Concurrency

### 7.1 Transactions

-   [ ] What is a transaction?
-   [ ] Transaction lifecycle
-   [ ] ACID properties
-   [ ] Atomicity
-   [ ] Consistency
-   [ ] Isolation
-   [ ] Durability
-   [ ] `COMMIT`
-   [ ] `ROLLBACK`
-   [ ] `SAVEPOINT`

### 7.2 Concurrency

-   [ ] What is concurrency?
-   [ ] Concurrent transactions
-   [ ] Dirty reads
-   [ ] Non-repeatable reads
-   [ ] Phantom reads
-   [ ] Lost updates
-   [ ] Locks --- basic
-   [ ] Shared and exclusive locks --- basic
-   [ ] Deadlocks
-   [ ] Isolation levels

### Practical work

-   [ ] Create a bank transfer transaction.
-   [ ] Transfer money between two accounts.
-   [ ] Test `COMMIT` and `ROLLBACK`.
-   [ ] Understand what happens when a transaction fails.
-   [ ] Experiment with two database sessions.


## Phase 08 - Indexing and Query Optimization

-   [ ] What is an index?
-   [ ] Why indexes are needed
-   [ ] How indexes work --- basic
-   [ ] B-tree index
-   [ ] Unique index
-   [ ] Composite index
-   [ ] Primary key indexing
-   [ ] Indexing foreign keys --- where appropriate
-   [ ] Index advantages and disadvantages
-   [ ] Full table scan
-   [ ] Query execution plan
-   [ ] `EXPLAIN PLAN` --- Oracle
-   [ ] `EXPLAIN` --- PostgreSQL
-   [ ] Query optimization basics
-   [ ] Avoiding unnecessary `SELECT *`
-   [ ] Understanding pagination
-   [ ] Why too many indexes can hurt performance

### Practical work

-   [ ] Create an index.
-   [ ] Compare query plans before and after indexing.
-   [ ] Create a composite index.
-   [ ] Examine a slow query.
-   [ ] Identify which columns may benefit from indexing.


## Phase 09 - Real-world Database Engineering Essentials

### 9.1 Database security

-   [ ] Database users
-   [ ] Roles and permissions
-   [ ] `GRANT`
-   [ ] `REVOKE`
-   [ ] Least privilege principle
-   [ ] SQL injection --- concept
-   [ ] Parameterized queries
-   [ ] Secure database credentials

### 9.2 Database objects

-   [ ] Views
-   [ ] Materialized views --- basic
-   [ ] Sequences
-   [ ] Stored procedures --- basic
-   [ ] Functions --- basic
-   [ ] Triggers --- basic
-   [ ] Constraints in production databases

### 9.3 Backup and recovery

-   [ ] Why database backups matter
-   [ ] Logical backup vs physical backup
-   [ ] Database restore
-   [ ] Recovery concepts
-   [ ] Point-in-time recovery --- basic
-   [ ] Data migration basics

### 9.4 Backend and database integration

-   [ ] How a backend connects to a database
-   [ ] Database drivers
-   [ ] Connection strings
-   [ ] Connection pooling --- basic
-   [ ] CRUD from backend
-   [ ] ORM concept
-   [ ] Prisma basics
-   [ ] Database migrations
-   [ ] Transactions from backend
-   [ ] Environment variables
-   [ ] Pagination and filtering from APIs

### Practical work

-   [ ] Connect Node.js to PostgreSQL.
-   [ ] Create a CRUD API.
-   [ ] Use parameterized queries.
-   [ ] Implement database migrations.
-   [ ] Use Prisma to model database tables.
-   [ ] Implement pagination.


## Phase 10 - Real-world Projects

**Recommended project:** University Management System database.

Build a relational database that supports students, teachers,
departments, courses, enrollments, attendance, and results.

### 10.1 Database design

-   [ ] Create the university database/schema.
-   [ ] Design the ER diagram.
-   [ ] Create `departments` table.
-   [ ] Create `students` table.
-   [ ] Create `teachers` table.
-   [ ] Create `courses` table.
-   [ ] Create `enrollments` table.
-   [ ] Create `semesters` table.
-   [ ] Create `attendance` table.
-   [ ] Create `results` table.
-   [ ] Define primary keys.
-   [ ] Define foreign keys.
-   [ ] Add appropriate constraints.
-   [ ] Normalize the database.
-   [ ] Insert realistic sample data.

### 10.2 SQL implementation

-   [ ] Implement CRUD queries.
-   [ ] Write JOIN queries.
-   [ ] Write GROUP BY reports.
-   [ ] Write subqueries.
-   [ ] Create views.
-   [ ] Add indexes where useful.
-   [ ] Implement transactions.
-   [ ] Test data integrity.
-   [ ] Test query performance.

### 10.3 Backend integration

-   [ ] Connect the database with Node.js.
-   [ ] Build student CRUD endpoints.
-   [ ] Build course enrollment endpoints.
-   [ ] Build teacher endpoints.
-   [ ] Implement validation.
-   [ ] Handle database errors.
-   [ ] Implement pagination.
-   [ ] Test API endpoints.


##  Daily Study Strategy

**Daily Study Time:** 90 Minutes

**Roadmap Duration:** 60 Days

| Activity | Time | Focus |
|:---|:---:|:---|
| Concept Learning | 25 min | Understand DBMS concepts and theory |
| SQL Practice | 35 min | Write queries and perform hands-on exercises |
| Problem Solving | 15 min | Solve SQL problems and practice ER diagrams |
| Revision & Notes | 15 min | Review concepts and document key learnings |
| **Total** | **90 min** | **Focused daily learning** |
