# Redis Syllabus

**Level:** Intermediate → Production
**Total time:** ~12–14 days
**Prerequisites:** Node.js, Express, REST APIs, PostgreSQL/MongoDB, WebSockets/Socket.io basics
**Focus:** Caching, Pub/Sub, Rate Limiting, Production Patterns
**Progress:** 0 / 32 topics done

---

## Skip for now

- [ ] Redis cluster internals
- [ ] Redis source-code internals
- [ ] Redis Streams deep dive
- [ ] RedisJSON / RedisSearch
- [ ] Redis Sentinel administration
- [ ] Multi-region Redis architecture
- [ ] Advanced Lua scripting
- [ ] Redis module development

---

# Phase 1: Redis Fundamentals

**Days 1–2**

**Goal:** Understand Redis as an in-memory data store and learn the core data structures.

**Done when:** You can install Redis, connect to it, and choose the correct Redis data type for a use case.

---

### 1.1 What is Redis? (Core)

- [ ] Redis use cases
- [ ] In-memory data storage
- [ ] Key-value model
- [ ] Redis vs PostgreSQL
- [ ] Redis vs MongoDB
- [ ] Redis as a primary database vs supporting service
- [ ] Build: Identify where Redis fits into **TaskFlow**
- [ ] Done when: you can explain why Redis should not automatically replace your database

---

### 1.2 Redis Setup (Core)

- [ ] Install Redis locally
- [ ] Run Redis with Docker
- [ ] Redis CLI
- [ ] Connect from Node.js
- [ ] Environment configuration
- [ ] Build: Add Redis to the backend of **TaskFlow**
- [ ] Done when: Node.js can set and retrieve a Redis value

---

### 1.3 Keys & Values (Core)

- [ ] `SET`
- [ ] `GET`
- [ ] `DEL`
- [ ] `EXISTS`
- [ ] `TTL`
- [ ] `EXPIRE`
- [ ] Key naming conventions
- [ ] Build: Create Redis keys for users and tasks
- [ ] Done when: you can create predictable, collision-free keys

---

### 1.4 Strings (Core)

- [ ] String values
- [ ] Numbers
- [ ] Increment/decrement
- [ ] `INCR`
- [ ] `DECR`
- [ ] `INCRBY`
- [ ] Build: Create a task-view counter in **TaskFlow**
- [ ] Done when: multiple requests can safely update the counter

---

### 1.5 Hashes (Core)

- [ ] Hash concept
- [ ] `HSET`
- [ ] `HGET`
- [ ] `HMGET`
- [ ] `HGETALL`
- [ ] `HDEL`
- [ ] Build: Store a lightweight user/session object
- [ ] Done when: you can read and update individual fields efficiently

---

### 1.6 Lists, Sets & Sorted Sets (Core)

- [ ] Lists
- [ ] Sets
- [ ] Sorted sets
- [ ] Common commands
- [ ] Choosing the correct structure
- [ ] Build:
  - List → recent activities
  - Set → online users
  - Sorted set → task leaderboard
- [ ] Done when: you can explain why each data structure was selected

---

### Phase 1 Checkpoint

- [ ] Explain Redis
- [ ] Use Redis CLI
- [ ] Create/read/delete keys
- [ ] Set expiration
- [ ] Use strings
- [ ] Use hashes
- [ ] Explain lists vs sets vs sorted sets
- [ ] Connect Redis with Node.js

---

# Phase 2: Redis with Node.js

**Days 3–4**

**Goal:** Integrate Redis cleanly into a Node.js/Express backend.

**Done when:** Redis operations are isolated behind reusable application services.

---

### 2.1 Redis Client in Node.js (Core)

- [ ] Redis Node.js client
- [ ] Connection lifecycle
- [ ] Async operations
- [ ] Error handling
- [ ] Graceful shutdown
- [ ] Build: Create `redisClient` infrastructure in **TaskFlow**
- [ ] Done when: application starts and shuts down without Redis connection leaks

---

### 2.2 Redis Configuration (Core)

- [ ] `REDIS_URL`
- [ ] Environment variables
- [ ] Local Redis
- [ ] Docker Redis
- [ ] Production Redis configuration
- [ ] Build: Create separate development/test/production Redis configuration
- [ ] Done when: credentials are never hardcoded

