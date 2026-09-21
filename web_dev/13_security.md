# Security + Monitoring Syllabus

**Stack:** OWASP • Rate Limiting • Sentry • Core Web Vitals
**Level:** Intermediate → Advanced
**Duration:** 12–14 Days
**Prerequisites:** React, Next.js, Node.js, Express, REST APIs, PostgreSQL/MongoDB, Redis, Authentication
**Projects:** TaskFlow • ChatSpace • SupportDesk AI
**Progress:** 0 / 36 topics completed

---

## What You Will Learn

* Web application security fundamentals
* OWASP Top 10
* Secure authentication and authorization
* Input validation and output encoding
* Rate limiting and abuse prevention
* Security headers and browser protections
* Secrets and environment security
* Sentry error tracking
* Backend and frontend monitoring
* Structured logging
* Performance monitoring
* Core Web Vitals
* Production security + observability workflow

---

# Phase 1: Web Security Fundamentals

**Days 1–2**
**Goal:** Understand how real web applications become vulnerable.

### 1.1 Security Mindset (Core)

* [ ] Threats vs vulnerabilities vs exploits
* [ ] Attack surface
* [ ] Trust boundaries
* [ ] Client vs server security
* [ ] Never trust client input
* [ ] Defense in depth
* [ ] Build: identify attack surfaces in TaskFlow
* [ ] Done when: you can explain where an attacker can interact with your application

### 1.2 OWASP Fundamentals (Core)

* [ ] What OWASP is
* [ ] OWASP Top 10
* [ ] Common web application vulnerabilities
* [ ] Security risk vs business impact
* [ ] Vulnerability prevention mindset
* [ ] Build: create an OWASP checklist for TaskFlow
* [ ] Done when: you can recognize the major OWASP vulnerability categories

### 1.3 Authentication Security (Core)

* [ ] Password hashing
* [ ] Strong password policies
* [ ] Session security
* [ ] JWT security
* [ ] Refresh-token security
* [ ] Cookie security
* [ ] Session expiration
* [ ] Account enumeration
* [ ] Build: harden TaskFlow authentication
* [ ] Done when: authentication cannot rely on client-side checks alone

### 1.4 Authorization & Access Control (Core)

* [ ] Authentication vs authorization
* [ ] RBAC
* [ ] Resource ownership
* [ ] IDOR / BOLA
* [ ] Privilege escalation
* [ ] Server-side authorization
* [ ] Build: secure TaskFlow project/team resources
* [ ] Done when: users cannot access another user's resources by changing an ID

### Phase 1 Checkpoint

* [ ] Explain authentication vs authorization
* [ ] Identify attack surfaces
* [ ] Explain OWASP Top 10 at a high level
* [ ] Find an authorization vulnerability in a sample API
* [ ] Secure one TaskFlow API endpoint

---

# Phase 2: OWASP Application Security

**Days 3–4**
**Goal:** Protect APIs and web applications against common attacks.

### 2.1 Injection Attacks (Core)

* [ ] SQL injection
* [ ] NoSQL injection
* [ ] Command injection
* [ ] ORM safety
* [ ] Parameterized queries
* [ ] Input validation
* [ ] Build: test TaskFlow API inputs
* [ ] Done when: user input cannot directly become executable database/OS commands

### 2.2 XSS (Core)

* [ ] Reflected XSS
* [ ] Stored XSS
* [ ] DOM-based XSS
* [ ] React escaping
* [ ] Dangerous HTML rendering
* [ ] Sanitization
* [ ] Content Security Policy basics
* [ ] Build: secure ChatSpace messages
* [ ] Done when: user-generated content cannot execute arbitrary browser JavaScript

### 2.3 CSRF & Cookies (Core)

* [ ] CSRF concept
* [ ] SameSite cookies
* [ ] HttpOnly
* [ ] Secure cookies
* [ ] Origin checks
* [ ] CSRF tokens
* [ ] When CSRF protection is required
* [ ] Build: harden authentication cookies
* [ ] Done when: you understand how browser credentials can be abused cross-site

