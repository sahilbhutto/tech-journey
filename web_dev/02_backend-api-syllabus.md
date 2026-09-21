# Backend API Development with Node.js

**Level:** Intermediate → Advanced
**Total time:** 30 days
**Prerequisites:** JavaScript, TypeScript, Git/GitHub. Basics of Backend
**Progress:** 0 / 35 topics done

---

# Phase 1: REST API Foundations

**Days:** 1–5
**Goal:** Build clean and predictable REST APIs using Node.js and Express.
**Done when:** I can design and implement a REST API without copying a tutorial.

---

## 1.1 REST Architecture

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Resources
  - HTTP methods
  - Request/response
  - Statelessness
  - REST conventions

- [ ] Build
  - Design the TaskFlow API resources:
    - Users
    - Projects
    - Tasks
    - Comments
  - Done when I can explain every endpoint and HTTP method.

**Docs:** https://developer.mozilla.org/en-US/docs/Web/HTTP

---

## 1.2 HTTP Methods

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
  - Idempotency

- [ ] Build
  - Implement TaskFlow task endpoints.
  - Done when each operation uses the appropriate HTTP method.

**Docs:** https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

---

## 1.3 HTTP Status Codes

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `200`
  - `201`
  - `204`
  - `400`
  - `401`
  - `403`
  - `404`
  - `409`
  - `422`
  - `429`
  - `500`

- [ ] Build
  - Standardize TaskFlow responses.
  - Done when every success and failure returns an appropriate status code.

**Docs:** https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

---

## 1.4 API URL Design

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Resource naming
  - Plural nouns
  - Nested resources
  - URL parameters
  - Query parameters

- [ ] Build
  - Design TaskFlow URLs such as:
    - `/api/v1/projects`
    - `/api/v1/projects/:projectId`
    - `/api/v1/projects/:projectId/tasks`
  - Done when the API has consistent URL conventions.

**Docs:** https://developer.mozilla.org/en-US/docs/Web/HTTP

---

## 1.5 Express Router

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Routers
  - Route parameters
  - Route organization
  - Controller separation

- [ ] Build
  - Organize TaskFlow into:
    - `routes`
    - `controllers`
    - `services`
  - Done when routes are separated from business logic.

**Docs:** https://expressjs.com/en/guide/routing.html

---

## 1.6 API Versioning

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - API versions
  - Backward compatibility
  - Breaking changes

- [ ] Build
  - Add `/api/v1` to TaskFlow.
  - Done when the API structure can support future versions.


**Docs:** Search official Express docs.

---

## Phase 1 Checkpoint

- [ ] Design TaskFlow REST API from memory.
- [ ] Define resources.
- [ ] Define endpoints.
- [ ] Select HTTP methods.
- [ ] Select status codes.
- [ ] Add `/api/v1`.
- [ ] Organize Express routes.
- [ ] No tutorial.
- [ ] No AI-generated code.

---

# Phase 2: Express Middleware & Request Pipeline

**Days:** 6–11
**Goal:** Understand how requests move through an Express application.
**Done when:** I can create reusable middleware and explain exactly where it runs.

---

## 2.1 Express Middleware

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Middleware function
  - `req`
  - `res`
  - `next`
  - Middleware order

- [ ] Build
  - Create a TaskFlow request logger.
  - Done when every request produces useful structured information.

**Docs:** https://expressjs.com/en/guide/using-middleware.html

---

## 2.2 Application vs Router Middleware

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `app.use()`
  - `router.use()`
  - Route-specific middleware
  - Middleware scope

- [ ] Build
  - Add project-specific middleware to TaskFlow.
  - Done when authentication middleware only runs where required.

**Docs:** https://expressjs.com/en/guide/using-middleware.html

---

## 2.3 Request Data

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `req.params`
  - `req.query`
  - `req.body`
  - `req.headers`

- [ ] Build
  - Build a TaskFlow task endpoint using:
    - Path parameters
    - Query parameters
    - Request body
    - Headers
  - Done when I can correctly identify where each piece of data belongs.

**Docs:** https://expressjs.com/en/api.html

---

## 2.4 Authentication Middleware

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Authentication middleware
  - Token/session extraction
  - `req.user`
  - Protected routes

- [ ] Build
  - Protect TaskFlow project routes.
  - Done when unauthenticated requests cannot access protected resources.

**Docs:** Search official Express authentication/security docs.