---

### 2.3 Redis Service Layer (Core)

- [ ] Keep Redis logic out of controllers
- [ ] Redis utility/service
- [ ] Reusable functions
- [ ] Error boundaries
- [ ] Serialization/deserialization
- [ ] Build: Create a reusable cache service
- [ ] Done when: controllers do not directly manage Redis commands

---

### 2.4 JSON Data in Redis (Core)

- [ ] JSON serialization
- [ ] `JSON.stringify()`
- [ ] `JSON.parse()`
- [ ] Cache object structures
- [ ] Cache invalidation considerations
- [ ] Build: Cache a TaskFlow project response
- [ ] Done when: cached data can be safely reconstructed

---

### 2.5 TTL & Expiration (Core)

- [ ] TTL concept
- [ ] Absolute vs relative expiration
- [ ] Session expiration
- [ ] Cache expiration
- [ ] Expiration strategies
- [ ] Build: Cache project statistics for a short period
- [ ] Done when: stale cached data automatically expires

---

# Phase 3: Redis Caching

**Days 5–7**

**Goal:** Use Redis to reduce database load and improve API response time.

**Done when:** You can design, implement, invalidate, and debug a production-style cache.

---

### 3.1 Why Caching? (Core)

- [ ] Database bottlenecks
- [ ] Repeated queries
- [ ] Latency
- [ ] Database load
- [ ] Cache hit
- [ ] Cache miss
- [ ] Build: Identify cacheable endpoints in **TaskFlow**
- [ ] Done when: you can explain which endpoints should and should not be cached

---

### 3.2 Cache-Aside Pattern (Core)

- [ ] Read from cache
- [ ] Cache miss
- [ ] Read database
- [ ] Store result
- [ ] Return response
- [ ] Build: Cache `GET /projects/:id`
- [ ] Done when: repeated requests avoid the database

---

### 3.3 Cache Keys (Core)

- [ ] Key naming
- [ ] Namespaces
- [ ] Resource IDs
- [ ] Query parameters
- [ ] Versioned keys
- [ ] Build: Design a cache-key convention for **TaskFlow**
- [ ] Done when: every cache key is predictable and documented

---

### 3.4 Cache Invalidation (Core)

- [ ] Why invalidation is difficult
- [ ] Delete cache after mutation
- [ ] Update cache
- [ ] TTL-based invalidation
- [ ] Related-cache invalidation
- [ ] Build: Invalidate project cache after task creation/update/deletion
- [ ] Done when: API does not return stale task data

---

### 3.5 Cache-Aside with CRUD (Core)

- [ ] GET → cache
- [ ] POST → invalidate
- [ ] PATCH → invalidate
- [ ] DELETE → invalidate
- [ ] Build: Apply caching to **TaskFlow** project/task APIs
- [ ] Done when: CRUD operations maintain cache consistency

---

### 3.6 Preventing Cache Problems (Next)

- [ ] Cache stampede
- [ ] Thundering herd
- [ ] Stale data
- [ ] Hot keys
- [ ] Cache penetration
- [ ] Basic mitigation strategies
- [ ] Build: Protect a frequently accessed **TaskFlow** endpoint
- [ ] Done when: you can explain how high traffic affects the cache

---

### 3.7 Cache Performance Testing (Core)

- [ ] Measure database-only requests
- [ ] Measure cached requests
- [ ] Cache hit ratio
- [ ] Response latency
- [ ] Redis memory usage
- [ ] Build: Compare cached vs uncached TaskFlow endpoints
- [ ] Done when: you can demonstrate the performance difference with measurements

---

### Phase 3 Checkpoint

- [ ] Explain cache-aside
- [ ] Implement caching
- [ ] Design cache keys
- [ ] Implement TTL
- [ ] Handle invalidation
- [ ] Explain cache stampede
- [ ] Measure cache performance

---

# Phase 4: Redis Pub/Sub

**Days 8–9**

**Goal:** Use Redis Pub/Sub for communication between application processes and real-time systems.

**Done when:** Multiple backend instances can exchange events through Redis.

---

### 4.1 Pub/Sub Fundamentals (Core)

