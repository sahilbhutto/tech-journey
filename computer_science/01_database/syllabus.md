# DBMS Engineering Syllabus

# PHASE 0: Database Engineering

##  What Is a Database?

- [X] What is data?
- [X] What is a database?
- [X] What is a DBMS?
- [X] What is an RDBMS?
- [X] Database vs DBMS vs RDBMS
- [X] Database server
- [X] Database client
- [X] Database schema
- [X] Tables
- [X] Rows
- [X] Columns
- [X] Records
- [X] Metadata

---

# PHASE 1: Relational Database Fundamentals

## 1.1 Relational Model

- [ ] Relational model
- [ ] Relation
- [ ] Tuple
- [ ] Attribute
- [ ] Domain
- [ ] Schema
- [ ] Instance
- [ ] Relational algebra basics

## 1.2 Keys

- [ ] Super key
- [ ] Candidate key
- [ ] Primary key
- [ ] Alternate key
- [ ] Foreign key
- [ ] Composite key
- [ ] Natural key
- [ ] Surrogate key
- [ ] UUID
- [ ] Auto-incrementing IDs

## 1.3 Integrity

- [ ] Entity integrity
- [ ] Referential integrity
- [ ] Domain integrity
- [ ] Business-rule integrity
- [ ] Data consistency

## 1.4 Constraints

- [ ] PRIMARY KEY
- [ ] FOREIGN KEY
- [ ] UNIQUE
- [ ] NOT NULL
- [ ] CHECK
- [ ] DEFAULT
- [ ] ON DELETE CASCADE
- [ ] ON DELETE RESTRICT
- [ ] ON DELETE SET NULL
- [ ] ON UPDATE behavior

---

# PHASE 2: SQL Foundations

## 2.1 SQL Fundamentals

- [ ] What is SQL?
- [ ] SQL categories
- [ ] DDL
- [ ] DML
- [ ] DQL
- [ ] DCL
- [ ] TCL

## 2.2 Database & Table Operations

- [ ] CREATE DATABASE
- [ ] DROP DATABASE
- [ ] CREATE TABLE
- [ ] ALTER TABLE
- [ ] DROP TABLE
- [ ] TRUNCATE
- [ ] CREATE SCHEMA
- [ ] Rename tables
- [ ] Rename columns

## 2.3 Data Types

- [ ] Integer
- [ ] BIGINT
- [ ] DECIMAL
- [ ] NUMERIC
- [ ] FLOAT
- [ ] BOOLEAN
- [ ] CHAR
- [ ] VARCHAR
- [ ] TEXT
- [ ] DATE
- [ ] TIME
- [ ] TIMESTAMP
- [ ] TIMESTAMPTZ
- [ ] UUID
- [ ] JSON
- [ ] JSONB
- [ ] Arrays
- [ ] Choosing appropriate data types

## 2.4 INSERT

- [ ] INSERT
- [ ] Insert multiple rows
- [ ] Insert from SELECT
- [ ] DEFAULT values
- [ ] RETURNING

## 2.5 SELECT

- [ ] SELECT
- [ ] SELECT *
- [ ] Selecting specific columns
- [ ] Column aliases
- [ ] Expressions
- [ ] DISTINCT
- [ ] ORDER BY
- [ ] LIMIT
- [ ] OFFSET

## 2.6 Filtering

- [ ] WHERE
- [ ] AND
- [ ] OR
- [ ] NOT
- [ ] IN
- [ ] NOT IN
- [ ] BETWEEN
- [ ] LIKE
- [ ] ILIKE
- [ ] IS NULL
- [ ] IS NOT NULL

## 2.7 NULL

- [ ] What NULL means
- [ ] NULL comparisons
- [ ] Three-valued logic
- [ ] COALESCE
- [ ] NULLIF

---

# PHASE 3: SQL Intermediate

## 3.1 UPDATE

- [ ] UPDATE
- [ ] Updating multiple rows
- [ ] Conditional updates
- [ ] RETURNING
- [ ] Safe UPDATE practices

## 3.2 DELETE

- [ ] DELETE
- [ ] Conditional DELETE
- [ ] RETURNING
- [ ] DELETE vs TRUNCATE

## 3.3 CASE

- [ ] CASE expressions
- [ ] Simple CASE
- [ ] Searched CASE
- [ ] Conditional data transformation

## 3.4 Aggregate Functions

- [ ] COUNT
- [ ] SUM
- [ ] AVG
- [ ] MIN
- [ ] MAX
- [ ] COUNT DISTINCT

## 3.5 GROUP BY

- [ ] GROUP BY
- [ ] Multiple grouping columns
- [ ] HAVING
- [ ] WHERE vs HAVING
- [ ] Aggregation patterns

---

# PHASE 4: SQL Advanced

## 4.1 Joins

