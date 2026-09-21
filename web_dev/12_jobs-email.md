# Background Jobs + Email Syllabus

**Topic:** Background Jobs + Email
**Technologies:** BullMQ + Redis + Resend + Cron
**Level:** Intermediate → Advanced
**Duration:** 12–15 Days
**Prerequisites:** Node.js, Express, TypeScript, REST APIs, PostgreSQL/MongoDB, Redis basics

**Projects:**

* TaskFlow — SaaS project
* ChatSpace — Real-time chat
* SupportDesk AI — AI ticketing system

**Goal:** Build reliable background-processing systems for emails, notifications, scheduled tasks, retries, delayed jobs, and production workflows.

**Progress:** 0 / 38 topics completed

---

# Phase 1: Background Job Fundamentals

**Days 1–2**

**Goal:** Understand why background jobs exist and when application work should leave the request-response cycle.

### 1.1 Synchronous vs Asynchronous Work — Core

* [ ] Request-response lifecycle
* [ ] Synchronous processing
* [ ] Asynchronous processing
* [ ] Blocking API requests
* [ ] Long-running operations
* [ ] Build: Move email sending outside TaskFlow API requests
* [ ] Done when: You can identify work that should not block an HTTP request

### 1.2 Background Jobs — Core

* [ ] What is a background job?
* [ ] Producer
* [ ] Queue
* [ ] Worker
* [ ] Job
* [ ] Consumer
* [ ] Build: First TaskFlow background job
* [ ] Done when: You can explain producer → queue → worker

### 1.3 Job Queue Architecture — Core

* [ ] Queue
* [ ] Producer
* [ ] Worker
* [ ] Redis
* [ ] Job state
* [ ] Failed jobs
* [ ] Completed jobs
* [ ] Build: Basic queue architecture
* [ ] Done when: You understand how a queue decouples API requests from processing

### 1.4 When to Use Background Jobs — Core

* [ ] Email sending
* [ ] Notifications
* [ ] Image processing
* [ ] File processing
* [ ] AI processing
* [ ] Reports
* [ ] Data synchronization
* [ ] Scheduled cleanup
* [ ] Build: Identify TaskFlow background workloads
* [ ] Done when: You can choose between synchronous and asynchronous processing

### Phase 1 Checkpoint

* [ ] Explain background jobs
* [ ] Explain queues
* [ ] Explain workers
* [ ] Identify background workloads
* [ ] Explain why Redis is useful for queues

---

# Phase 2: BullMQ Fundamentals

**Days 3–4**

**Goal:** Learn the core BullMQ architecture and APIs.

### 2.1 BullMQ Setup — Core

* [ ] Install BullMQ
* [ ] Redis connection
* [ ] Queue configuration
* [ ] Worker configuration
* [ ] Queue events
* [ ] Build: TaskFlow job queue
* [ ] Done when: BullMQ can enqueue and process a job

### 2.2 Producers & Jobs — Core

* [ ] Add jobs
* [ ] Job data
* [ ] Job IDs
* [ ] Job options
* [ ] Queue naming
* [ ] Build: Create notification jobs
* [ ] Done when: API can reliably enqueue background work

### 2.3 Workers — Core

* [ ] Worker processor
* [ ] Job data
* [ ] Job completion
* [ ] Worker errors
* [ ] Worker concurrency
* [ ] Build: Notification worker
* [ ] Done when: Workers process jobs independently from the API

### 2.4 Job Lifecycle — Core

* [ ] Waiting
* [ ] Active
* [ ] Completed
* [ ] Failed
* [ ] Delayed
* [ ] Retry state
* [ ] Build: Monitor TaskFlow jobs
* [ ] Done when: You understand the lifecycle of a BullMQ job

### 2.5 Job IDs & Idempotency — Core

* [ ] Unique job IDs
* [ ] Duplicate jobs
* [ ] Idempotent processing
* [ ] Safe retries
* [ ] Deduplication concepts
* [ ] Build: Prevent duplicate emails
* [ ] Done when: Retrying a job does not accidentally duplicate an important side effect

### Phase 2 Checkpoint

* [ ] Create queues
* [ ] Add jobs
* [ ] Build workers
* [ ] Handle job lifecycle
* [ ] Prevent duplicate processing

