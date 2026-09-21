# PostgreSQL + Drizzle Syllabus

**Level:** Intermediate → Production Backend Engineer
**Duration:** ~42 days
**Study Time:** ~2 hours/day
**Primary Database:** PostgreSQL
**ORM:** Drizzle ORM (Primary) / Prisma (Alternative)
**Prerequisites:** JavaScript/TypeScript, Node.js, Express, REST APIs, Zod, basic database concepts
**Projects:** TaskFlow, ChatSpace, SupportDesk AI
**Goal:** Build production-ready PostgreSQL backends with a type-safe ORM, migrations, relationships, transactions, indexes, query optimization, testing, and deployment.

---

# Phase 1: PostgreSQL Foundations

### Goal

Understand PostgreSQL as a database system before depending on an ORM.

### Done when

You can design tables, write SQL queries, understand relationships, and explain why a database design works.

---

## 1.1 PostgreSQL Architecture (Core) | ~2h

- [ ] Understand database → schema → table → row → column
- [ ] Understand PostgreSQL server and database connections
- [ ] Understand schemas
- [ ] Understand `public` schema
- [ ] Understand roles/users
- [ ] Understand database permissions
- [ ] Understand connection strings

### Build

- [ ] Create a PostgreSQL database for **TaskFlow**
- [ ] Create separate development database
- [ ] Connect using CLI and GUI

### Docs

- PostgreSQL official documentation → search: `PostgreSQL current documentation`

---

## 1.2 Tables, Data Types & Constraints (Core) | ~2h

- [ ] `CREATE TABLE`
- [ ] PostgreSQL data types
- [ ] `integer`
- [ ] `bigint`
- [ ] `numeric`
- [ ] `text`
- [ ] `boolean`
- [ ] `date`
- [ ] `timestamp`
- [ ] `timestamptz`
- [ ] `uuid`
- [ ] `jsonb`
- [ ] `NOT NULL`
- [ ] `DEFAULT`
- [ ] `UNIQUE`
- [ ] `CHECK`

### Build

- [ ] Design TaskFlow `users`
- [ ] Design TaskFlow `organizations`
- [ ] Design TaskFlow `projects`

---

## 1.3 Primary Keys & Foreign Keys (Core) | ~2h

- [ ] Primary keys
- [ ] Foreign keys
- [ ] Referential integrity
- [ ] One-to-one relationships
- [ ] One-to-many relationships
- [ ] Many-to-many relationships
- [ ] `ON DELETE`
- [ ] `ON UPDATE`

### Build

- [ ] Connect:
  - users → organizations
  - organizations → projects
  - projects → tasks

---

## 1.4 SQL CRUD & Querying (Core) | ~2h

- [ ] `INSERT`
- [ ] `SELECT`
- [ ] `UPDATE`
- [ ] `DELETE`
- [ ] `WHERE`
- [ ] `AND` / `OR`
- [ ] `IN`
- [ ] `BETWEEN`
- [ ] `LIKE`
- [ ] `IS NULL`
- [ ] `ORDER BY`
- [ ] `LIMIT`
- [ ] `OFFSET`

### Build

- [ ] Implement TaskFlow database operations directly in SQL
- [ ] Write at least 15 useful queries

---

## 1.5 Joins & Relational Queries (Core) | ~2h

- [ ] `INNER JOIN`
- [ ] `LEFT JOIN`
- [ ] `RIGHT JOIN`
- [ ] Many-to-many joins
- [ ] Table aliases
- [ ] Joining multiple tables
- [ ] Avoiding accidental duplicate rows

### Build

- [ ] Query projects with organization information
- [ ] Query tasks with project and assignee information
- [ ] Query users belonging to organizations

---

## 1.6 Aggregation & Grouping (Core) | ~2h

- [ ] `COUNT`
- [ ] `SUM`
- [ ] `AVG`
- [ ] `MIN`
- [ ] `MAX`
- [ ] `GROUP BY`
- [ ] `HAVING`
- [ ] Basic subqueries

### Build