- [ ] INNER JOIN
- [ ] LEFT JOIN
- [ ] RIGHT JOIN
- [ ] FULL OUTER JOIN
- [ ] CROSS JOIN
- [ ] SELF JOIN
- [ ] Multiple joins
- [ ] Join conditions
- [ ] Join filtering
- [ ] Understanding duplicate rows
- [ ] Join performance

## 4.2 Subqueries

- [ ] Subqueries
- [ ] Scalar subqueries
- [ ] Multi-row subqueries
- [ ] Correlated subqueries
- [ ] EXISTS
- [ ] NOT EXISTS
- [ ] IN
- [ ] NOT IN
- [ ] Subquery vs JOIN

## 4.3 Set Operations

- [ ] UNION
- [ ] UNION ALL
- [ ] INTERSECT
- [ ] EXCEPT

## 4.4 Common Table Expressions

- [ ] WITH
- [ ] Multiple CTEs
- [ ] CTE composition
- [ ] Recursive CTEs
- [ ] Hierarchical data
- [ ] CTE readability
- [ ] CTE performance considerations

---

# PHASE 5: SQL Window Functions

## 5.1 Window Fundamentals

- [ ] What is a window function?
- [ ] OVER()
- [ ] PARTITION BY
- [ ] ORDER BY
- [ ] Window frames

## 5.2 Ranking

- [ ] ROW_NUMBER
- [ ] RANK
- [ ] DENSE_RANK
- [ ] NTILE

## 5.3 Navigation

- [ ] LAG
- [ ] LEAD
- [ ] FIRST_VALUE
- [ ] LAST_VALUE

## 5.4 Analytical Patterns

- [ ] Running totals
- [ ] Moving averages
- [ ] Ranking within groups
- [ ] Top-N per group
- [ ] Previous/next record comparison
- [ ] Percentage calculations
- [ ] Time-series analysis

---

# PHASE 6: Database Design

## 6.1 Requirements → Database

- [ ] Extract entities from requirements
- [ ] Extract attributes
- [ ] Identify relationships
- [ ] Identify cardinality
- [ ] Identify optional relationships
- [ ] Identify business constraints
- [ ] Identify lifecycle of data
- [ ] Identify access patterns

## 6.2 Entity Relationship Modeling

- [ ] ER diagrams
- [ ] Entities
- [ ] Attributes
- [ ] Relationships
- [ ] One-to-one
- [ ] One-to-many
- [ ] Many-to-many
- [ ] Junction tables
- [ ] Weak entities
- [ ] Recursive relationships

## 6.3 Schema Design

- [ ] Table naming conventions
- [ ] Column naming conventions
- [ ] Primary key strategy
- [ ] Foreign key strategy
- [ ] Audit columns
- [ ] Created-at / updated-at
- [ ] Status fields
- [ ] Soft deletes
- [ ] Historical records
- [ ] Versioning data

---

# PHASE 7: Normalization

## 7.1 Functional Dependencies

- [ ] Functional dependency
- [ ] Full functional dependency
- [ ] Partial dependency
- [ ] Transitive dependency

## 7.2 Normal Forms

- [ ] First Normal Form: 1NF
- [ ] Second Normal Form: 2NF
- [ ] Third Normal Form: 3NF
- [ ] Boyce-Codd Normal Form: BCNF

## 7.3 Practical Normalization

- [ ] Normalize a real database
- [ ] Detect redundant data
- [ ] Detect update anomalies
- [ ] Detect insert anomalies
- [ ] Detect delete anomalies

## 7.4 Denormalization

- [ ] Why denormalize?
- [ ] Read performance
- [ ] Reporting requirements
- [ ] Aggregated data
- [ ] Controlled duplication
- [ ] Denormalization trade-offs

---

# PHASE 8: Transactions & ACID

## 8.1 Transactions

- [ ] What is a transaction?
- [ ] BEGIN
- [ ] COMMIT
- [ ] ROLLBACK
- [ ] SAVEPOINT
- [ ] Transaction boundaries

## 8.2 ACID

- [ ] Atomicity
- [ ] Consistency
- [ ] Isolation
- [ ] Durability

## 8.3 Real Transaction Examples

- [ ] Bank transfer
- [ ] Order creation
- [ ] Payment processing
- [ ] Inventory reservation
- [ ] Ticket booking
- [ ] Seat reservation

---

# PHASE 9: Concurrency Control

## 9.1 Concurrency Problems

- [ ] Race conditions
- [ ] Lost updates
- [ ] Dirty reads
- [ ] Non-repeatable reads
- [ ] Phantom reads
- [ ] Write conflicts

## 9.2 Isolation Levels

- [ ] Read Uncommitted
- [ ] Read Committed
- [ ] Repeatable Read
- [ ] Serializable
- [ ] Isolation-level trade-offs