---

# Phase 3: Retries, Failures & Reliability

**Days 5–6**

**Goal:** Build background workers that survive failures.

### 3.1 Retry Strategies — Core

* [ ] Why jobs fail
* [ ] Retry attempts
* [ ] Fixed delay
* [ ] Exponential backoff
* [ ] Retry limits
* [ ] Build: Retry failed email delivery
* [ ] Done when: Temporary failures retry automatically

### 3.2 Failed Jobs — Core

* [ ] Failed job state
* [ ] Error information
* [ ] Failure logging
* [ ] Manual retry
* [ ] Failure monitoring
* [ ] Build: Failed notification handling
* [ ] Done when: Failed jobs can be inspected and retried safely

### 3.3 Idempotent Jobs — Core

* [ ] Idempotency keys
* [ ] Duplicate execution
* [ ] Database checks
* [ ] Transaction boundaries
* [ ] Safe side effects
* [ ] Build: Idempotent email worker
* [ ] Done when: The same job can run multiple times without corrupting application state

### 3.4 Job Timeouts — Next

* [ ] Long-running jobs
* [ ] Worker timeouts
* [ ] External API timeouts
* [ ] Cancellation concepts
* [ ] Build: AI processing timeout
* [ ] Done when: A stuck external dependency cannot hold a worker indefinitely

### 3.5 Dead-Letter Concepts — Next

* [ ] Permanently failed jobs
* [ ] Dead-letter queue concept
* [ ] Manual inspection
* [ ] Recovery workflow
* [ ] Build: SupportDesk AI failed-job workflow
* [ ] Done when: You have a strategy for jobs that repeatedly fail

### Phase 3 Checkpoint

* [ ] Configure retries
* [ ] Configure backoff
* [ ] Handle failures
* [ ] Design idempotent jobs
* [ ] Handle permanently failed jobs

---

# Phase 4: Delayed & Scheduled Jobs

**Days 7–8**

**Goal:** Execute jobs at a specific time or repeatedly.

### 4.1 Delayed Jobs — Core

* [ ] Delayed execution
* [ ] Delay configuration
* [ ] Job scheduling
* [ ] Delayed job lifecycle
* [ ] Build: Scheduled TaskFlow reminder
* [ ] Done when: A job executes after a defined delay

### 4.2 Cron Fundamentals — Core

* [ ] What is cron?
* [ ] Cron expressions
* [ ] Minutes
* [ ] Hours
* [ ] Days
* [ ] Months
* [ ] Weekdays
* [ ] Build: Daily cleanup job
* [ ] Done when: You can read and write common cron schedules

### 4.3 BullMQ Job Schedulers — Core

* [ ] Repeated jobs
* [ ] Scheduled jobs
* [ ] Recurring processing
* [ ] Scheduler architecture
* [ ] Build: Recurring TaskFlow digest
* [ ] Done when: Recurring work runs through the queue system

### 4.4 Cron vs Queue Scheduling — Core

* [ ] Traditional cron
* [ ] Queue-based scheduling
* [ ] Delayed jobs
* [ ] Recurring jobs
* [ ] Reliability tradeoffs
* [ ] Build: Choose scheduling strategy for TaskFlow
* [ ] Done when: You know when to use cron and when to use a queue scheduler

### 4.5 Time Zones — Core

* [ ] UTC
* [ ] Local time
* [ ] User time zones
* [ ] Scheduled notifications
* [ ] Daylight-saving considerations
* [ ] Build: User-specific reminder scheduling
* [ ] Done when: Scheduled jobs don't depend incorrectly on server local time

### Phase 4 Checkpoint

* [ ] Create delayed jobs
* [ ] Read cron expressions
* [ ] Schedule recurring jobs
* [ ] Understand cron vs queue scheduling
* [ ] Handle time zones

---

# Phase 5: Email Fundamentals with Resend

**Days 9–10**

**Goal:** Build production email delivery into your applications.

### 5.1 Transactional Email — Core

* [ ] What is transactional email?
* [ ] Verification emails
* [ ] Password reset emails
* [ ] Login alerts
* [ ] Notifications
* [ ] Receipts
* [ ] Build: TaskFlow transactional email system
* [ ] Done when: You can identify transactional email use cases