- [ ] TaskFlow dashboard queries:
  - total tasks
  - completed tasks
  - tasks per project
  - tasks per user

---

## Phase 1 Checkpoint

- [ ] Design TaskFlow database schema
- [ ] Create tables using SQL
- [ ] Add constraints
- [ ] Create relationships
- [ ] Write joins
- [ ] Write aggregation queries
- [ ] Explain primary key vs foreign key
- [ ] Explain `WHERE` vs `HAVING`

---

# Phase 2: PostgreSQL Data Modeling

### Goal

Design schemas that remain maintainable as an application grows.

### Done when

You can take application requirements and convert them into a normalized relational database design.

---

## 2.1 Database Normalization (Core) | ~2h

- [ ] Why normalization exists
- [ ] First Normal Form
- [ ] Second Normal Form
- [ ] Third Normal Form
- [ ] Redundant data
- [ ] Update anomalies
- [ ] Insert anomalies
- [ ] Delete anomalies
- [ ] Practical normalization

### Build

- [ ] Refactor an intentionally bad TaskFlow schema

---

## 2.2 Relationship Modeling (Core) | ~2h

- [ ] One-to-one
- [ ] One-to-many
- [ ] Many-to-many
- [ ] Junction tables
- [ ] Composite keys
- [ ] Association tables

### Build

- [ ] TaskFlow:
  - users ↔ organizations
  - users ↔ projects
  - users ↔ tasks
  - tasks ↔ labels

---

## 2.3 UUIDs & ID Strategies (Core) | ~2h

- [ ] Sequential IDs
- [ ] UUIDs
- [ ] UUID generation
- [ ] Public IDs vs internal IDs
- [ ] ID security considerations
- [ ] When UUIDs make sense

### Build

- [ ] Use UUID-based IDs in TaskFlow

---

## 2.4 Timestamps & Audit Fields (Core) | ~2h

- [ ] `created_at`
- [ ] `updated_at`
- [ ] Soft deletion
- [ ] `deleted_at`
- [ ] Audit fields
- [ ] Server-generated timestamps
- [ ] Time zones

### Build

- [ ] Add lifecycle fields to TaskFlow entities

---

## 2.5 PostgreSQL `jsonb` (Next) | ~2h

- [ ] JSON vs JSONB
- [ ] When relational columns are better
- [ ] When JSONB is useful
- [ ] JSONB querying
- [ ] JSONB indexing
- [ ] Avoiding "everything in JSON" schemas

### Build

- [ ] Store flexible TaskFlow project settings using JSONB

---

## 2.6 Database Design Review (Core) | ~2h

- [ ] Design ChatSpace schema
- [ ] Users
- [ ] Conversations
- [ ] Participants
- [ ] Messages
- [ ] Attachments
- [ ] Read status

### Build

- [ ] Draw the complete relational model before writing code

---

## Phase 2 Checkpoint

- [ ] Design TaskFlow schema from requirements
- [ ] Design ChatSpace schema
- [ ] Explain normalization
- [ ] Choose ID strategy
- [ ] Model many-to-many relationships
- [ ] Explain when to use JSONB

---

# Phase 3: Drizzle ORM Fundamentals

### Goal

Use Drizzle to build type-safe database access without losing your understanding of SQL.

### Done when

You can create schemas, query PostgreSQL, and manage migrations using Drizzle.

---

## 3.1 Drizzle Setup & Project Structure (Core) | ~2h

- [ ] Install Drizzle
- [ ] PostgreSQL driver
- [ ] Database connection
- [ ] Environment variables
- [ ] `drizzle.config`
- [ ] Database folder structure
- [ ] Schema organization

### Build

- [ ] Add Drizzle to TaskFlow backend

### Docs

- [ ] Official Drizzle documentation
- [ ] Search: `Drizzle ORM PostgreSQL official docs`

---

## 3.2 Drizzle Schema Definition (Core) | ~2h

