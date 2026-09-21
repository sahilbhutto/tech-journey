# Advanced PostgreSQL + TanStack Query Syllabus

**Topic:** Advanced PostgreSQL + TanStack Query
**Focus:** PostgreSQL production patterns + pagination + caching + optimistic UI
**Level:** Intermediate → Advanced
**Duration:** 14–18 Days
**Prerequisites:** SQL fundamentals, PostgreSQL basics, React, TypeScript, REST APIs, TanStack Query basics

**Projects:**

* TaskFlow — SaaS project
* ChatSpace — Real-time chat
* SupportDesk AI — AI ticketing system

**Goal:** Build production-grade data access and frontend server-state management with PostgreSQL and TanStack Query.

**Progress:** 0 / 38 topics completed

---

# Phase 1: Advanced PostgreSQL Foundations

**Days 1–2**

**Goal:** Understand PostgreSQL beyond basic CRUD and write production-quality SQL.

### 1.1 PostgreSQL Data Types — Core

* [ ] Numeric types
* [ ] Text types
* [ ] Boolean
* [ ] Date/time types
* [ ] UUID
* [ ] JSON / JSONB
* [ ] Arrays
* [ ] ENUM
* [ ] Build: Production-ready TaskFlow schema
* [ ] Done when: You can choose appropriate PostgreSQL types for application data

### 1.2 Constraints — Core

* [ ] PRIMARY KEY
* [ ] FOREIGN KEY
* [ ] UNIQUE
* [ ] NOT NULL
* [ ] CHECK
* [ ] DEFAULT
* [ ] Composite constraints
* [ ] Build: Enforce TaskFlow data integrity
* [ ] Done when: Invalid data is rejected by the database itself

### 1.3 Relationships — Core

* [ ] One-to-one
* [ ] One-to-many
* [ ] Many-to-many
* [ ] Junction tables
* [ ] Foreign-key actions
* [ ] CASCADE
* [ ] RESTRICT
* [ ] SET NULL
* [ ] Build: Users → Projects → Tasks
* [ ] Done when: You can design relational structures without unnecessary duplication

### 1.4 Transactions — Core

* [ ] BEGIN
* [ ] COMMIT
* [ ] ROLLBACK
* [ ] Atomic operations
* [ ] Transaction boundaries
* [ ] Failure handling
* [ ] Build: TaskFlow project creation transaction
* [ ] Done when: Related database operations either all succeed or all fail

### Phase 1 Checkpoint

* [ ] Design relational schema
* [ ] Use constraints correctly
* [ ] Model relationships
* [ ] Use transactions
* [ ] Explain why database constraints matter

---

# Phase 2: Advanced SQL

**Days 3–4**

**Goal:** Write complex queries required by real-world applications.

### 2.1 Advanced JOINs — Core

* [ ] INNER JOIN
* [ ] LEFT JOIN
* [ ] RIGHT JOIN
* [ ] FULL JOIN
* [ ] CROSS JOIN
* [ ] Self joins
* [ ] Multiple-table joins
* [ ] Build: TaskFlow dashboard queries
* [ ] Done when: You can retrieve relational data without unnecessary queries

### 2.2 Subqueries — Core

* [ ] Scalar subqueries
* [ ] Correlated subqueries
* [ ] EXISTS
* [ ] NOT EXISTS
* [ ] IN
* [ ] Build: Task ownership and permission queries
* [ ] Done when: You can solve relational filtering problems using SQL

### 2.3 CTEs — Core

* [ ] WITH
* [ ] Multiple CTEs
* [ ] CTE readability
* [ ] Recursive CTE concept
* [ ] Build: Complex project reporting query
* [ ] Done when: Large queries can be broken into understandable stages

### 2.4 Aggregation — Core

* [ ] COUNT
* [ ] SUM
* [ ] AVG
* [ ] MIN
* [ ] MAX
* [ ] GROUP BY
* [ ] HAVING
* [ ] Build: Task/project statistics
* [ ] Done when: You can build analytics queries directly in PostgreSQL