- [ ] Publisher
- [ ] Subscriber
- [ ] Channel
- [ ] Publish
- [ ] Subscribe
- [ ] Message flow
- [ ] Build: Create a notification channel for **SupportDesk AI**
- [ ] Done when: one process publishes and another receives the event

---

### 4.2 Redis Publisher & Subscriber (Core)

- [ ] Publisher connection
- [ ] Subscriber connection
- [ ] Separate connection requirements
- [ ] Message handling
- [ ] Cleanup
- [ ] Build: Create publisher/subscriber services
- [ ] Done when: application processes can exchange events

---

### 4.3 Pub/Sub Event Design (Core)

- [ ] Event naming
- [ ] Event payloads
- [ ] Event versioning
- [ ] JSON messages
- [ ] Error handling
- [ ] Build: Define events such as:
  - `ticket.created`
  - `ticket.updated`
  - `ticket.assigned`
- [ ] Done when: events have consistent contracts

---

### 4.4 Redis Pub/Sub + Socket.io (Core)

- [ ] Why multiple Socket.io servers need coordination
- [ ] Redis as a message broker
- [ ] Cross-instance events
- [ ] Socket.io Redis adapter concept
- [ ] Build: Connect Redis Pub/Sub architecture with **ChatSpace**
- [ ] Done when: users connected to different server instances can receive the same real-time event

---

### 4.5 Pub/Sub Limitations (Next)

- [ ] Messages are not durable
- [ ] Offline subscribers
- [ ] Delivery guarantees
- [ ] Pub/Sub vs queue
- [ ] Pub/Sub vs Redis Streams
- [ ] When NOT to use Pub/Sub
- [ ] Build: Decide which **SupportDesk AI** events need Pub/Sub vs persistent storage
- [ ] Done when: you can explain the tradeoff

---

### Phase 4 Checkpoint

- [ ] Explain Pub/Sub
- [ ] Create publisher/subscriber
- [ ] Design event payloads
- [ ] Use Redis with Socket.io
- [ ] Explain Pub/Sub limitations
- [ ] Explain Pub/Sub vs queue

---

# Phase 5: Redis Rate Limiting

**Days 10–11**

**Goal:** Protect APIs and expensive operations from excessive requests.

**Done when:** Your API can enforce distributed rate limits across multiple backend instances.

---

### 5.1 Why Rate Limiting? (Core)

- [ ] Abuse prevention
- [ ] Brute-force protection
- [ ] API fairness
- [ ] Resource protection
- [ ] Cost protection
- [ ] Build: Identify rate-limit targets in **SupportDesk AI**
- [ ] Done when: you can identify which endpoints need stricter limits

---

### 5.2 Rate-Limit Concepts (Core)

- [ ] Request limits
- [ ] Time windows
- [ ] Client identity
- [ ] IP-based limiting
- [ ] User-based limiting
- [ ] API-key limiting
- [ ] Build: Design rate-limit rules for TaskFlow
- [ ] Done when: each rule has a clear key and time window

---

### 5.3 Fixed Window Algorithm (Core)

- [ ] Counter
- [ ] Window
- [ ] Increment
- [ ] Expiration
- [ ] Limit exceeded
- [ ] Build: Implement a basic Redis-backed API limiter
- [ ] Done when: requests beyond the limit are rejected

---

### 5.4 Sliding Window Concept (Next)

- [ ] Fixed window limitations
- [ ] Sliding window
- [ ] Burst traffic
- [ ] More accurate limiting
- [ ] Build: Improve the limiter for a sensitive endpoint
- [ ] Done when: you can explain the tradeoff between simplicity and accuracy

---

### 5.5 Rate Limiting Middleware (Core)

- [ ] Express middleware
- [ ] Redis counter
- [ ] HTTP `429`
- [ ] `Retry-After`
- [ ] Rate-limit headers
- [ ] Build: Protect AI ticket-generation endpoints in **SupportDesk AI**
- [ ] Done when: excessive requests receive a predictable `429` response

---

### 5.6 Distributed Rate Limiting (Core)

- [ ] Why in-memory counters fail with multiple servers
- [ ] Shared Redis state
- [ ] Multiple Node.js instances
- [ ] Atomic Redis operations
- [ ] Build: Run multiple API instances with one Redis rate limiter
- [ ] Done when: the limit remains consistent across instances

---

### Phase 5 Checkpoint