## 9.3 Locking

- [ ] Shared locks
- [ ] Exclusive locks
- [ ] Row-level locks
- [ ] Table-level locks
- [ ] SELECT FOR UPDATE
- [ ] Lock contention
- [ ] Deadlocks
- [ ] Deadlock detection
- [ ] Deadlock prevention

## 9.4 MVCC

- [ ] MVCC concept
- [ ] Why MVCC exists
- [ ] MVCC in PostgreSQL
- [ ] Transaction snapshots
- [ ] Visibility concepts

---

# PHASE 10: Indexing

## 10.1 Index Fundamentals

- [ ] Why indexes exist
- [ ] Index lookup
- [ ] Index overhead
- [ ] Read vs write trade-offs
- [ ] When NOT to create an index

## 10.2 Index Types

- [ ] B-tree
- [ ] Hash
- [ ] GIN
- [ ] GiST
- [ ] BRIN

## 10.3 Index Design

- [ ] Single-column indexes
- [ ] Composite indexes
- [ ] Column order
- [ ] Selectivity
- [ ] Cardinality
- [ ] Unique indexes
- [ ] Partial indexes
- [ ] Expression indexes
- [ ] Covering indexes
- [ ] Index-only scans

## 10.4 Index Mistakes

- [ ] Over-indexing
- [ ] Wrong column order
- [ ] Indexing low-value columns blindly
- [ ] Ignoring query patterns
- [ ] Ignoring write overhead

---

# PHASE 11: Query Optimization

## 11.1 Query Planning

- [ ] Query planner
- [ ] Query optimizer
- [ ] Cost estimation
- [ ] Statistics
- [ ] Execution plans

## 11.2 EXPLAIN

- [ ] EXPLAIN
- [ ] EXPLAIN ANALYZE
- [ ] Sequential scan
- [ ] Index scan
- [ ] Bitmap scan
- [ ] Nested loop
- [ ] Hash join
- [ ] Merge join
- [ ] Sort
- [ ] Aggregate
- [ ] Estimated vs actual rows

## 11.3 Performance Problems

- [ ] Slow queries
- [ ] Missing indexes
- [ ] Incorrect indexes
- [ ] N+1 queries
- [ ] Large OFFSET pagination
- [ ] Unnecessary columns
- [ ] Expensive joins
- [ ] Expensive sorting
- [ ] Poor filtering
- [ ] Lock contention

## 11.4 Pagination

- [ ] LIMIT/OFFSET pagination
- [ ] Cursor pagination
- [ ] Keyset pagination
- [ ] Pagination indexes
- [ ] Pagination at scale

---

# PHASE 12: PostgreSQL Engineering

## 12.1 PostgreSQL Fundamentals

- [ ] Install PostgreSQL
- [ ] PostgreSQL server
- [ ] PostgreSQL client
- [ ] psql
- [ ] Databases
- [ ] Schemas
- [ ] Roles
- [ ] Users
- [ ] Permissions
- [ ] Extensions

## 12.2 PostgreSQL Data Features

- [ ] JSON
- [ ] JSONB
- [ ] Arrays
- [ ] UUID
- [ ] ENUM
- [ ] Generated columns
- [ ] Identity columns
- [ ] Sequences

## 12.3 PostgreSQL Objects

- [ ] Views
- [ ] Materialized views
- [ ] Functions
- [ ] Procedures
- [ ] Triggers
- [ ] Extensions

## 12.4 PostgreSQL Maintenance

- [ ] VACUUM
- [ ] ANALYZE
- [ ] Autovacuum
- [ ] Statistics
- [ ] Database logs
- [ ] Configuration basics

---

# PHASE 13: Backend + Database Engineering

## 13.1 Application Database Layer

- [ ] Database drivers
- [ ] Database connections
- [ ] Connection lifecycle
- [ ] Connection pooling
- [ ] Environment variables
- [ ] Database configuration

## 13.2 Node.js + PostgreSQL

- [ ] PostgreSQL driver
- [ ] Parameterized queries
- [ ] SQL injection prevention
- [ ] Transactions
- [ ] Connection pooling
- [ ] Error handling
- [ ] Database timeouts

## 13.3 Migrations

- [ ] Why migrations exist
- [ ] Migration files
- [ ] Schema versioning
- [ ] Forward migrations
- [ ] Rollbacks
- [ ] Production migration safety
- [ ] Seed data

## 13.4 Data Access Architecture

- [ ] Data access layer
- [ ] Repository pattern
- [ ] Service layer
- [ ] Transaction boundaries
- [ ] Query organization
- [ ] Database error handling

---

# PHASE 14: ORM Engineering

## 14.1 ORM Fundamentals

- [ ] What is an ORM?
- [ ] Benefits of ORMs
- [ ] ORM limitations
- [ ] ORM vs raw SQL
- [ ] Query builders