---

## 2.5 Authorization Middleware

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Authentication vs authorization
  - Roles
  - Permissions
  - Resource ownership

- [ ] Build
  - TaskFlow roles:
    - Owner
    - Admin
    - Member
  - Done when members cannot perform owner-only operations.

**Docs:** Search official Express security documentation.

---

## 2.6 Middleware Composition

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - Middleware chains
  - Reusable middleware
  - Route-level middleware
  - Global middleware

- [ ] Build
  - Create reusable TaskFlow middleware:
    - `authenticate`
    - `authorize`
    - `validate`
    - `rateLimit`
  - Done when routes can compose middleware cleanly.

**Docs:** https://expressjs.com/en/guide/using-middleware.html

---

## Phase 2 Checkpoint

- [ ] Build middleware pipeline.
- [ ] Logger middleware.
- [ ] Authentication middleware.
- [ ] Authorization middleware.
- [ ] Request parsing.
- [ ] Route-level middleware.
- [ ] Middleware composition.
- [ ] Explain middleware order from memory.

---

# Phase 3: Zod Validation & API Contracts

**Days:** 12–18
**Goal:** Make APIs type-safe, validated, and predictable.
**Done when:** No untrusted request data reaches business logic without validation.

---

## 3.1 Zod Fundamentals

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Schemas
  - Parsing
  - Validation
  - `safeParse`

- [ ] Build
  - Create TaskFlow task schema.
  - Done when invalid task data is rejected before business logic executes.

**Docs:** https://zod.dev/

---

## 3.2 Request Body Validation

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Object schemas
  - Required fields
  - Optional fields
  - Default values
  - Type coercion

- [ ] Build
  - Validate TaskFlow create/update task requests.
  - Done when malformed requests receive structured validation errors.

**Docs:** https://zod.dev/

---

## 3.3 Params & Query Validation

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Validate IDs
  - Validate pagination
  - Validate filters
  - Validate sorting

- [ ] Build
  - Validate TaskFlow:
    - `projectId`
    - `taskId`
    - `page`
    - `limit`
    - `status`
  - Done when invalid URL/query values never reach the service layer.

**Docs:** https://zod.dev/

---

## 3.4 Reusable Validation Middleware

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Schema-driven middleware
  - Validated request data
  - Validation error formatting

- [ ] Build
  - Create:
    - `validateBody`
    - `validateParams`
    - `validateQuery`
  - Done when any TaskFlow route can reuse the middleware.

**Docs:** Search official Zod docs.

---

## 3.5 TypeScript + Zod

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `z.infer`
  - Runtime validation vs compile-time types
  - Single source of truth

- [ ] Build
  - Generate TaskFlow request types from Zod schemas.
  - Done when API validation and TypeScript types stay synchronized.

**Docs:** https://zod.dev/

---

## 3.6 API Contract Design

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Request contracts
  - Response contracts
  - Consistent JSON structure
  - Breaking changes

- [ ] Build
  - Standardize TaskFlow responses:
    - `success`
    - `data`
    - `message`
    - `errors`
  - Done when all endpoints follow the same contract.

**Docs:** Search official Zod and Express docs.

---

## Phase 3 Checkpoint

- [ ] Validate body.
- [ ] Validate params.
- [ ] Validate query.
- [ ] Create reusable validation middleware.
- [ ] Generate TypeScript types.
- [ ] Standardize API responses.
- [ ] Reject invalid input before business logic.

---

# Phase 4: Error Handling & API Reliability

**Days:** 19–24
**Goal:** Build APIs that fail predictably and are easy to debug.
**Done when:** Every expected failure has a consistent response and unexpected errors are safely handled.

---

## 4.1 Express Error Middleware

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Error middleware
  - Four arguments
  - `next(error)`
  - Centralized handling

- [ ] Build
  - Create TaskFlow global error middleware.
  - Done when controllers do not manually format every error response.

**Docs:** https://expressjs.com/en/guide/error-handling.html

---

## 4.2 Custom API Errors

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Custom error classes
  - Status codes
  - Error codes
  - Operational errors

- [ ] Build
  - Create errors such as:
    - `NotFoundError`
    - `UnauthorizedError`
    - `ForbiddenError`
    - `ConflictError`
  - Done when controllers can throw meaningful errors.

**Docs:** https://expressjs.com/en/guide/error-handling.html