### 2.4 Security Headers (Core)

* [ ] Content-Security-Policy
* [ ] X-Content-Type-Options
* [ ] Referrer-Policy
* [ ] Permissions-Policy
* [ ] HSTS
* [ ] Frame protection
* [ ] Build: security-header middleware
* [ ] Done when: production responses contain appropriate security headers

### 2.5 File & Upload Security (Next)

* [ ] File type validation
* [ ] MIME type validation
* [ ] File size limits
* [ ] Malicious file uploads
* [ ] Filename security
* [ ] Object-storage permissions
* [ ] Signed URLs
* [ ] Build: secure SupportDesk AI attachments
* [ ] Done when: users cannot upload arbitrary dangerous content

### Phase 2 Checkpoint

* [ ] Identify SQL/NoSQL injection risks
* [ ] Explain XSS prevention
* [ ] Explain CSRF
* [ ] Configure secure cookies
* [ ] Configure security headers
* [ ] Secure a file-upload endpoint

---

# Phase 3: Input Validation & API Security

**Days 5–6**
**Goal:** Make APIs resistant to malformed and abusive requests.

### 3.1 Request Validation (Core)

* [ ] Validate body
* [ ] Validate query parameters
* [ ] Validate route parameters
* [ ] Validate headers where required
* [ ] Zod schemas
* [ ] Type-safe validation
* [ ] Reject unexpected input
* [ ] Build: validation layer for TaskFlow APIs
* [ ] Done when: invalid requests never reach business logic

### 3.2 Output & Error Security (Core)

* [ ] Safe response objects
* [ ] Sensitive-field filtering
* [ ] Password/token leakage prevention
* [ ] Production error responses
* [ ] Error codes
* [ ] Internal vs public errors
* [ ] Build: secure Express error handler
* [ ] Done when: API errors never expose secrets or stack traces in production

### 3.3 CORS Security (Core)

* [ ] Same-origin policy
* [ ] CORS fundamentals
* [ ] Allowed origins
* [ ] Credentials
* [ ] Preflight requests
* [ ] Avoid wildcard configuration
* [ ] Build: production CORS configuration
* [ ] Done when: only intended frontend origins can access protected APIs

### 3.4 Secrets & Environment Security (Core)

* [ ] Environment variables
* [ ] API keys
* [ ] Database credentials
* [ ] Secret rotation
* [ ] `.env` security
* [ ] Git secret leaks
* [ ] Production secret management
* [ ] Build: audit TaskFlow configuration
* [ ] Done when: no secret is committed to Git

### Phase 3 Checkpoint

* [ ] Validate every API input
* [ ] Prevent sensitive fields from being returned
* [ ] Configure CORS correctly
* [ ] Audit environment variables
* [ ] Build a secure production error handler

---

# Phase 4: Rate Limiting & Abuse Prevention

**Days 7–8**
**Goal:** Prevent brute force, spam, scraping and API abuse.

### 4.1 Rate Limiting Fundamentals (Core)

* [ ] Why rate limiting exists
* [ ] Requests per second/minute
* [ ] Per-IP limits
* [ ] Per-user limits
* [ ] Endpoint-specific limits
* [ ] HTTP 429
* [ ] Retry-After
* [ ] Build: API rate limiter
* [ ] Done when: excessive requests are rejected predictably

### 4.2 Redis-Based Rate Limiting (Core)

* [ ] Redis counters
* [ ] Fixed-window limiting
* [ ] Sliding-window concept
* [ ] Token bucket concept
* [ ] Distributed rate limiting
* [ ] Expiration
* [ ] Build: Redis rate limiter
* [ ] Done when: multiple backend instances share rate-limit state

### 4.3 Authentication Rate Limits (Core)