## 14.2 Prisma

- [ ] Prisma setup
- [ ] Prisma schema
- [ ] Models
- [ ] Relations
- [ ] Migrations
- [ ] CRUD
- [ ] Filtering
- [ ] Pagination
- [ ] Transactions
- [ ] Nested queries
- [ ] Raw SQL
- [ ] Prisma performance

## 14.3 ORM Pitfalls

- [ ] N+1 queries
- [ ] Unnecessary data fetching
- [ ] Hidden queries
- [ ] Incorrect relation loading
- [ ] Over-reliance on ORM
- [ ] Knowing when raw SQL is better

---

# PHASE 15: NoSQL Fundamentals

## 15.1 Why NoSQL?

- [ ] Why NoSQL databases exist
- [ ] SQL vs NoSQL
- [ ] Document databases
- [ ] Key-value databases
- [ ] Wide-column databases
- [ ] Graph databases
- [ ] NoSQL trade-offs

## 15.2 MongoDB

- [ ] Documents
- [ ] Collections
- [ ] BSON
- [ ] CRUD
- [ ] Query operators
- [ ] Aggregation pipeline
- [ ] Indexes
- [ ] Schema design
- [ ] Embedding
- [ ] Referencing
- [ ] Transactions
- [ ] MongoDB performance

## 15.3 MongoDB Data Modeling

- [ ] Access-pattern-driven design
- [ ] Embedding vs referencing
- [ ] One-to-one
- [ ] One-to-many
- [ ] Many-to-many
- [ ] Denormalization
- [ ] Document size considerations

---

# PHASE 16: Redis & Caching

## 16.1 Redis Fundamentals

- [ ] Redis architecture
- [ ] Key-value model
- [ ] Strings
- [ ] Hashes
- [ ] Lists
- [ ] Sets
- [ ] Sorted sets
- [ ] TTL

## 16.2 Redis Use Cases

- [ ] Caching
- [ ] Sessions
- [ ] Rate limiting
- [ ] Counters
- [ ] Leaderboards
- [ ] Pub/Sub
- [ ] Temporary data

## 16.3 Caching Strategies

- [ ] Cache-aside
- [ ] Write-through
- [ ] Write-behind
- [ ] Cache invalidation
- [ ] TTL strategy
- [ ] Cache stampede
- [ ] Cache consistency

## 16.4 When NOT to Cache

- [ ] Avoid unnecessary caching
- [ ] Understand invalidation complexity
- [ ] Measure before optimizing

---

# PHASE 17: Database Security

## 17.1 Authentication & Authorization

- [ ] Database users
- [ ] Roles
- [ ] Permissions
- [ ] Least privilege
- [ ] Service accounts
- [ ] Role-based access

## 17.2 SQL Injection

- [ ] SQL injection fundamentals
- [ ] Parameterized queries
- [ ] Prepared statements
- [ ] ORM safety
- [ ] Dynamic SQL risks

## 17.3 Data Protection

- [ ] Encryption in transit
- [ ] Encryption at rest
- [ ] Password hashing
- [ ] Secrets management
- [ ] Sensitive data handling
- [ ] Audit logging
- [ ] Data retention

## 17.4 Security Engineering

- [ ] Principle of least privilege
- [ ] Secure database configuration
- [ ] Network access control
- [ ] Backup security
- [ ] Credential rotation

---

# PHASE 18: Database Reliability

## 18.1 Backups

- [ ] Why backups matter
- [ ] Logical backups
- [ ] Physical backups
- [ ] Backup frequency
- [ ] Backup verification
- [ ] Restore testing

## 18.2 Disaster Recovery

- [ ] Disaster recovery
- [ ] RPO
- [ ] RTO
- [ ] Recovery procedures
- [ ] Failure scenarios
- [ ] Recovery testing

## 18.3 Replication

- [ ] Replication fundamentals
- [ ] Primary/replica architecture
- [ ] Read replicas
- [ ] Replication lag
- [ ] Failover
- [ ] High availability

---

# PHASE 19: Database Scaling

## 19.1 Vertical Scaling

- [ ] CPU scaling
- [ ] RAM scaling
- [ ] Storage scaling
- [ ] I/O considerations

## 19.2 Horizontal Scaling

- [ ] Read replicas
- [ ] Database partitioning
- [ ] Sharding
- [ ] Distributed databases
- [ ] Horizontal scaling trade-offs

## 19.3 Partitioning

- [ ] Why partition tables?
- [ ] Range partitioning
- [ ] List partitioning
- [ ] Hash partitioning
- [ ] Partition pruning
- [ ] Partition maintenance

## 19.4 Sharding

- [ ] What is sharding?
- [ ] Shard keys
- [ ] Hash-based sharding
- [ ] Range-based sharding
- [ ] Hot shards
- [ ] Cross-shard queries
- [ ] Rebalancing
- [ ] Why sharding should not be the first solution

