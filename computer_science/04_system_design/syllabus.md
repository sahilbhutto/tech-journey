# System Design Sallybus


# Phase 1: System Design Fundamentals

- [ ] What is System Design?
- [ ] Why System Design Matters
- [ ] Functional Requirements
- [ ] Non-Functional Requirements
- [ ] Functional vs Non-Functional Requirements
- [ ] Constraints
- [ ] Assumptions
- [ ] System Boundaries
- [ ] Actors
- [ ] Use Cases
- [ ] Trade-Offs
- [ ] Scalability
- [ ] Availability
- [ ] Reliability
- [ ] Maintainability
- [ ] Performance
- [ ] Security
- [ ] Cost

---

# Phase 2: Requirements & Capacity Estimation

- [ ] Requirement Gathering
- [ ] Clarifying Ambiguous Requirements
- [ ] User Estimation
- [ ] Traffic Estimation
- [ ] Requests Per Second (RPS)
- [ ] Queries Per Second (QPS)
- [ ] Read vs Write Ratio
- [ ] Storage Estimation
- [ ] Bandwidth Estimation
- [ ] Memory Estimation
- [ ] Peak Traffic
- [ ] Growth Estimation
- [ ] Back-of-the-Envelope Calculations

---

# Phase 3: Core Building Blocks

- [ ] Client
- [ ] Server
- [ ] API
- [ ] Database
- [ ] Cache
- [ ] Load Balancer
- [ ] Reverse Proxy
- [ ] CDN
- [ ] Object Storage
- [ ] Message Queue
- [ ] Event Stream
- [ ] Search Engine
- [ ] DNS
- [ ] Service Discovery

---

# Phase 4: API & Service Design

- [ ] REST API Design
- [ ] RPC
- [ ] gRPC Basics
- [ ] API Versioning
- [ ] Pagination
- [ ] Filtering
- [ ] Sorting
- [ ] Idempotency
- [ ] Rate Limiting
- [ ] Authentication
- [ ] Authorization
- [ ] Input Validation
- [ ] Error Handling
- [ ] API Timeouts
- [ ] Retries
- [ ] Webhooks
- [ ] Service-to-Service Communication

---

# Phase 5: Database Architecture

- [ ] Database Selection
- [ ] SQL vs NoSQL
- [ ] Data Modeling
- [ ] Indexing
- [ ] Transactions
- [ ] ACID
- [ ] Isolation Levels
- [ ] Replication
- [ ] Read Replicas
- [ ] Database Partitioning
- [ ] Sharding
- [ ] Horizontal vs Vertical Scaling
- [ ] Database Failover
- [ ] Connection Pooling
- [ ] Database Caching
- [ ] Hot Partitions
- [ ] Data Consistency

---

# Phase 6: Caching

- [ ] Why Caching?
- [ ] Cache-Aside
- [ ] Read-Through Cache
- [ ] Write-Through Cache
- [ ] Write-Behind Cache
- [ ] Cache Invalidation
- [ ] TTL
- [ ] Cache Eviction
- [ ] LRU
- [ ] Cache Stampede
- [ ] Cache Penetration
- [ ] Cache Avalanche
- [ ] Distributed Caching
- [ ] Redis
- [ ] CDN Caching

---

# Phase 7: Scalability

- [ ] Vertical Scaling
- [ ] Horizontal Scaling
- [ ] Stateless Services
- [ ] Stateful Services
- [ ] Load Balancing
- [ ] Load Balancing Algorithms
- [ ] Auto Scaling
- [ ] Database Scaling
- [ ] Cache Scaling
- [ ] Read Scaling
- [ ] Write Scaling
- [ ] Sharding
- [ ] Partitioning
- [ ] Consistent Hashing
- [ ] Hotspot Handling

---

# Phase 8: Distributed Systems

- [ ] Distributed Systems Fundamentals
- [ ] Distributed vs Monolithic Systems
- [ ] Partial Failures
- [ ] Network Failures
- [ ] Network Partitions
- [ ] CAP Theorem
- [ ] Consistency
- [ ] Availability
- [ ] Partition Tolerance
- [ ] Strong Consistency
- [ ] Eventual Consistency
- [ ] Replication
- [ ] Leader-Follower
- [ ] Leaderless Systems
- [ ] Quorum
- [ ] Consensus Basics
- [ ] Distributed Locks
- [ ] Distributed Transactions
- [ ] Idempotency
- [ ] Exactly-Once vs At-Least-Once
- [ ] Ordering
- [ ] Clock & Time Problems

---

# Phase 9: Messaging & Event-Driven Architecture