### 2.5 Window Functions — Next

* [ ] OVER
* [ ] PARTITION BY
* [ ] ORDER BY
* [ ] ROW_NUMBER
* [ ] RANK
* [ ] DENSE_RANK
* [ ] LAG
* [ ] LEAD
* [ ] Build: Task activity analytics
* [ ] Done when: You understand when window functions are better than GROUP BY

### Phase 2 Checkpoint

* [ ] Complex joins
* [ ] Subqueries
* [ ] CTEs
* [ ] Aggregation
* [ ] Window functions

---

# Phase 3: PostgreSQL Indexing & Performance

**Days 5–6**

**Goal:** Understand why queries become slow and how PostgreSQL executes them.

### 3.1 Index Fundamentals — Core

* [ ] What is an index?
* [ ] B-tree indexes
* [ ] Composite indexes
* [ ] Unique indexes
* [ ] Partial indexes
* [ ] Expression indexes
* [ ] Build: Index TaskFlow queries
* [ ] Done when: You can identify columns that benefit from indexing

### 3.2 Composite Indexes — Core

* [ ] Multi-column indexes
* [ ] Column order
* [ ] Selectivity
* [ ] Query patterns
* [ ] Index prefix concepts
* [ ] Build: Project/task filtering indexes
* [ ] Done when: You understand why index column order matters

### 3.3 EXPLAIN — Core

* [ ] EXPLAIN
* [ ] EXPLAIN ANALYZE
* [ ] Sequential scan
* [ ] Index scan
* [ ] Bitmap scan
* [ ] Cost estimates
* [ ] Execution time
* [ ] Build: Analyze slow TaskFlow queries
* [ ] Done when: You can read a basic PostgreSQL query plan

### 3.4 Query Optimization — Core

* [ ] Avoid SELECT *
* [ ] Reduce unnecessary joins
* [ ] Index appropriate filters
* [ ] Pagination performance
* [ ] N+1 query problem
* [ ] Query batching
* [ ] Build: Optimize TaskFlow dashboard
* [ ] Done when: You can investigate and improve a slow query systematically

### 3.5 PostgreSQL Statistics — Bonus

* [ ] Query planner concept
* [ ] Table statistics
* [ ] ANALYZE
* [ ] Cardinality estimates
* [ ] Planner decisions

### Phase 3 Checkpoint

* [ ] Create useful indexes
* [ ] Understand composite indexes
* [ ] Read EXPLAIN output
* [ ] Identify sequential scans
* [ ] Optimize a slow query

---

# Phase 4: Pagination & Large Datasets

**Days 7–8**

**Goal:** Build scalable pagination for production APIs.

### 4.1 Offset Pagination — Core

* [ ] LIMIT
* [ ] OFFSET
* [ ] Page numbers
* [ ] Page size
* [ ] Total count
* [ ] Build: TaskFlow task list
* [ ] Done when: API supports page-based pagination

### 4.2 Offset Pagination Problems — Core

* [ ] Large OFFSET performance
* [ ] Data inserted during pagination
* [ ] Duplicate records
* [ ] Missing records
* [ ] Inconsistent ordering
* [ ] Build: Test pagination under changing data
* [ ] Done when: You understand why OFFSET is not always suitable

### 4.3 Cursor Pagination — Core

* [ ] Cursor concept
* [ ] Stable ordering
* [ ] `WHERE id > cursor`
* [ ] Next cursor
* [ ] Previous cursor
* [ ] Limit
* [ ] Build: Production TaskFlow task API
* [ ] Done when: You can implement cursor pagination correctly

### 4.4 Cursor Pagination with Timestamps — Core

* [ ] Created-at cursor
* [ ] ID tie-breaker
* [ ] Composite ordering
* [ ] Duplicate timestamps
* [ ] Stable pagination
* [ ] Build: ChatSpace message pagination
* [ ] Done when: Pagination remains stable when timestamps are equal

### 4.5 API Pagination Contract — Core