---

# PHASE 20: Database Internals

## 20.1 Storage

- [ ] Database pages
- [ ] Disk storage
- [ ] Memory buffers
- [ ] Buffer cache
- [ ] Data files
- [ ] Storage hierarchy

## 20.2 Index Internals

- [ ] B-tree structure
- [ ] Index pages
- [ ] Index traversal
- [ ] Index height
- [ ] Index maintenance

## 20.3 PostgreSQL Internals

- [ ] PostgreSQL process architecture
- [ ] Shared buffers
- [ ] WAL
- [ ] Checkpoints
- [ ] MVCC
- [ ] Transaction IDs
- [ ] VACUUM internals

---

# PHASE 21: Distributed Database Concepts

## 21.1 Distributed Systems Basics

- [ ] Distributed systems fundamentals
- [ ] Network failures
- [ ] Partial failures
- [ ] Latency
- [ ] Replication
- [ ] Coordination

## 21.2 Consistency

- [ ] Strong consistency
- [ ] Eventual consistency
- [ ] Read-after-write consistency
- [ ] Consistency trade-offs

## 21.3 CAP

- [ ] CAP theorem
- [ ] Consistency
- [ ] Availability
- [ ] Partition tolerance
- [ ] Practical CAP trade-offs

## 21.4 Distributed Transactions

- [ ] Distributed transactions
- [ ] Two-phase commit
- [ ] Transaction coordination
- [ ] Distributed transaction limitations

---

# PHASE 22: OLAP & Data Warehousing

## 22.1 OLTP vs OLAP

- [ ] OLTP characteristics
- [ ] OLAP characteristics
- [ ] Transactional databases
- [ ] Analytical databases
- [ ] Operational vs analytical workloads

## 22.2 Data Warehouse

- [ ] Data warehouse fundamentals
- [ ] Fact tables
- [ ] Dimension tables
- [ ] Star schema
- [ ] Snowflake schema
- [ ] Slowly changing dimensions

## 22.3 Data Pipelines

- [ ] ETL
- [ ] ELT
- [ ] Data ingestion
- [ ] Data transformation
- [ ] Batch processing
- [ ] Data quality

---

# PHASE 23: Database Observability

## 23.1 Metrics

- [ ] Query latency
- [ ] Query throughput
- [ ] Connection count
- [ ] CPU usage
- [ ] Memory usage
- [ ] Disk usage
- [ ] I/O
- [ ] Cache hit ratio
- [ ] Lock contention

## 23.2 Monitoring

- [ ] Slow query monitoring
- [ ] Database logs
- [ ] Error monitoring
- [ ] Connection monitoring
- [ ] Replication monitoring
- [ ] Storage monitoring

## 23.3 Debugging

- [ ] Identify symptoms
- [ ] Reproduce problem
- [ ] Inspect query
- [ ] Inspect execution plan
- [ ] Inspect indexes
- [ ] Inspect locks
- [ ] Inspect resources
- [ ] Measure before optimization
- [ ] Verify optimization

---

# PHASE 24: Database System Design

## 24.1 System Design Process

- [ ] Clarify requirements
- [ ] Define functional requirements
- [ ] Define non-functional requirements
- [ ] Identify entities
- [ ] Design schema
- [ ] Identify access patterns
- [ ] Estimate data volume
- [ ] Estimate traffic
- [ ] Identify bottlenecks
- [ ] Define consistency requirements
- [ ] Define availability requirements

## 24.2 Database Architecture

- [ ] Primary database
- [ ] Read replicas
- [ ] Cache
- [ ] Search engine
- [ ] Object storage
- [ ] Message queues
- [ ] Background workers

## 24.3 Scaling Decisions

- [ ] Add indexes
- [ ] Optimize queries
- [ ] Add caching
- [ ] Connection pooling
- [ ] Read replicas
- [ ] Partitioning
- [ ] Sharding
- [ ] Database migration strategies

---

# PHASE 25: Real-World Database Design Exercises

## E-Commerce

- [ ] Users
- [ ] Products
- [ ] Categories
- [ ] Inventory
- [ ] Cart
- [ ] Orders
- [ ] Order items
- [ ] Payments
- [ ] Addresses
- [ ] Reviews
- [ ] Coupons
- [ ] Transactions
- [ ] Index strategy
- [ ] Scaling strategy

## University Management

- [ ] Students
- [ ] Teachers
- [ ] Departments
- [ ] Courses
- [ ] Enrollments
- [ ] Classes
- [ ] Exams
- [ ] Results
- [ ] Attendance
- [ ] Fees
- [ ] ERD
- [ ] Normalization
- [ ] Complex SQL reports
- [ ] Index optimization

## Learning Management System