- [ ] Tables
- [ ] Columns
- [ ] PostgreSQL types
- [ ] Defaults
- [ ] Constraints
- [ ] Primary keys
- [ ] Foreign keys
- [ ] Relations

### Build

- [ ] Convert TaskFlow SQL schema into Drizzle schema

---

## 3.3 Drizzle Migrations (Core) | ~2h

- [ ] Migration concept
- [ ] Generate migrations
- [ ] Apply migrations
- [ ] Migration history
- [ ] Schema changes
- [ ] Production migrations
- [ ] Migration safety

### Build

- [ ] Create TaskFlow migration history from scratch

---

## 3.4 Basic Drizzle Queries (Core) | ~2h

- [ ] `select`
- [ ] `insert`
- [ ] `update`
- [ ] `delete`
- [ ] `where`
- [ ] `eq`
- [ ] `and`
- [ ] `or`
- [ ] `inArray`
- [ ] ordering
- [ ] limits

### Build

- [ ] Replace TaskFlow raw CRUD SQL with Drizzle queries

---

## 3.5 Drizzle Relations & Joins (Core) | ~2h

- [ ] Relations
- [ ] Relational queries
- [ ] SQL joins
- [ ] Nested results
- [ ] Explicit joins
- [ ] Choosing relation queries vs joins

### Build

- [ ] Fetch:
  - project + tasks
  - task + assignee
  - organization + members

---

## 3.6 Drizzle Transactions (Core) | ~2h

- [ ] What transactions solve
- [ ] `BEGIN`
- [ ] `COMMIT`
- [ ] `ROLLBACK`
- [ ] Drizzle transactions
- [ ] Atomic operations

### Build

- [ ] Create TaskFlow project + initial member in one transaction

---

## Phase 3 Checkpoint

- [ ] Define PostgreSQL schema using Drizzle
- [ ] Generate migrations
- [ ] Run migrations
- [ ] Perform CRUD
- [ ] Write joins
- [ ] Use relations
- [ ] Use transactions

---

# Phase 4: Advanced Queries & Type-Safe Backend

### Goal

Build reusable, type-safe database operations for real APIs.

### Done when

You can implement complex API queries without turning route handlers into database spaghetti.

---

## 4.1 Repository / Database Access Layer (Core) | ~2h

- [ ] Separate database logic from controllers
- [ ] Repository functions
- [ ] Query modules
- [ ] Service layer
- [ ] Dependency boundaries

### Build

- [ ] Create TaskFlow:
  - `user.repository.ts`
  - `project.repository.ts`
  - `task.repository.ts`

---

## 4.2 Dynamic Filtering (Core) | ~2h

- [ ] Optional filters
- [ ] Multiple conditions
- [ ] Safe query construction
- [ ] Whitelisting fields
- [ ] Avoiding SQL injection

### Build

- [ ] TaskFlow task filters:
  - status
  - priority
  - assignee
  - project

---

## 4.3 Sorting & Search (Core) | ~2h

- [ ] Dynamic sorting
- [ ] Allowed sort fields
- [ ] Search conditions
- [ ] Case-insensitive search
- [ ] PostgreSQL text search basics

### Build

- [ ] Search and sort TaskFlow projects/tasks

---

## 4.4 Pagination with PostgreSQL (Core) | ~2h

- [ ] Offset pagination
- [ ] Cursor pagination
- [ ] Stable ordering
- [ ] Pagination metadata
- [ ] Performance implications

### Build

- [ ] TaskFlow task pagination
- [ ] ChatSpace message cursor pagination

---

## 4.5 Aggregation Queries for APIs (Core) | ~2h

- [ ] Dashboard queries
- [ ] Counts
- [ ] Grouping
- [ ] Aggregation
- [ ] Query composition

### Build

- [ ] TaskFlow analytics endpoint

---

## 4.6 Raw SQL with Drizzle (Next) | ~2h

- [ ] Why raw SQL still matters
- [ ] Raw SQL expressions
- [ ] PostgreSQL-specific features
- [ ] Type safety considerations
- [ ] Avoiding unnecessary raw SQL

### Build