* [ ] `data`
* [ ] `nextCursor`
* [ ] `hasNextPage`
* [ ] Page metadata
* [ ] Sorting
* [ ] Filtering
* [ ] Search
* [ ] Build: Reusable pagination response format
* [ ] Done when: Frontend can consume pagination consistently

### Phase 4 Checkpoint

* [ ] Implement offset pagination
* [ ] Explain its limitations
* [ ] Implement cursor pagination
* [ ] Handle stable ordering
* [ ] Build a paginated REST endpoint

---

# Phase 5: PostgreSQL Concurrency & Production Patterns

**Days 9–10**

**Goal:** Understand the database behavior that matters when multiple users access data simultaneously.

### 5.1 Transactions in Real Applications — Core

* [ ] Transaction boundaries
* [ ] Atomic updates
* [ ] Transaction failures
* [ ] Rollback
* [ ] Service-layer transactions
* [ ] Build: Task assignment workflow
* [ ] Done when: Multi-step operations remain consistent

### 5.2 Isolation Levels — Next

* [ ] Read Committed
* [ ] Repeatable Read
* [ ] Serializable
* [ ] Dirty reads
* [ ] Non-repeatable reads
* [ ] Phantom reads
* [ ] Build: Understand concurrent updates
* [ ] Done when: You can explain common transaction anomalies

### 5.3 Row-Level Locking — Next

* [ ] `FOR UPDATE`
* [ ] Row locks
* [ ] Lock contention
* [ ] Deadlock concept
* [ ] Build: Prevent conflicting task updates
* [ ] Done when: You understand when explicit locking is useful

### 5.4 Soft Deletes — Core

* [ ] Deleted timestamp
* [ ] Filtering deleted records
* [ ] Unique constraints with deleted data
* [ ] Cleanup strategy
* [ ] Build: Soft-delete projects
* [ ] Done when: Deleted records are safely hidden without immediate physical deletion

### 5.5 Audit Data — Next

* [ ] Created timestamps
* [ ] Updated timestamps
* [ ] Created-by
* [ ] Updated-by
* [ ] Audit tables
* [ ] Build: TaskFlow activity history
* [ ] Done when: Important changes can be traced

### Phase 5 Checkpoint

* [ ] Use transactions correctly
* [ ] Explain isolation
* [ ] Understand row locks
* [ ] Handle soft deletes
* [ ] Design audit information

---

# Phase 6: TanStack Query Fundamentals

**Days 11–12**

**Goal:** Manage server state correctly in React.

### 6.1 Server State vs Client State — Core

* [ ] Server state
* [ ] Client state
* [ ] Why server state is different
* [ ] Cache ownership
* [ ] Build: TaskFlow API state architecture
* [ ] Done when: You know what belongs in TanStack Query vs local React state

### 6.2 Query Fundamentals — Core

* [ ] Query keys
* [ ] Query functions
* [ ] `useQuery`
* [ ] Loading state
* [ ] Error state
* [ ] Success state
* [ ] Build: Task list
* [ ] Done when: API data is managed through query caching

### 6.3 Query Keys — Core

* [ ] Static keys
* [ ] Dynamic keys
* [ ] Nested keys
* [ ] Filter-dependent keys
* [ ] Pagination-dependent keys
* [ ] Build: Filtered task queries
* [ ] Done when: Different server states receive correct cache entries

### 6.4 Query Cache — Core

* [ ] Cache lifecycle
* [ ] Stale data
* [ ] Fresh data
* [ ] Garbage collection
* [ ] `staleTime`
* [ ] Cache invalidation
* [ ] Build: Dashboard caching
* [ ] Done when: You understand why data refetches or stays cached

### 6.5 Mutations — Core

* [ ] `useMutation`
* [ ] Mutation function
* [ ] Mutation states
* [ ] Success handling
* [ ] Error handling
* [ ] Invalidation
* [ ] Build: Create/update/delete task
* [ ] Done when: CRUD operations correctly synchronize with queries

### Phase 6 Checkpoint