### 5.2 Resend Setup — Core

* [ ] Resend account
* [ ] API key
* [ ] Domain configuration
* [ ] Sender identity
* [ ] Environment variables
* [ ] Build: Resend email service
* [ ] Done when: Backend can send a test email securely

### 5.3 Email Service Layer — Core

* [ ] Email service
* [ ] Templates
* [ ] Sender configuration
* [ ] Recipient validation
* [ ] Error handling
* [ ] Logging
* [ ] Build: Reusable TaskFlow email service
* [ ] Done when: Application code does not directly call the email provider everywhere

### 5.4 Email Templates — Core

* [ ] HTML email
* [ ] Plain-text fallback
* [ ] Reusable layouts
* [ ] Dynamic variables
* [ ] Verification template
* [ ] Password-reset template
* [ ] Notification template
* [ ] Build: TaskFlow email templates
* [ ] Done when: Multiple emails share a consistent template structure

### 5.5 Email Security — Core

* [ ] Never expose API keys
* [ ] Environment variables
* [ ] Sender verification
* [ ] Tokenized links
* [ ] Expiring links
* [ ] Sensitive information
* [ ] Build: Secure password-reset email
* [ ] Done when: Sensitive actions use short-lived, protected links

### Phase 5 Checkpoint

* [ ] Configure Resend
* [ ] Send transactional email
* [ ] Create reusable email service
* [ ] Build HTML templates
* [ ] Secure email links

---

# Phase 6: BullMQ + Resend

**Days 11–12**

**Goal:** Build a reliable asynchronous email pipeline.

### 6.1 Email Queue Architecture — Core

* [ ] API creates email job
* [ ] Redis stores job
* [ ] Worker processes job
* [ ] Resend sends email
* [ ] Job completion
* [ ] Job failure
* [ ] Build: TaskFlow email queue
* [ ] Done when: HTTP requests never wait for email delivery

### 6.2 Email Job Payloads — Core

* [ ] Recipient
* [ ] Template
* [ ] Template variables
* [ ] Metadata
* [ ] Job ID
* [ ] Build: Generic email job structure
* [ ] Done when: One queue can support multiple email types

### 6.3 Email Retry Handling — Core

* [ ] Temporary provider failure
* [ ] Network failure
* [ ] Retry attempts
* [ ] Backoff
* [ ] Permanent failure
* [ ] Build: Resilient email worker
* [ ] Done when: Temporary failures are retried automatically

### 6.4 Email Idempotency — Core

* [ ] Duplicate job prevention
* [ ] Idempotency key
* [ ] Database tracking
* [ ] Safe retry
* [ ] Build: Prevent duplicate verification emails
* [ ] Done when: Worker retries don't accidentally send duplicate critical emails

### 6.5 Email Delivery Tracking — Next

* [ ] Queued
* [ ] Processing
* [ ] Sent
* [ ] Failed
* [ ] Provider response
* [ ] Delivery events/webhooks concept
* [ ] Build: Email delivery status
* [ ] Done when: Application can distinguish queued, sent, and failed emails

### Phase 6 Checkpoint

* [ ] Queue email jobs
* [ ] Process with workers
* [ ] Send through Resend
* [ ] Retry failures
* [ ] Prevent duplicates
* [ ] Track delivery state

---

# Phase 7: Production Background Job Architecture

**Days 13–14**

**Goal:** Build scalable background processing across multiple application features.

### 7.1 Multiple Queues — Core

* [ ] Email queue
* [ ] Notification queue
* [ ] File-processing queue
* [ ] AI-processing queue
* [ ] Cleanup queue
* [ ] Queue naming strategy
* [ ] Build: TaskFlow job architecture
* [ ] Done when: Different workloads can be isolated from each other

### 7.2 Worker Concurrency — Core

* [ ] Concurrency
* [ ] Worker capacity
* [ ] CPU-bound jobs
* [ ] I/O-bound jobs
* [ ] External API limits
* [ ] Build: Configure email worker concurrency
* [ ] Done when: Workers can process multiple jobs without overwhelming dependencies

### 7.3 Rate Limiting Workers — Next