- [ ] Implement one complex TaskFlow query using SQL where ORM abstraction becomes less useful

---

## Phase 4 Checkpoint

- [ ] Build reusable repositories
- [ ] Implement filtering
- [ ] Implement sorting
- [ ] Implement cursor pagination
- [ ] Build aggregation endpoints
- [ ] Know when to use ORM vs SQL

---

# Phase 5: Indexes & PostgreSQL Performance

### Goal

Understand why queries become slow and how PostgreSQL executes them.

### Done when

You can identify common database performance problems instead of blindly adding indexes.

---

## 5.1 Index Fundamentals (Core) | ~2h

- [ ] What indexes are
- [ ] Why indexes improve reads
- [ ] Index storage cost
- [ ] Write overhead
- [ ] Primary-key indexes
- [ ] Unique indexes

### Build

- [ ] Analyze TaskFlow tables that need indexes

---

## 5.2 B-Tree Indexes (Core) | ~2h

- [ ] Default PostgreSQL index
- [ ] Equality queries
- [ ] Range queries
- [ ] Sorting
- [ ] Composite indexes

### Build

- [ ] Add appropriate indexes to TaskFlow

---

## 5.3 Composite Indexes (Core) | ~2h

- [ ] Multi-column indexes
- [ ] Column order
- [ ] Query patterns
- [ ] Leftmost-prefix behavior
- [ ] Index selectivity

### Build

- [ ] Optimize TaskFlow:
  - organization + project
  - project + status
  - assignee + status

---

## 5.4 `EXPLAIN` & `EXPLAIN ANALYZE` (Core) | ~2h

- [ ] Query plans
- [ ] Sequential scans
- [ ] Index scans
- [ ] Cost estimates
- [ ] Actual execution time
- [ ] Rows examined
- [ ] Basic plan reading

### Build

- [ ] Compare TaskFlow queries before and after indexing

---

## 5.5 N+1 Query Problem (Core) | ~2h

- [ ] What N+1 means
- [ ] Why ORMs can hide N+1
- [ ] Detecting N+1
- [ ] Joins
- [ ] Batch queries
- [ ] Query optimization

### Build

- [ ] Find and eliminate N+1 queries from TaskFlow

---

## 5.6 Database Performance Strategy (Next) | ~2h

- [ ] Index only where useful
- [ ] Avoid unnecessary columns
- [ ] Pagination
- [ ] Query batching
- [ ] Connection pooling
- [ ] Caching boundaries
- [ ] Measuring before optimizing

### Build

- [ ] Create a TaskFlow database performance checklist

---

## Phase 5 Checkpoint

- [ ] Explain indexes
- [ ] Create composite indexes
- [ ] Read basic `EXPLAIN ANALYZE`
- [ ] Find N+1 queries
- [ ] Optimize a slow endpoint
- [ ] Explain read-performance vs write-cost tradeoffs

---

# Phase 6: Transactions, Concurrency & Reliability

### Goal

Understand the database behavior that separates toy applications from production systems.

### Done when

You can safely handle concurrent operations and maintain data consistency.

---

## 6.1 ACID Transactions (Core) | ~2h

- [ ] Atomicity
- [ ] Consistency
- [ ] Isolation
- [ ] Durability
- [ ] Transaction boundaries

### Build

- [ ] TaskFlow multi-step project creation

---

## 6.2 Isolation Levels (Next) | ~2h

- [ ] Read Uncommitted
- [ ] Read Committed
- [ ] Repeatable Read
- [ ] Serializable
- [ ] Practical PostgreSQL behavior

### Build

- [ ] Create a small concurrent transaction experiment

---

## 6.3 Locks & Concurrent Updates (Next) | ~2h

- [ ] Row locks
- [ ] Table locks
- [ ] `SELECT ... FOR UPDATE`
- [ ] Race conditions
- [ ] Lost updates

### Build

- [ ] Simulate concurrent TaskFlow task updates

---

## 6.4 Upserts (Core) | ~2h