---

## 4.3 Async Error Handling

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Async route handlers
  - Promise rejection
  - Error propagation

- [ ] Build
  - Convert TaskFlow controllers to clean async handlers.
  - Done when database/API failures reach centralized error handling.

**Docs:** https://expressjs.com/en/guide/error-handling.html

---

## 4.4 Error Response Design

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Public vs internal errors
  - Error codes
  - Validation errors
  - Production-safe messages

- [ ] Build
  - Design TaskFlow error format.
  - Done when clients receive useful errors without leaking stack traces or secrets.

**Docs:** https://expressjs.com/en/guide/error-handling.html

---

## 4.5 Logging

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Structured logs
  - Log levels
  - Request IDs
  - Error context

- [ ] Build
  - Add structured logging to TaskFlow.
  - Done when a failed request can be traced through logs.

**Docs:** Search official Node.js documentation for logging/runtime diagnostics.

---

## Phase 4 Checkpoint

- [ ] Global error middleware.
- [ ] Custom API errors.
- [ ] Async errors.
- [ ] Validation errors.
- [ ] Consistent error responses.
- [ ] Production-safe error messages.
- [ ] Structured logging.
- [ ] Request tracing.

---

# Phase 5: Pagination, Filtering & API Querying

**Days:** 25–30
**Goal:** Build scalable collection endpoints that work correctly with large datasets.
**Done when:** I can design pagination and filtering APIs without loading unnecessary data.

---

## 5.1 Offset Pagination

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `page`
  - `limit`
  - `skip`
  - `total`
  - `totalPages`

- [ ] Build
  - Add pagination to TaskFlow task listing.
  - Done when `/tasks?page=2&limit=20` works correctly.

**Docs:** Search official MongoDB or PostgreSQL pagination docs.

---

## 5.2 Cursor Pagination

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Cursor
  - Stable ordering
  - `nextCursor`
  - Large dataset pagination

- [ ] Build
  - Add cursor pagination to ChatSpace messages.
  - Done when older messages can load efficiently.

**Docs:** Search official PostgreSQL/MongoDB documentation.

---

## 5.3 Filtering

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Query filters
  - Multiple filters
  - Validation
  - Database query construction

- [ ] Build
  - Filter TaskFlow tasks by:
    - Status
    - Priority
    - Assignee
    - Project
  - Done when filters are validated and efficiently queried.

**Docs:** Search official database query documentation.

---

## 5.4 Sorting

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Sort fields
  - Ascending/descending
  - Safe sort allowlists

- [ ] Build
  - Add TaskFlow sorting:
    - `createdAt`
    - `priority`
    - `dueDate`
  - Done when clients cannot inject arbitrary database fields into sorting.

**Docs:** Search official database query documentation.

---

## 5.5 Search

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Search parameters
  - Partial matching
  - Full-text search
  - Search performance

- [ ] Build
  - Add TaskFlow task search.
  - Done when users can search tasks by title/description.

**Docs:** Search official PostgreSQL/MongoDB search documentation.

---

## 5.6 Query Builder Design

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - Parse query parameters
  - Build safe database queries
  - Prevent query injection
  - Reusable query utilities

- [ ] Build
  - Create TaskFlow query utilities for:
    - Filter
    - Search
    - Sort
    - Pagination
  - Done when multiple endpoints reuse the same query logic safely.

**Docs:** Search official database documentation.

---

## Phase 5 Checkpoint

- [ ] Offset pagination.
- [ ] Cursor pagination.
- [ ] Filtering.
- [ ] Sorting.
- [ ] Search.
- [ ] Safe query construction.
- [ ] Reusable query utilities.
- [ ] Explain when cursor pagination is preferable.

---

# Phase 6: Environment, Security & Production API

**Days:** 31–37
**Goal:** Turn the API into a secure and production-ready backend service.
**Done when:** I can deploy and operate the API safely.

---

## 6.1 Environment Configuration

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `.env`
  - Environment variables
  - Development
  - Test
  - Production

- [ ] Build
  - Configure TaskFlow:
    - Database URL
    - JWT/session secrets
    - API keys
    - Port
  - Done when secrets are never hardcoded.

**Docs:** Search official Node.js environment variables documentation.

---

## 6.2 Environment Validation

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Required variables
  - Startup validation
  - Type-safe configuration