* [ ] Provider limits
* [ ] Queue rate limiting
* [ ] Email sending limits
* [ ] API limits
* [ ] Backpressure
* [ ] Build: Resend-safe email processing
* [ ] Done when: Workers respect external service limits

### 7.4 Job Priorities — Next

* [ ] High-priority jobs
* [ ] Normal jobs
* [ ] Low-priority jobs
* [ ] User-facing vs maintenance jobs
* [ ] Build: Prioritized notification system
* [ ] Done when: Critical jobs can be processed ahead of lower-priority work

### 7.5 Graceful Shutdown — Core

* [ ] SIGTERM
* [ ] Stop accepting new work
* [ ] Finish active jobs
* [ ] Close Redis connections
* [ ] Worker shutdown
* [ ] Build: Production worker shutdown
* [ ] Done when: Deployment doesn't abruptly terminate active processing

### Phase 7 Checkpoint

* [ ] Design multiple queues
* [ ] Configure concurrency
* [ ] Handle provider limits
* [ ] Configure priorities
* [ ] Implement graceful shutdown

---

# Phase 8: Monitoring & Operations

**Day 15**

**Goal:** Know what your workers are doing and quickly diagnose failures.

### 8.1 Job Observability — Core

* [ ] Job counts
* [ ] Waiting jobs
* [ ] Active jobs
* [ ] Completed jobs
* [ ] Failed jobs
* [ ] Processing duration
* [ ] Build: Background-job metrics
* [ ] Done when: You can identify queue health problems

### 8.2 Logging — Core

* [ ] Structured logs
* [ ] Job ID
* [ ] User ID
* [ ] Queue name
* [ ] Error information
* [ ] Processing duration
* [ ] Build: Worker logging
* [ ] Done when: A failed job can be traced through logs

### 8.3 BullMQ Dashboard — Next

* [ ] Queue monitoring
* [ ] Job inspection
* [ ] Retry failed jobs
* [ ] Remove jobs
* [ ] Operational access
* [ ] Build: Queue administration
* [ ] Done when: Developers can inspect queues without directly querying Redis

### 8.4 Alerts — Core

* [ ] Failure-rate alerts
* [ ] Queue backlog
* [ ] Worker downtime
* [ ] Email provider failures
* [ ] Long-running jobs
* [ ] Build: Production alert strategy
* [ ] Done when: Important background failures don't remain unnoticed

---

# Final Phase: Production Background Job System

**Goal:** Build a complete background-processing platform for TaskFlow.

---

## Final Project: TaskFlow Job System

### Email Jobs

* [ ] Welcome email
* [ ] Email verification
* [ ] Password reset
* [ ] Task assignment notification
* [ ] Comment notification
* [ ] Daily digest
* [ ] Weekly summary

### Background Processing

* [ ] BullMQ
* [ ] Redis
* [ ] Workers
* [ ] Multiple queues
* [ ] Retry strategy
* [ ] Exponential backoff
* [ ] Delayed jobs
* [ ] Recurring jobs
* [ ] Job priorities
* [ ] Rate limiting
* [ ] Idempotency

### Scheduled Jobs

* [ ] Daily cleanup
* [ ] Daily digest
* [ ] Weekly reports
* [ ] Expired-token cleanup
* [ ] Orphan-file cleanup
* [ ] Subscription checks

### Email

* [ ] Resend
* [ ] Verified domain
* [ ] Email service
* [ ] HTML templates
* [ ] Plain-text fallback
* [ ] Secure links
* [ ] Delivery tracking

### Reliability

* [ ] Failed jobs
* [ ] Retries
* [ ] Backoff
* [ ] Dead-letter strategy
* [ ] Graceful shutdown
* [ ] Error logging
* [ ] Monitoring
* [ ] Alerts

---

# ChatSpace Integration

Build background processing for the real-time chat application.

* [ ] Offline notification emails
* [ ] Mention notifications
* [ ] Daily message digest
* [ ] File-processing jobs
* [ ] Image-processing jobs
* [ ] Cleanup jobs
* [ ] Failed notification retries
* [ ] Notification deduplication

---

# SupportDesk AI Integration

Use background jobs for AI-heavy and support workflows.