- [ ] Insert-or-update
- [ ] PostgreSQL `ON CONFLICT`
- [ ] Unique constraints
- [ ] Idempotent database operations

### Build

- [ ] Implement TaskFlow membership upsert

---

## 6.5 Soft Delete & Data Lifecycle (Core) | ~2h

- [ ] Soft deletion
- [ ] Hard deletion
- [ ] Restore operations
- [ ] Unique constraints with deleted records
- [ ] Data retention considerations

### Build

- [ ] Add archive/delete behavior to TaskFlow

---

## 6.6 Idempotency & Database Safety (Next) | ~2h

- [ ] Idempotent API operations
- [ ] Unique request keys
- [ ] Duplicate requests
- [ ] Payment/order-style operations
- [ ] Database constraints as safety mechanisms

### Build

- [ ] Implement idempotent TaskFlow operation

---

## Phase 6 Checkpoint

- [ ] Explain ACID
- [ ] Use transactions
- [ ] Explain race conditions
- [ ] Use row locking where appropriate
- [ ] Implement upserts
- [ ] Design idempotent database operations

---

# Phase 7: Production PostgreSQL + ORM Engineering

### Goal

Turn your PostgreSQL + Drizzle knowledge into a production-ready backend stack.

### Done when

You can deploy, test, monitor, and maintain a PostgreSQL-backed Node.js application.

---

## 7.1 Environment & Connection Management (Core) | ~2h

- [ ] Development database
- [ ] Test database
- [ ] Production database
- [ ] Connection strings
- [ ] Connection pooling
- [ ] Secrets
- [ ] Environment validation with Zod

### Build

- [ ] Configure TaskFlow environments safely

---

## 7.2 Database Testing (Core) | ~2h

- [ ] Integration tests
- [ ] Test database
- [ ] Test isolation
- [ ] Seed data
- [ ] Transactions in tests
- [ ] Cleanup strategies

### Build

- [ ] Test TaskFlow repositories and API endpoints

---

## 7.3 Database Seeding (Core) | ~2h

- [ ] Seed scripts
- [ ] Development data
- [ ] Test fixtures
- [ ] Deterministic test data
- [ ] Avoiding production seed mistakes

### Build

- [ ] Create realistic TaskFlow seed data

---

## 7.4 PostgreSQL Backups & Recovery (Core) | ~2h

- [ ] Backup concepts
- [ ] Restore concepts
- [ ] Logical backups
- [ ] Migration safety
- [ ] Disaster recovery basics

### Build

- [ ] Perform a local backup and restore experiment

---

## 7.5 Connection Pooling & Production Configuration (Core) | ~2h

- [ ] Connection pools
- [ ] Pool limits
- [ ] Long-running queries
- [ ] Connection exhaustion
- [ ] Serverless database considerations

### Build

- [ ] Review TaskFlow production database configuration

---

## 7.6 Prisma Fundamentals — Alternative ORM (Bonus) | ~2h

- [ ] Prisma schema
- [ ] Prisma Client
- [ ] Prisma migrations
- [ ] Relations
- [ ] Queries
- [ ] Transactions
- [ ] Prisma vs Drizzle

### Build

- [ ] Rebuild one small TaskFlow module using Prisma

> **Do not study Prisma and Drizzle simultaneously at full depth.**

---

## 7.7 Database Observability (Next) | ~2h

- [ ] Slow query monitoring
- [ ] Query logging
- [ ] Connection monitoring
- [ ] Error tracking
- [ ] Application metrics
- [ ] PostgreSQL monitoring basics

### Build

- [ ] Add database/query observability to TaskFlow

---

## Phase 7 Checkpoint

- [ ] Configure production database
- [ ] Validate environment variables
- [ ] Run migrations safely
- [ ] Seed development data
- [ ] Test database operations
- [ ] Understand backups
- [ ] Understand connection pooling
- [ ] Explain Drizzle vs Prisma

---

# Final Phase: Prove It

## Production Project — TaskFlow Backend

Build a production-style SaaS backend using:

- [ ] Node.js
- [ ] Express
- [ ] TypeScript
- [ ] PostgreSQL
- [ ] Drizzle ORM
- [ ] Zod
- [ ] REST API
- [ ] Authentication
- [ ] Authorization
- [ ] Transactions

### Database

- [ ] Users
- [ ] Organizations
- [ ] Organization members
- [ ] Projects
- [ ] Tasks
- [ ] Comments
- [ ] Labels
- [ ] Notifications
- [ ] Audit logs

### Database Engineering

- [ ] Proper primary keys
- [ ] Foreign keys
- [ ] Constraints
- [ ] Normalized schema
- [ ] UUIDs
- [ ] Timestamps
- [ ] Soft deletion where appropriate
- [ ] Useful indexes
- [ ] Composite indexes
- [ ] Transactions
- [ ] Upserts

### API

- [ ] REST resource design
- [ ] Versioning
- [ ] Zod request validation
- [ ] Central error handling
- [ ] Pagination
- [ ] Filtering
- [ ] Sorting
- [ ] Search
- [ ] Consistent response format

### Performance

- [ ] Analyze important queries
- [ ] Use `EXPLAIN ANALYZE`
- [ ] Remove N+1 queries
- [ ] Optimize indexes
- [ ] Implement cursor pagination
- [ ] Avoid unnecessary database calls

### Testing

- [ ] Repository tests
- [ ] Service tests
- [ ] API integration tests
- [ ] Test database
- [ ] Seed data
- [ ] Error cases
- [ ] Transaction failure cases

### Production

- [ ] Environment validation
- [ ] Secure database credentials
- [ ] Production migrations
- [ ] Connection pooling
- [ ] Health endpoint
- [ ] Logging
- [ ] Database monitoring
- [ ] Backup strategy
- [ ] Deployment

---

# Interview Readiness

- [ ] What is PostgreSQL?
- [ ] PostgreSQL vs MongoDB
- [ ] Primary key vs unique constraint
- [ ] Foreign key and referential integrity
- [ ] Normalization
- [ ] One-to-many vs many-to-many
- [ ] SQL JOINs
- [ ] Indexes
- [ ] Composite indexes
- [ ] B-Tree indexes
- [ ] `EXPLAIN ANALYZE`
- [ ] Transactions
- [ ] ACID
- [ ] Isolation levels
- [ ] Race conditions
- [ ] Row locking
- [ ] Upsert
- [ ] Offset vs cursor pagination
- [ ] N+1 problem
- [ ] Connection pooling
- [ ] Database migrations
- [ ] Soft deletion
- [ ] PostgreSQL vs ORM abstraction
- [ ] Drizzle vs Prisma
- [ ] When to use raw SQL
- [ ] How to optimize a slow query
- [ ] How to design a multi-tenant SaaS database

---

# Production Checklist

## PostgreSQL

- [ ] Schema is normalized where appropriate
- [ ] Constraints protect data integrity
- [ ] Foreign keys are correct
- [ ] Indexes match real query patterns
- [ ] Important queries analyzed
- [ ] Transactions used for multi-step operations
- [ ] Connection pool configured
- [ ] Backup strategy exists

## Drizzle

- [ ] Schema is organized
- [ ] Migrations are version controlled
- [ ] Queries are type-safe
- [ ] Database logic is separated from controllers
- [ ] Complex queries are understood at SQL level
- [ ] Raw SQL is used only when appropriate

## API

- [ ] Validation with Zod
- [ ] Consistent errors
- [ ] Pagination
- [ ] Filtering
- [ ] Sorting
- [ ] Authentication
- [ ] Authorization
- [ ] Rate limiting
- [ ] Logging
- [ ] Health checks

## Code Quality

- [ ] Controllers stay thin
- [ ] Services contain business logic
- [ ] Repositories contain database operations
- [ ] No database queries inside random utility files
- [ ] No duplicated query logic
- [ ] No unbounded queries
- [ ] No unvalidated dynamic SQL fields
- [ ] No secrets committed to Git