- [ ] Build
  - Validate TaskFlow environment variables with Zod.
  - Done when the server refuses to start with invalid configuration.

**Docs:** https://zod.dev/

---

## 6.3 API Security Middleware

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Security headers
  - CORS
  - Request size limits
  - Secure cookies
  - Rate limiting

- [ ] Build
  - Harden TaskFlow API.
  - Done when common HTTP/API security controls are configured intentionally.

**Docs:** https://expressjs.com/en/advanced/best-practice-security.html

---

## 6.4 Rate Limiting

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Request limits
  - Per-IP limits
  - Per-user limits
  - Distributed rate limiting

- [ ] Build
  - Protect TaskFlow login and sensitive endpoints.
  - Done when abusive repeated requests are limited.

**Docs:** Search official Express security guidance and chosen rate-limit package docs.

---

## 6.5 CORS

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Same-origin policy
  - CORS headers
  - Allowed origins
  - Credentials

- [ ] Build
  - Configure TaskFlow frontend/backend communication.
  - Done when only approved frontend origins can access the API as intended.

**Docs:** https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

---

## 6.6 API Documentation

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - OpenAPI
  - Endpoint documentation
  - Request schemas
  - Response schemas

- [ ] Build
  - Document TaskFlow API using OpenAPI/Swagger.
  - Done when another developer can use the API without reading backend source code.

**Docs:** Search official OpenAPI documentation.

---

## 6.7 Production Deployment

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Production build
  - Process management
  - Environment variables
  - Health checks
  - Logs

- [ ] Build
  - Deploy TaskFlow API.
  - Done when the production API is reachable and monitored.

**Docs:** Search official Node.js and deployment platform documentation.

---

## Phase 6 Checkpoint

- [ ] Environment configuration.
- [ ] Environment validation.
- [ ] Security middleware.
- [ ] CORS.
- [ ] Rate limiting.
- [ ] API documentation.
- [ ] Health check.
- [ ] Production deployment.
- [ ] Production logs.

---

# Phase 7: Production Architecture & Testing

**Days:** 38–42
**Goal:** Design backend systems that remain maintainable as features and traffic grow.
**Done when:** I can structure, test, debug, and evolve a production API.

---

## 7.1 Service Layer Architecture

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Routes
  - Controllers
  - Services
  - Repositories
  - Business logic

- [ ] Build
  - Refactor TaskFlow:
    - Route
    - Controller
    - Service
    - Repository
  - Done when business logic is not mixed into route definitions.

**Docs:** Search official Express architecture guidance.

---

## 7.2 Testing REST APIs

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Unit tests
  - Integration tests
  - API tests
  - Test database

- [ ] Build
  - Test TaskFlow:
    - Authentication
    - CRUD
    - Validation
    - Authorization
  - Done when critical API behavior is automatically tested.


**Docs:** Search official Vitest/Jest and Supertest docs.

---

## 7.3 Health Checks

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Liveness
  - Readiness
  - Dependency checks

- [ ] Build
  - Add:
    - `/health`
    - `/ready`
  - Done when deployment infrastructure can determine whether the API is healthy.

**Docs:** Search official Node.js/deployment platform documentation.

---

## 7.4 API Performance

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Database indexes
  - Query performance
  - Response size
  - Compression
  - Caching

- [ ] Build
  - Optimize TaskFlow task listing.
  - Done when you can identify and fix an intentionally slow endpoint.

**Docs:** Search official PostgreSQL/MongoDB and Express documentation.

---

## 7.5 Redis & API Caching

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - Cache-aside pattern
  - TTL
  - Cache invalidation
  - Redis basics

- [ ] Build
  - Cache frequently requested TaskFlow data.
  - Done when repeated reads can use Redis without returning stale data indefinitely.

**Docs:** Search official Redis documentation.

---

## 7.6 Background Jobs

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - Queues
  - Workers
  - Retries
  - Delayed jobs
  - Job failure

- [ ] Build
  - Add TaskFlow email notifications using a background queue.
  - Done when email work does not block the API request.

**Docs:** Search official BullMQ documentation.

---

## 7.7 API Observability

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Logs
  - Metrics
  - Traces
  - Error monitoring
  - Request correlation

- [ ] Build
  - Add observability to TaskFlow.
  - Done when you can trace a slow or failed API request.

**Docs:** Search official OpenTelemetry documentation.

---

## Phase 7 Checkpoint