* [ ] AI ticket analysis
* [ ] AI response generation
* [ ] Document processing
* [ ] RAG ingestion
* [ ] Email notifications
* [ ] Ticket assignment notifications
* [ ] Daily agent reports
* [ ] SLA reminders
* [ ] Failed AI-job retries
* [ ] Long-running AI processing

---

# Interview Preparation

## Background Jobs

* [ ] What is a background job?
* [ ] Why use a queue?
* [ ] Producer vs consumer?
* [ ] Queue vs worker?
* [ ] When should work become asynchronous?
* [ ] What happens when a worker crashes?
* [ ] How do you retry jobs?
* [ ] What is exponential backoff?
* [ ] What is idempotency?
* [ ] How do you prevent duplicate jobs?
* [ ] How do you handle permanently failed jobs?

## BullMQ

* [ ] Queue
* [ ] Worker
* [ ] Job
* [ ] Job lifecycle
* [ ] Delayed jobs
* [ ] Recurring jobs
* [ ] Concurrency
* [ ] Job priorities
* [ ] Rate limiting
* [ ] Retries
* [ ] Backoff
* [ ] Graceful shutdown

## Email

* [ ] What is transactional email?
* [ ] Why use an email provider?
* [ ] Why queue emails?
* [ ] How do you prevent duplicate emails?
* [ ] How do you handle email provider failures?
* [ ] How do you secure password-reset links?
* [ ] How do you track email delivery?

## Architecture

* [ ] Design an email queue
* [ ] Design a notification system
* [ ] Design a scheduled-job system
* [ ] Design a retry system
* [ ] Design a multi-queue worker architecture
* [ ] Design a scalable background processing system

---

# Production Checklist

## Queue

* [ ] Redis configured
* [ ] BullMQ configured
* [ ] Producers separated from workers
* [ ] Multiple queues where appropriate
* [ ] Job IDs
* [ ] Job lifecycle handling

## Reliability

* [ ] Retries
* [ ] Exponential backoff
* [ ] Idempotency
* [ ] Duplicate prevention
* [ ] Failure handling
* [ ] Dead-letter strategy
* [ ] Graceful shutdown

## Scheduling

* [ ] Delayed jobs
* [ ] Recurring jobs
* [ ] Cron expressions
* [ ] Time-zone handling
* [ ] Cleanup jobs

## Email

* [ ] Resend configured
* [ ] Domain verified
* [ ] API key in environment variables
* [ ] Email templates
* [ ] Plain-text fallback
* [ ] Secure links
* [ ] Delivery tracking

## Operations

* [ ] Structured logging
* [ ] Queue metrics
* [ ] Failure monitoring
* [ ] Worker monitoring
* [ ] Alerts
* [ ] Queue dashboard

---

# Completion Standard

You can mark this syllabus **COMPLETE** when you can independently build:

**API Request**
→ **Create Job**
→ **Redis / BullMQ**
→ **Worker**
→ **Process Job**
→ **Resend / External Service**
→ **Retry on Failure**
→ **Backoff**
→ **Idempotent Processing**
→ **Track Status**
→ **Monitor**

And you can explain **why background jobs are needed, when to use queues, how retries work, how to prevent duplicate side effects, how scheduled jobs work, and how to operate workers safely in production.**

---

# Recommended Learning Order

1. [ ] Background-job fundamentals
2. [ ] BullMQ
3. [ ] Redis queues
4. [ ] Producers
5. [ ] Workers
6. [ ] Job lifecycle
7. [ ] Retries
8. [ ] Backoff
9. [ ] Idempotency
10. [ ] Delayed jobs
11. [ ] Cron / recurring jobs
12. [ ] Resend
13. [ ] Email service architecture
14. [ ] BullMQ + Resend
15. [ ] Multiple queues
16. [ ] Worker concurrency
17. [ ] Rate limiting
18. [ ] Monitoring
19. [ ] Graceful shutdown
20. [ ] Production TaskFlow implementation

---

# What Comes After This

* [ ] WebSockets / Socket.io
* [ ] Advanced Redis
* [ ] File uploads + S3/R2
* [ ] PostgreSQL + Drizzle/Prisma
* [ ] Authentication + RBAC
* [ ] Stripe subscriptions
* [ ] Docker
* [ ] CI/CD
* [ ] Observability
* [ ] System Design
* [ ] AI/RAG background processing