* [ ] Login throttling
* [ ] Registration limits
* [ ] Password-reset limits
* [ ] OTP limits
* [ ] Email verification limits
* [ ] Prevent brute-force attacks
* [ ] Build: secure TaskFlow authentication endpoints
* [ ] Done when: authentication endpoints cannot be spammed indefinitely

### 4.4 API Abuse Protection (Next)

* [ ] Request body limits
* [ ] Pagination limits
* [ ] Query complexity
* [ ] Expensive endpoint protection
* [ ] Bot/automation abuse
* [ ] Resource quotas
* [ ] Build: protect expensive SupportDesk AI endpoints
* [ ] Done when: expensive operations have explicit limits

### Phase 4 Checkpoint

* [ ] Explain fixed vs sliding windows
* [ ] Implement Redis-based rate limiting
* [ ] Protect login
* [ ] Protect password reset
* [ ] Return correct 429 responses
* [ ] Protect expensive API operations

---

# Phase 5: Sentry Error Monitoring

**Days 9–10**
**Goal:** Detect and debug production failures.

### 5.1 Monitoring Fundamentals (Core)

* [ ] Logs vs metrics vs traces
* [ ] Error tracking
* [ ] Application monitoring
* [ ] Production observability
* [ ] Error aggregation
* [ ] Alerting
* [ ] Build: monitoring plan for TaskFlow
* [ ] Done when: you understand what should be monitored and why

### 5.2 Sentry Setup (Core)

* [ ] Create Sentry project
* [ ] Frontend integration
* [ ] Backend integration
* [ ] Environment configuration
* [ ] Development vs production
* [ ] Build: add Sentry to TaskFlow
* [ ] Done when: production errors appear in Sentry

### 5.3 Error Context (Core)

* [ ] User context
* [ ] Request context
* [ ] Tags
* [ ] Breadcrumbs
* [ ] Extra metadata
* [ ] Release/environment information
* [ ] Build: add useful context to TaskFlow errors
* [ ] Done when: an error contains enough context to reproduce/debug it

### 5.4 Performance Monitoring (Next)

* [ ] Slow requests
* [ ] Slow database operations
* [ ] Frontend transactions
* [ ] Performance traces
* [ ] Error + performance correlation
* [ ] Build: identify slow TaskFlow operations
* [ ] Done when: you can locate a performance bottleneck from monitoring data

### 5.5 Source Maps & Releases (Next)

* [ ] Production source maps
* [ ] Stack trace readability
* [ ] Release tracking
* [ ] Deployment tracking
* [ ] Build: connect TaskFlow deployments to releases
* [ ] Done when: production frontend errors point toward useful source locations

### Phase 5 Checkpoint

* [ ] Capture frontend errors
* [ ] Capture backend errors
* [ ] Add user/request context
* [ ] Track releases
* [ ] Investigate one real production-style error

---

# Phase 6: Structured Logging & Observability

**Days 11–12**
**Goal:** Build an observable backend instead of relying on `console.log()`.

### 6.1 Structured Logging (Core)

* [ ] Log levels
* [ ] JSON logs
* [ ] Request IDs
* [ ] Correlation IDs
* [ ] Timestamps
* [ ] Structured metadata
* [ ] Build: production logger for TaskFlow
* [ ] Done when: logs can be searched and correlated reliably

### 6.2 What to Log (Core)

* [ ] Authentication events
* [ ] Authorization failures
* [ ] API errors
* [ ] Payment events
* [ ] Background jobs
* [ ] External API failures
* [ ] Security events
* [ ] Build: security audit logs
* [ ] Done when: important production events are traceable

### 6.3 What NOT to Log (Core)

* [ ] Passwords
* [ ] Access tokens
* [ ] Refresh tokens
* [ ] API secrets
* [ ] Sensitive personal data
* [ ] Payment secrets
* [ ] Full authentication headers
* [ ] Build: audit existing TaskFlow logs
* [ ] Done when: sensitive data cannot accidentally appear in logs

### 6.4 Health Checks (Core)