* [ ] Design query keys
* [ ] Use queries
* [ ] Use mutations
* [ ] Understand stale/fresh data
* [ ] Invalidate related queries

---

# Phase 7: TanStack Query Pagination

**Days 13–14**

**Goal:** Connect production pagination APIs to TanStack Query.

### 7.1 Paginated Queries — Core

* [ ] Page-based query keys
* [ ] Page state
* [ ] Previous/next navigation
* [ ] Loading states
* [ ] Empty states
* [ ] Build: TaskFlow pagination
* [ ] Done when: UI correctly handles page-based APIs

### 7.2 Infinite Queries — Core

* [ ] `useInfiniteQuery`
* [ ] Pages
* [ ] Page parameters
* [ ] Next page
* [ ] Previous page
* [ ] Fetch next page
* [ ] Build: ChatSpace message history
* [ ] Done when: Users can continuously load additional data

### 7.3 Cursor-Based Infinite Scroll — Core

* [ ] Cursor API
* [ ] `getNextPageParam`
* [ ] Cursor persistence
* [ ] Loading indicators
* [ ] End-of-list detection
* [ ] Build: ChatSpace conversation history
* [ ] Done when: Infinite scrolling works with cursor pagination

### 7.4 Prefetching — Next

* [ ] Prefetch next page
* [ ] Prefetch on hover
* [ ] Prefetch detail data
* [ ] Reduce perceived latency
* [ ] Build: TaskFlow project navigation
* [ ] Done when: Frequently expected data is loaded before navigation

### 7.5 Placeholder & Previous Data UX — Next

* [ ] Keep previous data
* [ ] Placeholder data
* [ ] Loading indicators
* [ ] Avoid layout jumps
* [ ] Build: Smooth paginated table
* [ ] Done when: Pagination doesn't produce a poor loading experience

### Phase 7 Checkpoint

* [ ] Implement page pagination
* [ ] Implement infinite queries
* [ ] Connect cursor pagination
* [ ] Prefetch data
* [ ] Handle loading transitions

---

# Phase 8: Optimistic UI

**Days 15–16**

**Goal:** Make application interactions feel instant while keeping server state correct.

### 8.1 Optimistic Updates — Core

* [ ] What is optimistic UI?
* [ ] Server-confirmed UI
* [ ] Optimistic UI
* [ ] Temporary state
* [ ] Failure rollback
* [ ] Build: Instant task completion
* [ ] Done when: UI updates before the server response

### 8.2 Mutation Lifecycle — Core

* [ ] Before mutation
* [ ] Mutation request
* [ ] Success
* [ ] Error
* [ ] Settled
* [ ] Build: Task update lifecycle
* [ ] Done when: Each mutation stage is handled intentionally

### 8.3 Cache Updates — Core

* [ ] Read cached data
* [ ] Modify cached data
* [ ] Cancel queries
* [ ] Update query cache
* [ ] Refetch after mutation
* [ ] Build: Optimistic task editing
* [ ] Done when: UI and server state synchronize correctly

### 8.4 Rollback — Core

* [ ] Snapshot previous state
* [ ] Apply optimistic change
* [ ] Handle server failure
* [ ] Restore previous state
* [ ] Show error feedback
* [ ] Build: Failed task update rollback
* [ ] Done when: Failed mutations never leave incorrect UI state

### 8.5 Optimistic Create — Next

* [ ] Temporary IDs
* [ ] Temporary records
* [ ] Replace temporary record
* [ ] Server-generated IDs
* [ ] Error removal
* [ ] Build: Instant task creation
* [ ] Done when: New records appear immediately and reconcile with the server

### 8.6 Optimistic Delete — Core

* [ ] Remove from cache
* [ ] Send delete request
* [ ] Restore on failure
* [ ] Confirmation UX
* [ ] Build: Instant task deletion
* [ ] Done when: Failed deletion restores the record correctly

### Phase 8 Checkpoint

* [ ] Implement optimistic update
* [ ] Snapshot previous cache
* [ ] Cancel conflicting queries
* [ ] Roll back on failure
* [ ] Refetch after mutation
* [ ] Handle temporary records