- [ ] Clean backend architecture.
- [ ] Unit tests.
- [ ] Integration tests.
- [ ] Health checks.
- [ ] Performance optimization.
- [ ] Redis caching.
- [ ] Background jobs.
- [ ] Observability.
- [ ] Production debugging.

---

# Final Phase: Prove It

## Mini-Project: TaskFlow Backend API

Build a production-style backend for **TaskFlow**.

### API Features

- [ ] Authentication
- [ ] Authorization
- [ ] Users
- [ ] Organizations
- [ ] Projects
- [ ] Tasks
- [ ] Comments
- [ ] Task assignments
- [ ] Roles
- [ ] Permissions

### REST API

- [ ] Resource-based URLs
- [ ] HTTP methods
- [ ] Correct status codes
- [ ] API versioning
- [ ] Query parameters
- [ ] Path parameters
- [ ] Consistent response format

### Express

- [ ] Routers
- [ ] Controllers
- [ ] Services
- [ ] Middleware
- [ ] Error middleware
- [ ] Authentication middleware
- [ ] Authorization middleware

### Zod

- [ ] Body validation
- [ ] Params validation
- [ ] Query validation
- [ ] Environment validation
- [ ] Reusable validation middleware
- [ ] Type inference

### Querying

- [ ] Pagination
- [ ] Cursor pagination
- [ ] Filtering
- [ ] Sorting
- [ ] Search
- [ ] Safe query construction

### Production

- [ ] CORS
- [ ] Rate limiting
- [ ] Security headers
- [ ] Request size limits
- [ ] Environment configuration
- [ ] Structured logging
- [ ] Health checks
- [ ] API documentation
- [ ] Redis caching
- [ ] Background jobs
- [ ] Monitoring

### Testing

- [ ] Unit tests
- [ ] Integration tests
- [ ] Authentication tests
- [ ] Authorization tests
- [ ] Validation tests
- [ ] Error tests
- [ ] Pagination tests
- [ ] API endpoint tests

---

# Interview Proof

- [ ] Explain REST in 5 minutes.
- [ ] Explain HTTP methods.
- [ ] Explain HTTP status codes.
- [ ] Explain Express middleware.
- [ ] Explain middleware execution order.
- [ ] Explain authentication vs authorization.
- [ ] Explain Zod runtime validation.
- [ ] Explain why TypeScript alone cannot validate API input.
- [ ] Explain offset vs cursor pagination.
- [ ] Explain centralized error handling.
- [ ] Explain controller vs service layer.
- [ ] Explain CORS.
- [ ] Explain rate limiting.
- [ ] Explain API versioning.
- [ ] Explain Redis caching.
- [ ] Explain background jobs.
- [ ] Explain API testing.
- [ ] Explain production API security.
- [ ] Explain API observability.
- [ ] Design a REST API for a SaaS application from scratch.

---

# Production Checklist

## API Design

- [ ] REST conventions
- [ ] Consistent URLs
- [ ] Correct HTTP methods
- [ ] Correct status codes
- [ ] API versioning
- [ ] Consistent response format

## Validation

- [ ] Body validation
- [ ] Query validation
- [ ] Params validation
- [ ] Environment validation
- [ ] Type-safe schemas

## Errors

- [ ] Centralized error handling
- [ ] Custom errors
- [ ] Validation errors
- [ ] Safe production messages
- [ ] Structured logs

## Security

- [ ] Authentication
- [ ] Authorization
- [ ] CORS
- [ ] Rate limiting
- [ ] Security headers
- [ ] Input validation
- [ ] Secret management
- [ ] Request size limits

## Performance

- [ ] Database indexes
- [ ] Efficient queries
- [ ] Pagination
- [ ] Cursor pagination
- [ ] Response optimization
- [ ] Redis caching

## Reliability

- [ ] Health checks
- [ ] Background jobs
- [ ] Retry strategy
- [ ] Error monitoring
- [ ] Logging
- [ ] Request IDs

## Testing

- [ ] Unit tests
- [ ] Integration tests
- [ ] API tests
- [ ] Authentication tests
- [ ] Authorization tests
- [ ] Validation tests
- [ ] E2E tests

## Deployment

- [ ] Production environment
- [ ] Environment variables
- [ ] Database configuration
- [ ] CI/CD
- [ ] Production logs
- [ ] Monitoring
- [ ] Rollback strategy