* [ ] `/health`
* [ ] `/ready`
* [ ] Database health
* [ ] Redis health
* [ ] Dependency health
* [ ] Graceful degradation
* [ ] Build: production health endpoints
* [ ] Done when: deployment infrastructure can determine application health

### Phase 6 Checkpoint

* [ ] Implement structured logging
* [ ] Add request IDs
* [ ] Add health checks
* [ ] Audit sensitive logging
* [ ] Trace one request across multiple backend operations

---

# Phase 7: Core Web Vitals

**Days 13–14**
**Goal:** Measure and improve real-world frontend performance.

### 7.1 Web Performance Fundamentals (Core)

* [ ] Page-load lifecycle
* [ ] Browser rendering
* [ ] Critical rendering path
* [ ] JavaScript cost
* [ ] Network latency
* [ ] Caching
* [ ] Build: performance audit of TaskFlow
* [ ] Done when: you can explain why a page feels slow

### 7.2 Core Web Vitals (Core)

* [ ] LCP — Largest Contentful Paint
* [ ] INP — Interaction to Next Paint
* [ ] CLS — Cumulative Layout Shift
* [ ] Good / needs-improvement / poor thresholds
* [ ] Field data vs lab data
* [ ] Build: measure TaskFlow
* [ ] Done when: you can interpret Core Web Vitals data

### 7.3 LCP Optimization (Core)

* [ ] Optimize hero content
* [ ] Image optimization
* [ ] Font loading
* [ ] Critical resources
* [ ] Server response time
* [ ] Reduce render-blocking resources
* [ ] Build: optimize TaskFlow landing page
* [ ] Done when: you can identify the largest content bottleneck

### 7.4 INP Optimization (Core)

* [ ] Long JavaScript tasks
* [ ] Event handlers
* [ ] Main-thread blocking
* [ ] Code splitting
* [ ] Lazy loading
* [ ] Reduce unnecessary renders
* [ ] Build: optimize ChatSpace interactions
* [ ] Done when: expensive interactions are measurable and improved

### 7.5 CLS Optimization (Core)

* [ ] Image dimensions
* [ ] Dynamic content
* [ ] Font shifts
* [ ] Layout reservations
* [ ] Ads/embeds
* [ ] Skeleton loading
* [ ] Build: eliminate layout shifts in TaskFlow
* [ ] Done when: page layout remains stable during loading

### 7.6 Real User Monitoring (Next)

* [ ] Field performance data
* [ ] Device differences
* [ ] Network differences
* [ ] Geographic differences
* [ ] Performance segmentation
* [ ] Build: performance dashboard
* [ ] Done when: you can identify which users experience slow pages

### Phase 7 Checkpoint

* [ ] Explain LCP
* [ ] Explain INP
* [ ] Explain CLS
* [ ] Distinguish lab vs field data
* [ ] Measure a real application
* [ ] Fix one issue for each Core Web Vital

---

# Final Phase: Production Security & Monitoring System

**Goal:** Combine everything into one production-ready system.

## TaskFlow

* [ ] OWASP security audit
* [ ] Authentication hardening
* [ ] Authorization checks
* [ ] Zod validation
* [ ] Security headers
* [ ] CORS configuration
* [ ] Redis rate limiting
* [ ] Sentry frontend monitoring
* [ ] Sentry backend monitoring
* [ ] Structured logging
* [ ] Health checks
* [ ] Core Web Vitals monitoring

## ChatSpace

* [ ] Secure WebSocket authentication
* [ ] Message validation
* [ ] XSS protection
* [ ] Message spam protection
* [ ] Per-user rate limits
* [ ] Error tracking
* [ ] Connection monitoring
* [ ] Performance monitoring

## SupportDesk AI

* [ ] Secure ticket APIs
* [ ] File-upload security
* [ ] AI endpoint rate limits
* [ ] Request quotas
* [ ] Sensitive-data protection
* [ ] AI/API failure monitoring
* [ ] Background-job monitoring
* [ ] Sentry error tracking
* [ ] Performance monitoring