- [ ] Explain rate limiting
- [ ] Implement Redis counters
- [ ] Return `429`
- [ ] Understand fixed vs sliding windows
- [ ] Rate-limit by IP/user/API key
- [ ] Explain distributed rate limiting

---

# Phase 6: Production Redis

**Days 12–14**

**Goal:** Make Redis usage reliable, secure, observable, and production-ready.

**Done when:** You can safely operate Redis as part of a real backend architecture.

---

### 6.1 Redis Persistence (Next)

- [ ] Why Redis can persist data
- [ ] RDB
- [ ] AOF
- [ ] Persistence tradeoffs
- [ ] Cache vs persistent Redis data
- [ ] Build: Decide whether each Redis feature in your projects requires persistence
- [ ] Done when: you can justify the choice

---

### 6.2 Memory Management (Core)

- [ ] Redis memory usage
- [ ] TTL
- [ ] Eviction
- [ ] Memory limits
- [ ] Large values
- [ ] Key expiration
- [ ] Build: Review Redis memory usage in **TaskFlow**
- [ ] Done when: temporary data cannot grow without limits

---

### 6.3 Atomic Operations (Core)

- [ ] Why race conditions happen
- [ ] Atomic commands
- [ ] `INCR`
- [ ] Conditional operations
- [ ] Transactions concept
- [ ] Build: Make the rate limiter safe under concurrent requests
- [ ] Done when: simultaneous requests cannot bypass the limit because of a read-modify-write race

---

### 6.4 Redis Transactions (Next)

- [ ] `MULTI`
- [ ] `EXEC`
- [ ] Transaction concept
- [ ] When transactions help
- [ ] Limitations
- [ ] Build: Group related Redis operations
- [ ] Done when: you understand when a transaction is actually necessary

---

### 6.5 Redis Security (Core)

- [ ] Authentication
- [ ] Network isolation
- [ ] TLS
- [ ] Secrets
- [ ] Least privilege
- [ ] Avoid exposing Redis publicly
- [ ] Build: Secure Redis configuration for production
- [ ] Done when: Redis is accessible only by authorized application infrastructure

---

### 6.6 Redis Monitoring (Core)

- [ ] Memory usage
- [ ] Connected clients
- [ ] Commands
- [ ] Latency
- [ ] Cache hit/miss
- [ ] Rate-limit activity
- [ ] Build: Add Redis health information to your backend monitoring
- [ ] Done when: you can identify common Redis failures

---

### 6.7 Redis Failure Handling (Core)

- [ ] Redis unavailable
- [ ] Connection timeout
- [ ] Reconnection
- [ ] Fail-open vs fail-closed
- [ ] Cache failure behavior
- [ ] Rate limiter failure behavior
- [ ] Build: Decide failure behavior for **TaskFlow** and **SupportDesk AI**
- [ ] Done when: your application has an explicit Redis failure strategy

---

### 6.8 Redis Docker Setup (Core)

- [ ] Redis Docker image
- [ ] Volumes
- [ ] Environment variables
- [ ] Docker networking
- [ ] Health checks
- [ ] Development setup
- [ ] Build: Add Redis to your project's Docker environment
- [ ] Done when: backend + database + Redis start together

---

### Phase 6 Checkpoint

- [ ] Explain Redis persistence
- [ ] Manage Redis memory
- [ ] Understand atomic operations
- [ ] Use transactions when appropriate
- [ ] Secure Redis
- [ ] Monitor Redis
- [ ] Handle Redis failure
- [ ] Run Redis with Docker

---

# Final Phase: Prove It

## Mini Project: Production Redis Layer

Add Redis to **TaskFlow + ChatSpace + SupportDesk AI**.

### TaskFlow

- [ ] Cache project lists
- [ ] Cache project details
- [ ] Cache task statistics
- [ ] TTL-based expiration
- [ ] Cache invalidation
- [ ] Redis-backed rate limiting
- [ ] Cache hit/miss logging

### ChatSpace

- [ ] Redis Pub/Sub
- [ ] Multi-instance Socket.io architecture
- [ ] Online-user tracking
- [ ] Cross-instance events
- [ ] Redis adapter
- [ ] Connection failure handling

### SupportDesk AI