- [ ] Users
- [ ] Courses
- [ ] Lessons
- [ ] Enrollments
- [ ] Progress
- [ ] Assignments
- [ ] Submissions
- [ ] Exams
- [ ] Certificates
- [ ] Payments
- [ ] Analytics

## Social Media

- [ ] Users
- [ ] Profiles
- [ ] Posts
- [ ] Comments
- [ ] Likes
- [ ] Followers
- [ ] Notifications
- [ ] Messages
- [ ] Feeds
- [ ] Media metadata
- [ ] Scaling considerations

## Booking System

- [ ] Users
- [ ] Resources
- [ ] Availability
- [ ] Reservations
- [ ] Payments
- [ ] Cancellation
- [ ] Concurrency handling
- [ ] Prevent double booking
- [ ] Transactions

---

# PHASE 26: Database Projects

## PROJECT 1: SQL Mastery Database

- [ ] Choose a realistic domain
- [ ] Design schema
- [ ] Create tables
- [ ] Add constraints
- [ ] Insert realistic data
- [ ] Write basic queries
- [ ] Write joins
- [ ] Write aggregation queries
- [ ] Write subqueries
- [ ] Write CTEs
- [ ] Write window functions
- [ ] Write 50+ meaningful SQL queries
- [ ] Optimize slow queries

---

## PROJECT 2: University Management Database

- [ ] Requirements document
- [ ] ERD
- [ ] Normalized schema
- [ ] PostgreSQL implementation
- [ ] Constraints
- [ ] Relationships
- [ ] Sample data
- [ ] Complex reports
- [ ] Transactions
- [ ] Indexes
- [ ] Query optimization
- [ ] Backup/restore testing

---

## PROJECT 3: Production E-Commerce Database

- [ ] Requirements
- [ ] ERD
- [ ] PostgreSQL schema
- [ ] Users
- [ ] Products
- [ ] Categories
- [ ] Inventory
- [ ] Orders
- [ ] Payments
- [ ] Reviews
- [ ] Transactions
- [ ] Concurrency handling
- [ ] Indexing
- [ ] Pagination
- [ ] Search
- [ ] Redis caching
- [ ] Database migrations

---

## PROJECT 4: Full-Stack Database System

### Backend

- [ ] Node.js
- [ ] TypeScript
- [ ] PostgreSQL
- [ ] Prisma
- [ ] Raw SQL
- [ ] REST API
- [ ] Authentication
- [ ] Authorization
- [ ] Validation
- [ ] Transactions
- [ ] Error handling

### Database

- [ ] Production-style schema
- [ ] Constraints
- [ ] Migrations
- [ ] Indexes
- [ ] Query optimization
- [ ] Pagination
- [ ] Search
- [ ] Transactions

### Infrastructure

- [ ] Docker
- [ ] PostgreSQL container
- [ ] Redis container
- [ ] Environment configuration
- [ ] Database backup
- [ ] Database restore
- [ ] Logging
- [ ] Monitoring

---

# PHASE 27: Database Testing

## 27.1 Data Integrity Testing

- [ ] Constraint testing
- [ ] Foreign key testing
- [ ] Unique constraint testing
- [ ] NULL handling
- [ ] Transaction rollback testing

## 27.2 Query Testing

- [ ] SQL query tests
- [ ] Edge cases
- [ ] Empty results
- [ ] Duplicate data
- [ ] Large datasets
- [ ] Pagination tests

## 27.3 Performance Testing

- [ ] Benchmark queries
- [ ] Load testing
- [ ] Query latency
- [ ] Concurrent requests
- [ ] Index effectiveness
- [ ] Connection pool behavior

---

# PHASE 28: Database Interview Preparation

## SQL

- [ ] SELECT problems
- [ ] WHERE problems
- [ ] JOIN problems
- [ ] GROUP BY problems
- [ ] HAVING problems
- [ ] Subqueries
- [ ] CTEs
- [ ] Window functions
- [ ] Ranking problems
- [ ] Top-N problems
- [ ] Duplicate detection
- [ ] Missing records
- [ ] Running totals
- [ ] Date problems
- [ ] Consecutive records
- [ ] Complex reporting queries

## DBMS Theory

- [ ] DBMS vs RDBMS
- [ ] Primary key
- [ ] Foreign key
- [ ] Candidate key
- [ ] Normalization
- [ ] Denormalization
- [ ] ACID
- [ ] Transactions
- [ ] Isolation levels
- [ ] Locks
- [ ] Deadlocks
- [ ] MVCC
- [ ] Indexes
- [ ] Query optimization
- [ ] Replication
- [ ] Partitioning
- [ ] Sharding
- [ ] CAP theorem

## Practical Questions