---

# Security Audit Checklist

## Authentication

* [ ] Passwords hashed securely
* [ ] Secure session/token handling
* [ ] Cookies configured securely
* [ ] Login rate limiting
* [ ] Password reset protection
* [ ] Session expiration

## Authorization

* [ ] Server-side authorization
* [ ] Resource ownership checks
* [ ] RBAC
* [ ] No IDOR/BOLA vulnerabilities
* [ ] Admin endpoints protected

## API

* [ ] Input validation
* [ ] Output filtering
* [ ] Error sanitization
* [ ] CORS configured
* [ ] Rate limiting
* [ ] Request-size limits
* [ ] Pagination limits

## Browser

* [ ] XSS protection
* [ ] CSRF protection where applicable
* [ ] Security headers
* [ ] Secure cookies
* [ ] Content Security Policy

## Secrets

* [ ] No secrets in Git
* [ ] Environment variables protected
* [ ] Production secrets separated
* [ ] Secret rotation strategy
* [ ] Sensitive logs removed

---

# Monitoring Checklist

* [ ] Error tracking
* [ ] Structured logs
* [ ] Request IDs
* [ ] Health checks
* [ ] Database monitoring
* [ ] Redis monitoring
* [ ] Background-job monitoring
* [ ] API latency monitoring
* [ ] Frontend performance monitoring
* [ ] Core Web Vitals
* [ ] Production alerts
* [ ] Deployment/release tracking

---

# Interview Preparation

### Security

* [ ] What is OWASP Top 10?
* [ ] What is SQL injection?
* [ ] What is XSS?
* [ ] What is CSRF?
* [ ] What is IDOR/BOLA?
* [ ] Authentication vs authorization?
* [ ] How do you secure JWTs?
* [ ] How do you secure cookies?
* [ ] What is CORS?
* [ ] Why are security headers important?

### Rate Limiting

* [ ] Why use rate limiting?
* [ ] How does Redis rate limiting work?
* [ ] Fixed window vs sliding window?
* [ ] How would you rate-limit login?
* [ ] What HTTP status represents rate limiting?
* [ ] How do distributed servers share rate-limit state?

### Monitoring

* [ ] Logs vs metrics vs traces?
* [ ] Why use Sentry?
* [ ] What information should an error contain?
* [ ] Why use request IDs?
* [ ] What should never be logged?
* [ ] How would you debug a production error?

### Performance

* [ ] What are Core Web Vitals?
* [ ] What is LCP?
* [ ] What is INP?
* [ ] What is CLS?
* [ ] Lab data vs field data?
* [ ] How do you improve LCP?
* [ ] How do you reduce JavaScript impact on INP?
* [ ] How do you prevent CLS?

---

# Production Completion Standard

You are finished when you can:

* [ ] Audit a full-stack application for common OWASP risks
* [ ] Secure authentication and authorization
* [ ] Validate every API boundary
* [ ] Implement Redis-based rate limiting
* [ ] Protect expensive endpoints
* [ ] Configure production security headers
* [ ] Secure file uploads
* [ ] Integrate Sentry into frontend and backend
* [ ] Create useful structured logs
* [ ] Implement health/readiness checks
* [ ] Monitor production errors
* [ ] Measure Core Web Vitals
* [ ] Diagnose frontend performance problems
* [ ] Build a complete security + observability checklist

---

# Recommended Learning Order

**OWASP → Authentication Security → API Security → Rate Limiting → Redis Rate Limiting → Sentry → Structured Logging → Health Checks → Core Web Vitals → Production Audit**

---

# After This Syllabus

Next recommended areas:

1. **System Design**
2. **Advanced Docker & Deployment**
3. **CI/CD & DevSecOps**
4. **OpenTelemetry**
5. **Distributed Systems**
6. **Advanced PostgreSQL**
7. **Cloud Architecture**
8. **AI Application Security**
9. **LLM Observability & AI Evaluation**