- [ ] API rate limiting
- [ ] User-based limits
- [ ] IP-based limits
- [ ] AI endpoint protection
- [ ] Redis-backed usage counters
- [ ] Pub/Sub for internal notifications
- [ ] `429` responses
- [ ] Retry information

---

# Interview Preparation

- [ ] What is Redis?
- [ ] Why is Redis fast?
- [ ] Redis vs PostgreSQL?
- [ ] Redis vs MongoDB?
- [ ] What are Redis data structures?
- [ ] What is TTL?
- [ ] What is cache-aside?
- [ ] How does cache invalidation work?
- [ ] What is a cache stampede?
- [ ] What is Redis Pub/Sub?
- [ ] What are Pub/Sub limitations?
- [ ] Redis Pub/Sub vs message queue?
- [ ] How does Redis help Socket.io scaling?
- [ ] How would you implement rate limiting with Redis?
- [ ] Fixed window vs sliding window?
- [ ] Why are atomic operations important?
- [ ] What happens if Redis goes down?
- [ ] How would you secure Redis?
- [ ] How would you monitor Redis?
- [ ] How would you design Redis for a production SaaS?

---

# Production Checklist

## Caching

- [ ] Cache only expensive/repeated data
- [ ] Clear cache-key naming
- [ ] Appropriate TTL
- [ ] Explicit invalidation strategy
- [ ] Cache hit/miss monitoring
- [ ] Protection against cache stampede
- [ ] Avoid unnecessarily large cached objects

## Pub/Sub

- [ ] Clear event names
- [ ] Structured event payloads
- [ ] Separate publisher/subscriber responsibilities
- [ ] Understand message delivery limitations
- [ ] Do not use Pub/Sub where durable delivery is required

## Rate Limiting

- [ ] IP/user/API-key strategy
- [ ] Appropriate limits
- [ ] Redis-backed shared state
- [ ] Atomic counters
- [ ] `429` responses
- [ ] `Retry-After`
- [ ] Different limits for expensive endpoints

## Security

- [ ] Redis not publicly exposed
- [ ] Authentication enabled
- [ ] TLS where required
- [ ] Secrets in environment variables
- [ ] Network restrictions
- [ ] Least-privilege access

## Reliability

- [ ] Connection retry strategy
- [ ] Redis health checks
- [ ] Timeout handling
- [ ] Application behavior when Redis is unavailable
- [ ] Graceful shutdown
- [ ] Memory limits
- [ ] TTL for temporary data

## Performance

- [ ] Avoid unnecessary Redis calls
- [ ] Avoid huge values
- [ ] Use appropriate data structures
- [ ] Monitor latency
- [ ] Monitor memory
- [ ] Monitor connection count
- [ ] Test under concurrent traffic

---

# What to Learn Next

1. **BullMQ**
   - Background jobs
   - Queues
   - Workers
   - Retries
   - Delayed jobs

2. **PostgreSQL + Prisma/Drizzle**
   - Transactions
   - Indexes
   - Relations
   - Query optimization

3. **System Design**
   - Caching architecture
   - Distributed systems
   - Scaling
   - Load balancing
   - Message queues

4. **Advanced Real-Time Systems**
   - Socket.io scaling
   - Redis adapter
   - Event-driven architecture

5. **Observability**
   - Structured logging
   - Metrics
   - Tracing
   - OpenTelemetry

6. **Redis Streams**
   - Durable event processing
   - Consumer groups
   - Event-driven architectures

---

# Weekly Review Log

| Week | Topics finished | What I forgot | Fix |
|------|-----------------|---------------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

---

# Completion Standard

You are **job-ready with Redis** when you can:

- [ ] Explain Redis and its appropriate use cases
- [ ] Choose Redis data structures correctly
- [ ] Integrate Redis with Node.js
- [ ] Implement cache-aside caching
- [ ] Design cache keys
- [ ] Handle cache invalidation
- [ ] Use TTL correctly
- [ ] Implement Redis Pub/Sub
- [ ] Integrate Redis with Socket.io
- [ ] Build distributed rate limiting
- [ ] Handle Redis failures
- [ ] Secure Redis
- [ ] Monitor Redis
- [ ] Run Redis with Docker
- [ ] Explain Redis architecture in an interview
- [ ] Build a production-ready Redis layer for a SaaS application