---

# Phase 9: Production Data Synchronization

**Days 17–18**

**Goal:** Handle real-world caching, synchronization, filtering, and stale data.

### 9.1 Query Invalidation Strategy — Core

* [ ] Targeted invalidation
* [ ] Parent/child query keys
* [ ] Avoid unnecessary invalidation
* [ ] Mutation-driven invalidation
* [ ] Build: TaskFlow invalidation architecture
* [ ] Done when: Mutations refresh only the data that needs refreshing

### 9.2 Filtering & Sorting — Core

* [ ] Filter state
* [ ] Search state
* [ ] Sort state
* [ ] Query keys
* [ ] Backend filters
* [ ] Database indexes
* [ ] Build: Searchable task table
* [ ] Done when: Search/filter/sort works with URL + API + database

### 9.3 Debounced Search — Next

* [ ] Search input
* [ ] Debouncing
* [ ] Query keys
* [ ] Request cancellation
* [ ] Empty search
* [ ] Build: TaskFlow global search
* [ ] Done when: Search doesn't send unnecessary API requests

### 9.4 Retry & Error Handling — Core

* [ ] Retry behavior
* [ ] Network failures
* [ ] Server errors
* [ ] Authentication errors
* [ ] User feedback
* [ ] Build: Production error states
* [ ] Done when: Users receive useful feedback without uncontrolled retries

### 9.5 Offline / Reconnect Behavior — Bonus

* [ ] Network state
* [ ] Refetch on reconnect
* [ ] Stale data
* [ ] Offline UX
* [ ] Mutation retry concepts
* [ ] Build: Offline-aware TaskFlow
* [ ] Done when: You understand how server state behaves during network interruptions

### Phase 9 Checkpoint

* [ ] Design invalidation strategy
* [ ] Combine filters + pagination
* [ ] Implement search
* [ ] Handle retries
* [ ] Handle network failures

---

# Final Phase: Production Data Layer

**Goal:** Build a complete PostgreSQL + API + TanStack Query workflow.

---

## Final Project: TaskFlow Data Architecture

### PostgreSQL

* [ ] Users
* [ ] Organizations
* [ ] Projects
* [ ] Tasks
* [ ] Comments
* [ ] Activity logs
* [ ] File metadata

### Database Engineering

* [ ] Foreign keys
* [ ] Constraints
* [ ] Transactions
* [ ] Indexes
* [ ] Composite indexes
* [ ] Soft deletes
* [ ] Audit data

### API

* [ ] REST endpoints
* [ ] Filtering
* [ ] Sorting
* [ ] Search
* [ ] Cursor pagination
* [ ] Consistent response format
* [ ] Error handling

### TanStack Query

* [ ] Query keys
* [ ] Query cache
* [ ] Mutations
* [ ] Pagination
* [ ] Infinite queries
* [ ] Prefetching
* [ ] Cache invalidation
* [ ] Optimistic updates
* [ ] Rollbacks

### Production UX

* [ ] Loading states
* [ ] Empty states
* [ ] Error states
* [ ] Skeletons
* [ ] Optimistic feedback
* [ ] Pagination controls
* [ ] Infinite scrolling
* [ ] Search
* [ ] Filtering
* [ ] Sorting

---

# Integration: ChatSpace

Use the same architecture for real-time messaging.

* [ ] PostgreSQL message storage
* [ ] Conversation relationships
* [ ] Cursor pagination
* [ ] Infinite message history
* [ ] TanStack Query cache
* [ ] Optimistic message sending
* [ ] Temporary message IDs
* [ ] Socket.io synchronization
* [ ] Duplicate message prevention
* [ ] Failed message rollback
* [ ] Read-status synchronization

---

# Integration: SupportDesk AI

Use PostgreSQL + TanStack Query for an AI support dashboard.