- [ ] Why PostgreSQL?
- [ ] PostgreSQL vs MongoDB?
- [ ] When would you use Redis?
- [ ] How do indexes work?
- [ ] When should you create an index?
- [ ] Why can too many indexes hurt performance?
- [ ] How do you debug a slow query?
- [ ] What is EXPLAIN ANALYZE?
- [ ] How do transactions work?
- [ ] What causes deadlocks?
- [ ] How do you prevent SQL injection?
- [ ] How would you handle millions of rows?
- [ ] How would you scale a database?
- [ ] How would you prevent double booking?
- [ ] How would you design an order/payment transaction?

---

# PHASE 29: Advanced Database System Design Problems

- [ ] Design an e-commerce database
- [ ] Design a payment database
- [ ] Design a banking ledger
- [ ] Design a university system
- [ ] Design an LMS
- [ ] Design a food delivery database
- [ ] Design a ride-sharing database
- [ ] Design a booking system
- [ ] Design a social media database
- [ ] Design a messaging database
- [ ] Design an inventory system
- [ ] Design a notification system

For every system:

- [ ] Requirements
- [ ] Entities
- [ ] ERD
- [ ] Schema
- [ ] Primary keys
- [ ] Foreign keys
- [ ] Constraints
- [ ] Normalization
- [ ] Access patterns
- [ ] Indexes
- [ ] Transactions
- [ ] Concurrency
- [ ] Caching
- [ ] Replication
- [ ] Partitioning
- [ ] Failure scenarios
- [ ] Recovery strategy
- [ ] Scalability
- [ ] Cost considerations
- [ ] Trade-offs

---

# PHASE 30: Final Capstone

# Production-Grade Database System

Build one serious system from requirements to production-like deployment.

## Requirements

- [ ] Write product requirements
- [ ] Define functional requirements
- [ ] Define non-functional requirements
- [ ] Define expected users
- [ ] Define expected traffic
- [ ] Define data volume

## Design

- [ ] Design ERD
- [ ] Identify entities
- [ ] Identify relationships
- [ ] Normalize schema
- [ ] Define constraints
- [ ] Define indexes
- [ ] Define access patterns

## Implementation

- [ ] PostgreSQL
- [ ] Node.js
- [ ] TypeScript
- [ ] Prisma
- [ ] Raw SQL
- [ ] Database migrations
- [ ] Seed data
- [ ] REST API
- [ ] Validation
- [ ] Authentication
- [ ] Authorization

## Reliability

- [ ] Transactions
- [ ] Concurrency control
- [ ] Deadlock handling
- [ ] Backups
- [ ] Restore testing
- [ ] Failure scenarios

## Performance

- [ ] Query benchmarking
- [ ] EXPLAIN ANALYZE
- [ ] Index optimization
- [ ] Pagination
- [ ] Connection pooling
- [ ] Redis caching
- [ ] Load testing

## Production

- [ ] Docker
- [ ] Environment configuration
- [ ] Logging
- [ ] Monitoring
- [ ] Security
- [ ] Backup strategy
- [ ] Recovery strategy
- [ ] Deployment
- [ ] Documentation

## Final Documentation

- [ ] Architecture diagram
- [ ] ERD
- [ ] Database schema
- [ ] API documentation
- [ ] Query optimization report
- [ ] Security decisions
- [ ] Scaling strategy
- [ ] Backup strategy
- [ ] Failure scenarios
- [ ] Engineering trade-offs

---

# PHASE 31: 2026 Priority Matrix

## TIER 1: MUST MASTER

These are the highest-value DBMS skills.

- [ ] Relational database fundamentals
- [ ] SQL
- [ ] SELECT
- [ ] WHERE
- [ ] JOINs
- [ ] GROUP BY
- [ ] Aggregation
- [ ] Subqueries
- [ ] CTEs
- [ ] Window functions
- [ ] ER modeling
- [ ] Database design
- [ ] Normalization
- [ ] Primary/foreign keys
- [ ] Constraints
- [ ] Transactions
- [ ] ACID
- [ ] Isolation levels
- [ ] Concurrency
- [ ] Indexing
- [ ] EXPLAIN ANALYZE
- [ ] PostgreSQL
- [ ] Query optimization
- [ ] Backend database integration
- [ ] SQL injection prevention

---

# TIER 2: STRONGLY RECOMMENDED

- [ ] Prisma
- [ ] Raw SQL
- [ ] Connection pooling
- [ ] Database migrations
- [ ] Redis
- [ ] MongoDB
- [ ] Caching
- [ ] Pagination
- [ ] Database security
- [ ] Backups
- [ ] Replication
- [ ] Partitioning
- [ ] Observability
- [ ] Database system design

---

# TIER 3: ADVANCED

Learn these after mastering the core.