- [ ] Message Queues
- [ ] Producers
- [ ] Consumers
- [ ] Topics
- [ ] Partitions
- [ ] Consumer Groups
- [ ] Pub/Sub
- [ ] Event-Driven Architecture
- [ ] Asynchronous Processing
- [ ] Retry Queues
- [ ] Dead Letter Queues
- [ ] Message Ordering
- [ ] Duplicate Messages
- [ ] Idempotent Consumers
- [ ] Backpressure
- [ ] Kafka Fundamentals
- [ ] RabbitMQ Fundamentals

---

# Phase 10: Microservices Architecture

- [ ] Monolith
- [ ] Modular Monolith
- [ ] Microservices
- [ ] Monolith vs Microservices
- [ ] Service Boundaries
- [ ] Domain-Driven Design Basics
- [ ] Service Communication
- [ ] API Gateway
- [ ] Service Discovery
- [ ] Configuration Management
- [ ] Distributed Transactions
- [ ] Saga Pattern
- [ ] Event-Driven Microservices
- [ ] Circuit Breaker
- [ ] Bulkhead Pattern
- [ ] Retry Pattern
- [ ] Microservice Observability
- [ ] Microservice Deployment

---

# Phase 11: Reliability & Fault Tolerance

- [ ] Reliability Fundamentals
- [ ] Failure Modes
- [ ] Single Point of Failure
- [ ] Redundancy
- [ ] Failover
- [ ] Health Checks
- [ ] Heartbeats
- [ ] Timeouts
- [ ] Retries
- [ ] Exponential Backoff
- [ ] Jitter
- [ ] Circuit Breakers
- [ ] Bulkheads
- [ ] Graceful Degradation
- [ ] Disaster Recovery
- [ ] Backup Strategy
- [ ] Recovery Point Objective (RPO)
- [ ] Recovery Time Objective (RTO)
- [ ] Multi-AZ Architecture
- [ ] Multi-Region Architecture

---

# Phase 12: Availability & Consistency

- [ ] Availability
- [ ] Reliability vs Availability
- [ ] SLA
- [ ] SLO
- [ ] SLI
- [ ] Error Budgets
- [ ] High Availability
- [ ] Active-Passive
- [ ] Active-Active
- [ ] Failover
- [ ] Data Replication
- [ ] Strong Consistency
- [ ] Eventual Consistency
- [ ] Read-After-Write Consistency
- [ ] Conflict Resolution

---

# Phase 13: Performance Engineering

- [ ] Latency
- [ ] Throughput
- [ ] Tail Latency
- [ ] p50
- [ ] p95
- [ ] p99
- [ ] Bottleneck Identification
- [ ] Caching
- [ ] Connection Pooling
- [ ] Batch Processing
- [ ] Async Processing
- [ ] Compression
- [ ] CDN
- [ ] Database Optimization
- [ ] Query Optimization
- [ ] Load Testing
- [ ] Stress Testing
- [ ] Capacity Planning

---

# Phase 14: Security Architecture

- [ ] Authentication
- [ ] Authorization
- [ ] Identity Management
- [ ] OAuth
- [ ] Access Control
- [ ] Encryption
- [ ] TLS
- [ ] Secrets Management
- [ ] API Security
- [ ] Rate Limiting
- [ ] DDoS Protection
- [ ] WAF
- [ ] Network Segmentation
- [ ] Least Privilege
- [ ] Zero Trust Basics
- [ ] Threat Modeling
- [ ] Secure Architecture

---

# Phase 15: Observability

- [ ] Logging
- [ ] Metrics
- [ ] Tracing
- [ ] Distributed Tracing
- [ ] Health Checks
- [ ] Monitoring
- [ ] Alerting
- [ ] Dashboards
- [ ] Correlation IDs
- [ ] Request IDs
- [ ] Error Tracking
- [ ] Performance Monitoring
- [ ] Incident Detection
- [ ] Production Debugging

---

# Phase 16: Cloud System Architecture

- [ ] Cloud Fundamentals
- [ ] Regions
- [ ] Availability Zones
- [ ] VPC
- [ ] Subnets
- [ ] Load Balancers
- [ ] Auto Scaling
- [ ] Object Storage
- [ ] Managed Databases
- [ ] Managed Caches
- [ ] Serverless
- [ ] Containers
- [ ] Kubernetes Basics
- [ ] CDN
- [ ] Cloud Networking
- [ ] IAM
- [ ] Infrastructure as Code Basics
- [ ] Cloud Cost Optimization

---

# Phase 17: Data & Storage Systems

- [ ] Object Storage
- [ ] Block Storage
- [ ] File Storage
- [ ] Blob Storage
- [ ] Data Replication
- [ ] Data Partitioning
- [ ] Data Lifecycle
- [ ] Archiving
- [ ] Backup
- [ ] Search Systems
- [ ] Elasticsearch/OpenSearch Basics
- [ ] Time-Series Data
- [ ] Data Warehousing Basics
- [ ] Event Streams

---