* [ ] Ticket list
* [ ] Cursor pagination
* [ ] Ticket filtering
* [ ] Ticket search
* [ ] Ticket status mutation
* [ ] Optimistic status updates
* [ ] Ticket assignment
* [ ] Agent dashboard
* [ ] AI-generated responses
* [ ] Activity timeline
* [ ] Query invalidation after AI actions

---

# Interview Preparation

## PostgreSQL

* [ ] What is an index?
* [ ] When should you create an index?
* [ ] What is a composite index?
* [ ] How does column order affect an index?
* [ ] What is EXPLAIN ANALYZE?
* [ ] Sequential scan vs index scan?
* [ ] What is a transaction?
* [ ] What is ACID?
* [ ] What are isolation levels?
* [ ] What is row-level locking?
* [ ] Offset vs cursor pagination?
* [ ] How would you optimize a slow query?
* [ ] How would you design a multi-tenant schema?

## TanStack Query

* [ ] What is server state?
* [ ] What is a query key?
* [ ] What is stale data?
* [ ] What is cache invalidation?
* [ ] `useQuery` vs `useMutation`
* [ ] How does query caching work?
* [ ] When should you use `useInfiniteQuery`?
* [ ] How do you implement cursor pagination?
* [ ] What is optimistic UI?
* [ ] How do you rollback an optimistic update?
* [ ] How do you prevent stale data?
* [ ] How should query keys be structured?
* [ ] How do you synchronize multiple related queries?

---

# Production Checklist

## PostgreSQL

* [ ] Correct data types
* [ ] Proper constraints
* [ ] Foreign keys
* [ ] Transactions
* [ ] Appropriate indexes
* [ ] Composite indexes
* [ ] Query analysis
* [ ] Cursor pagination
* [ ] Connection pooling
* [ ] Migration strategy
* [ ] Backup strategy
* [ ] Monitoring

## API

* [ ] Consistent response format
* [ ] Cursor pagination
* [ ] Filtering
* [ ] Sorting
* [ ] Search
* [ ] Validation
* [ ] Authorization
* [ ] Error handling
* [ ] Rate limiting

## TanStack Query

* [ ] Consistent query keys
* [ ] Proper cache configuration
* [ ] Targeted invalidation
* [ ] Pagination
* [ ] Infinite queries
* [ ] Prefetching
* [ ] Optimistic updates
* [ ] Rollbacks
* [ ] Error handling
* [ ] Loading states

## Frontend UX

* [ ] No unnecessary refetches
* [ ] No layout jumps
* [ ] Instant feedback
* [ ] Proper empty states
* [ ] Proper error states
* [ ] Pagination UX
* [ ] Search UX
* [ ] Filter UX
* [ ] Optimistic UI

---

# Completion Standard

You can mark this syllabus **COMPLETE** when you can independently build:

**React**
→ **TanStack Query**
→ **REST API**
→ **PostgreSQL**
→ **Indexed Queries**
→ **Cursor Pagination**
→ **Caching**
→ **Optimistic Mutations**
→ **Rollback**
→ **Database Transactions**

And you can explain **why** each part exists, when to use it, its tradeoffs, and how it behaves under real production workloads.

---

# Recommended Learning Order

1. [ ] Advanced PostgreSQL
2. [ ] Advanced SQL
3. [ ] Indexing
4. [ ] EXPLAIN / query optimization
5. [ ] Transactions
6. [ ] Cursor pagination
7. [ ] TanStack Query fundamentals
8. [ ] Query caching
9. [ ] Pagination with TanStack Query
10. [ ] Infinite queries
11. [ ] Optimistic UI
12. [ ] Rollbacks
13. [ ] Cache invalidation
14. [ ] Production data synchronization
15. [ ] Final TaskFlow implementation

---

# What Comes After This

After completing this syllabus, continue with:

* [ ] Redis + caching
* [ ] BullMQ + background jobs
* [ ] WebSockets / Socket.io
* [ ] File uploads + S3/R2
* [ ] Authentication + RBAC
* [ ] Stripe subscriptions
* [ ] Docker
* [ ] CI/CD
* [ ] System Design
* [ ] RAG + AI application architecture