- [ ] PostgreSQL internals
- [ ] WAL
- [ ] Advanced MVCC
- [ ] Advanced indexing
- [ ] Advanced partitioning
- [ ] Sharding
- [ ] Distributed transactions
- [ ] CAP theorem
- [ ] Distributed databases
- [ ] Data warehouses
- [ ] OLAP systems
- [ ] Advanced replication architectures

---

# DATABASE LEARNING LOOP

For every important concept:

1. [ ] Understand the concept
2. [ ] Write the SQL yourself
3. [ ] Run it against PostgreSQL
4. [ ] Break it intentionally
5. [ ] Observe the error
6. [ ] Test edge cases
7. [ ] Understand performance
8. [ ] Apply it to a real system
9. [ ] Explain it without notes
10. [ ] Solve an interview problem

---

# DATABASE ENGINEERING MENTAL MODEL

When designing or debugging any database, ask:

## 1. DATA

- [ ] What data do we store?
- [ ] What entities exist?
- [ ] What relationships exist?

## 2. CORRECTNESS

- [ ] What must always be true?
- [ ] What constraints enforce it?
- [ ] Where are transactions required?

## 3. ACCESS

- [ ] How will the application read the data?
- [ ] How will it write the data?
- [ ] Which queries are most frequent?

## 4. PERFORMANCE

- [ ] How much data?
- [ ] How many requests?
- [ ] Which queries are slow?
- [ ] Which indexes are required?

## 5. CONCURRENCY

- [ ] Can two users modify the same data?
- [ ] Can race conditions occur?
- [ ] What isolation level is appropriate?

## 6. RELIABILITY

- [ ] What happens if the database fails?
- [ ] How do we recover?
- [ ] What is the RPO?
- [ ] What is the RTO?

## 7. SECURITY

- [ ] Who can access the data?
- [ ] What permissions are required?
- [ ] Is sensitive data protected?

## 8. SCALE

- [ ] What happens at 10x traffic?
- [ ] What happens at 100x data?
- [ ] Do we need caching?
- [ ] Do we need replicas?
- [ ] Do we need partitioning?

---

# FINAL MASTERY CHECKLIST

## Fundamentals

- [ ] I understand how relational databases work.
- [ ] I understand keys and constraints.
- [ ] I can design an ERD.
- [ ] I can normalize a database.
- [ ] I understand when to denormalize.

## SQL

- [ ] I can write SQL without an ORM.
- [ ] I can confidently use JOINs.
- [ ] I can write complex aggregations.
- [ ] I can use subqueries.
- [ ] I can use CTEs.
- [ ] I can use window functions.
- [ ] I can solve real SQL problems.

## Transactions

- [ ] I understand ACID.
- [ ] I understand isolation levels.
- [ ] I understand concurrency.
- [ ] I understand locks.
- [ ] I can reason about deadlocks.
- [ ] I can design safe transactional operations.

## Performance

- [ ] I understand indexes.
- [ ] I can choose indexes based on query patterns.
- [ ] I can read EXPLAIN ANALYZE.
- [ ] I can diagnose slow queries.
- [ ] I understand pagination performance.
- [ ] I understand connection pooling.

## PostgreSQL

- [ ] I can use PostgreSQL confidently.
- [ ] I understand PostgreSQL-specific features.
- [ ] I understand VACUUM and ANALYZE.
- [ ] I understand PostgreSQL MVCC at a practical level.
- [ ] I can operate a production-like PostgreSQL database.

## Backend

- [ ] I can integrate PostgreSQL with Node.js.
- [ ] I can use Prisma effectively.
- [ ] I know when to use raw SQL.
- [ ] I can implement transactions from backend code.
- [ ] I can design a reliable data-access layer.

## NoSQL

- [ ] I understand when SQL is better.
- [ ] I understand when NoSQL is better.
- [ ] I can model MongoDB documents.
- [ ] I can use Redis appropriately.
- [ ] I understand caching trade-offs.

## Production

- [ ] I understand backups.
- [ ] I understand restore procedures.
- [ ] I understand replication.
- [ ] I understand partitioning.
- [ ] I understand scaling strategies.
- [ ] I understand database security.
- [ ] I understand database observability.

## System Design

- [ ] I can design a database for a real product.
- [ ] I can estimate database requirements.
- [ ] I can identify bottlenecks.
- [ ] I can choose indexes.
- [ ] I can choose transaction boundaries.
- [ ] I can choose caching strategies.
- [ ] I can reason about scaling.
- [ ] I can explain engineering trade-offs.

---

## Target Skill Stack

**DBMS Fundamentals**
→ **SQL**
→ **Database Design**
→ **Normalization**
→ **Transactions**
→ **Concurrency**
→ **Indexing**
→ **Query Optimization**
→ **PostgreSQL**
→ **Backend Integration**
→ **Redis**
→ **MongoDB**
→ **Security**
→ **Reliability**
→ **Scaling**
→ **Database System Design**