# Phase 18: AI System Design

- [ ] AI Application Architecture
- [ ] LLM API Architecture
- [ ] Model Gateway
- [ ] Prompt Management
- [ ] Embeddings
- [ ] Vector Databases
- [ ] RAG Architecture
- [ ] Retrieval Systems
- [ ] Semantic Search
- [ ] Tool Calling
- [ ] AI Agents
- [ ] Agent Architecture
- [ ] Model Routing
- [ ] AI Caching
- [ ] AI Rate Limiting
- [ ] AI Observability
- [ ] AI Evaluation
- [ ] AI Guardrails
- [ ] AI Security
- [ ] AI Cost Optimization
- [ ] AI Latency Optimization
- [ ] Multi-Model Architecture

---

# Phase 19: Real-World System Design

- [ ] URL Shortener
- [ ] Pastebin
- [ ] File Storage System
- [ ] Image Hosting System
- [ ] Notification System
- [ ] Email Delivery System
- [ ] Chat Application
- [ ] Real-Time Messaging System
- [ ] Social Media Feed
- [ ] News Feed
- [ ] Video Streaming Platform
- [ ] Search Engine
- [ ] Ride-Sharing System
- [ ] Food Delivery System
- [ ] E-Commerce Platform
- [ ] Payment System
- [ ] Ticket Booking System
- [ ] Distributed Rate Limiter
- [ ] Distributed Task Scheduler
- [ ] Logging Platform
- [ ] Analytics Platform
- [ ] AI Chatbot
- [ ] RAG Platform
- [ ] AI Agent Platform

---

# Phase 20: Architecture Patterns

- [ ] Layered Architecture
- [ ] Clean Architecture
- [ ] Hexagonal Architecture
- [ ] Event-Driven Architecture
- [ ] Microservices Architecture
- [ ] Modular Monolith
- [ ] CQRS
- [ ] Event Sourcing
- [ ] Saga Pattern
- [ ] API Gateway Pattern
- [ ] Backend-for-Frontend
- [ ] Pub/Sub Pattern
- [ ] Strangler Pattern
- [ ] Sidecar Pattern
- [ ] Circuit Breaker Pattern
- [ ] Bulkhead Pattern

---

# Phase 21: System Design Interview Engineering

- [ ] Clarify Requirements
- [ ] Define Scope
- [ ] Identify Constraints
- [ ] Estimate Scale
- [ ] Define APIs
- [ ] Design Data Model
- [ ] Draw High-Level Architecture
- [ ] Identify Bottlenecks
- [ ] Scale the System
- [ ] Handle Failures
- [ ] Discuss Security
- [ ] Discuss Observability
- [ ] Discuss Trade-Offs
- [ ] Explain Alternatives
- [ ] Defend Architecture Decisions

---

# Phase 22: Senior Engineer Thinking

- [ ] Think in Requirements
- [ ] Think in Constraints
- [ ] Think in Trade-Offs
- [ ] Think in Failure Modes
- [ ] Think in Bottlenecks
- [ ] Think in Cost
- [ ] Think in Security
- [ ] Think in Scalability
- [ ] Think in Reliability
- [ ] Think in Maintainability
- [ ] Think in Operational Complexity
- [ ] Avoid Premature Optimization
- [ ] Avoid Premature Microservices
- [ ] Choose Simple Architecture First
- [ ] Know When to Scale
- [ ] Know When NOT to Scale

---

# Phase 23: Practical System Design Projects

- [ ] Design a Production E-Commerce System
- [ ] Design a Real-Time Chat System
- [ ] Design a Notification Platform
- [ ] Design a File Storage Platform
- [ ] Design a Video Streaming Platform
- [ ] Design a Search Platform
- [ ] Design a Payment Platform
- [ ] Design a Social Media Platform
- [ ] Design a Ride-Sharing Platform
- [ ] Design an AI Chat Platform
- [ ] Design a RAG Platform
- [ ] Design an AI Agent Platform
- [ ] Document Architecture Decisions
- [ ] Identify Failure Scenarios
- [ ] Estimate Capacity
- [ ] Load Test the System
- [ ] Monitor the System
- [ ] Optimize the System

---

# ⭐ Highest-Priority Topics

If time is limited, prioritize:

- [ ] Requirements & Constraints
- [ ] Capacity Estimation
- [ ] API Design
- [ ] Database Architecture
- [ ] Caching
- [ ] Load Balancing
- [ ] Scalability
- [ ] Replication
- [ ] Partitioning & Sharding
- [ ] Distributed Systems
- [ ] Consistency
- [ ] Message Queues
- [ ] Event-Driven Architecture
- [ ] Reliability & Fault Tolerance
- [ ] Security
- [ ] Observability
- [ ] Performance
- [ ] Cloud Architecture
- [ ] System Design Trade-Offs
