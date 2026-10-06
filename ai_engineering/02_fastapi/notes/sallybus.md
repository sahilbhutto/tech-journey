#  FastAPI Sallybus

# Phase 1 — FastAPI Foundations

## 1.1 Understanding FastAPI

* [X] What is FastAPI?
* [X] FastAPI vs Flask vs Django
* [X] ASGI vs WSGI
* [X] Uvicorn
* [X] Starlette
* [X] Pydantic
* [X] FastAPI request/response lifecycle
* [X] Type hints in FastAPI

## 1.2 Project Setup

* [X] Python virtual environment
* [X] Install FastAPI
* [X] Install Uvicorn
* [X] Basic project structure
* [X] Run development server
* [X] `--reload`
* [X] Environment configuration basics

## 1.3 First API

* [X] Create `FastAPI()` application
* [X] First route
* [X] HTTP methods
* [X] Path operations
* [X] `/docs`
* [X] `/redoc`

---

# Phase 2 — Routing & Parameters

## 2.1 HTTP Methods

* [X] GET
* [X] POST
* [X] PUT
* [X] PATCH
* [X] DELETE

## 2.2 Path Parameters

* [X] Basic path parameters
* [X] Typed path parameters
* [X] Multiple path parameters
* [X] Validation
* [X] Enum path parameters

## 2.3 Query Parameters

* [X] Basic query parameters
* [X] Optional parameters
* [X] Default values
* [X] Typed query parameters
* [X] Required query parameters
* [X] Query validation
* [X] Pagination parameters
* [X] Filtering
* [X] Sorting
* [X] Searching

---

# Phase 3 — Request & Response Handling

## 3.1 Request Bodies

* [X] JSON request body
* [X] Pydantic models
* [X] Nested models
* [X] Optional fields
* [X] Default values
* [X] Field validation
* [X] Custom validation
* [X] Request body + path parameters
* [X] Request body + query parameters

## 3.2 Response Models

* [ ] `response_model`
* [ ] Response validation
* [ ] Nested response models
* [ ] Optional response fields
* [ ] Excluding fields
* [ ] Input model vs output model
* [ ] Preventing sensitive fields from being returned

## 3.3 Status Codes

* [ ] HTTP status codes
* [ ] `status_code`
* [ ] 200
* [ ] 201
* [ ] 204
* [ ] 400
* [ ] 401
* [ ] 403
* [ ] 404
* [ ] 409
* [ ] 422
* [ ] 500

---

# Phase 4 — Validation & Error Handling

## 4.1 Pydantic

* [ ] Pydantic models
* [ ] Pydantic field types
* [ ] `Field()`
* [ ] Constraints
* [ ] Nested models
* [ ] Lists and dictionaries
* [ ] Enums
* [ ] Custom validators
* [ ] Model validators
* [ ] Serialization
* [ ] Deserialization

## 4.2 Error Handling

* [ ] `HTTPException`
* [ ] Custom error responses
* [ ] Request validation errors
* [ ] Exception handlers
* [ ] Global exception handling
* [ ] Custom exception classes
* [ ] Consistent API error format

---

# Phase 5 — Dependency Injection

## 5.1 Dependencies

* [ ] What is Dependency Injection?
* [ ] `Depends()`
* [ ] Function dependencies
* [ ] Shared dependencies
* [ ] Nested dependencies
* [ ] Dependency parameters
* [ ] Dependency lifecycle
* [ ] Dependency overrides

## 5.2 Real-World Dependencies

* [ ] Database session dependency
* [ ] Authentication dependency
* [ ] Current-user dependency
* [ ] Permission dependency
* [ ] Configuration dependency
* [ ] Service dependencies

---

# Phase 6 — Routers & Professional Project Structure

## 6.1 APIRouter

* [ ] `APIRouter`
* [ ] Router prefixes
* [ ] Router tags
* [ ] Router dependencies
* [ ] Including routers
* [ ] Versioned API routers

## 6.2 Project Architecture

* [ ] `main.py`
* [ ] `routers/`
* [ ] `schemas/`
* [ ] `models/`
* [ ] `services/`
* [ ] `repositories/`
* [ ] `dependencies/`
* [ ] `core/`
* [ ] `config/`
* [ ] `utils/`

## 6.3 Application Design

* [ ] Separation of concerns
* [ ] Service layer
* [ ] Repository pattern
* [ ] Schema/model separation
* [ ] Configuration management
* [ ] API versioning
* [ ] Modular architecture

---

# Phase 7 — Database Integration

## 7.1 SQL Databases

* [ ] PostgreSQL
* [ ] Database connection
* [ ] SQLAlchemy
* [ ] SQLAlchemy 2.x
* [ ] Engine
* [ ] Sessions
* [ ] Models
* [ ] Relationships
* [ ] Transactions

## 7.2 CRUD

* [ ] Create
* [ ] Read
* [ ] Update
* [ ] Delete
* [ ] Filtering
* [ ] Pagination
* [ ] Sorting
* [ ] Searching

## 7.3 Database Migrations

* [ ] Alembic
* [ ] Migration files
* [ ] Create migration
* [ ] Apply migration
* [ ] Rollback migration
* [ ] Production migration workflow

---

# Phase 8 — Authentication & Authorization

## 8.1 Authentication

* [ ] Authentication vs authorization
* [ ] Password hashing
* [ ] OAuth2
* [ ] OAuth2 password flow
* [ ] Access tokens
* [ ] JWT
* [ ] Refresh tokens
* [ ] Token expiration
* [ ] Token revocation

## 8.2 Authorization

* [ ] Current user
* [ ] User roles
* [ ] RBAC
* [ ] Permissions
* [ ] Role-based dependencies
* [ ] Resource ownership
* [ ] Admin routes

## 8.3 Social Authentication

* [ ] Google OAuth
* [ ] OAuth callback
* [ ] Account linking
* [ ] Secure session handling

---

# Phase 9 — Async FastAPI

## 9.1 Async Fundamentals

* [ ] `async def`
* [ ] `await`
* [ ] Async I/O
* [ ] Event loop
* [ ] Coroutines
* [ ] `asyncio`

## 9.2 Async FastAPI

* [ ] Async route handlers
* [ ] Async database access
* [ ] Async HTTP requests
* [ ] `httpx`
* [ ] Async dependencies
* [ ] Async context managers

## 9.3 Concurrency

* [ ] `asyncio.gather()`
* [ ] Tasks
* [ ] Timeouts
* [ ] Cancellation
* [ ] Background concurrent operations
* [ ] Avoiding blocking code

---

# Phase 10 — Background Tasks & Job Processing

## 10.1 Background Tasks

* [ ] FastAPI `BackgroundTasks`
* [ ] When to use background tasks
* [ ] Limitations of background tasks
* [ ] Email/background processing

## 10.2 Production Job Queues

* [ ] Redis
* [ ] Celery
* [ ] BullMQ concepts
* [ ] Task queues
* [ ] Workers
* [ ] Retries
* [ ] Scheduled jobs
* [ ] Job monitoring

---

# Phase 11 — Middleware & Application Lifecycle

## 11.1 Middleware

* [ ] Middleware concept
* [ ] Custom middleware
* [ ] Request timing
* [ ] Request logging
* [ ] Authentication middleware
* [ ] CORS middleware
* [ ] Trusted host middleware

## 11.2 Lifespan

* [ ] Application startup
* [ ] Application shutdown
* [ ] Lifespan events
* [ ] Database initialization
* [ ] Resource cleanup
* [ ] Connection pools

---

# Phase 12 — Files & External Services

## 12.1 File Handling

* [ ] File uploads
* [ ] `UploadFile`
* [ ] Multiple uploads
* [ ] File validation
* [ ] File size limits
* [ ] Streaming responses
* [ ] File downloads

## 12.2 Object Storage

* [ ] Amazon S3
* [ ] Cloudflare R2
* [ ] Presigned URLs
* [ ] Secure uploads
* [ ] Secure downloads

## 12.3 External APIs

* [ ] HTTP clients
* [ ] `httpx`
* [ ] API authentication
* [ ] API timeouts
* [ ] Retries
* [ ] Error handling
* [ ] Rate limits

---

# Phase 13 — API Security

## 13.1 Security Fundamentals

* [ ] CORS
* [ ] CSRF concepts
* [ ] XSS
* [ ] SQL injection
* [ ] Authentication security
* [ ] Authorization security
* [ ] Input validation
* [ ] Secure headers

## 13.2 API Protection

* [ ] Rate limiting
* [ ] Request size limits
* [ ] Brute-force protection
* [ ] IP-based limits
* [ ] User-based limits
* [ ] API keys
* [ ] Secrets management

## 13.3 OWASP

* [ ] OWASP API Security Top 10
* [ ] Broken authentication
* [ ] Broken authorization
* [ ] Excessive data exposure
* [ ] Injection
* [ ] Security misconfiguration

---

# Phase 14 — Testing

## 14.1 Testing Fundamentals

* [ ] `pytest`
* [ ] Test structure
* [ ] Assertions
* [ ] Fixtures
* [ ] Test configuration
* [ ] Test isolation

## 14.2 FastAPI Testing

* [ ] `TestClient`
* [ ] Endpoint tests
* [ ] Request validation tests
* [ ] Response validation tests
* [ ] Authentication tests
* [ ] Error tests

## 14.3 Advanced Testing

* [ ] Dependency overrides
* [ ] Database testing
* [ ] Mocking
* [ ] External API mocking
* [ ] Async tests
* [ ] Integration tests

---

# Phase 15 — Performance & Scalability

* [ ] Async performance
* [ ] Database connection pooling
* [ ] Query optimization
* [ ] Response caching
* [ ] Redis caching
* [ ] Pagination
* [ ] Lazy loading
* [ ] N+1 query problem
* [ ] Rate limiting
* [ ] Load testing
* [ ] Profiling
* [ ] Worker processes
* [ ] Horizontal scaling

---

# Phase 16 — Observability & Production

## 16.1 Logging

* [ ] Python `logging`
* [ ] Structured logging
* [ ] Request IDs
* [ ] Error logging
* [ ] Log levels

## 16.2 Monitoring

* [ ] Health checks
* [ ] Readiness checks
* [ ] Metrics
* [ ] Prometheus concepts
* [ ] Sentry
* [ ] Application monitoring

## 16.3 Production Configuration

* [ ] Environment variables
* [ ] `.env`
* [ ] Pydantic Settings
* [ ] Secrets
* [ ] Development configuration
* [ ] Production configuration

---

# Phase 17 — Deployment

## 17.1 Server

* [ ] Uvicorn production mode
* [ ] Gunicorn concepts
* [ ] Multiple workers
* [ ] Reverse proxy
* [ ] Nginx

## 17.2 Docker

* [ ] Dockerfile
* [ ] Docker image
* [ ] Containers
* [ ] Environment variables
* [ ] Docker Compose
* [ ] PostgreSQL + FastAPI
* [ ] Redis + FastAPI

## 17.3 CI/CD

* [ ] GitHub Actions
* [ ] Automated tests
* [ ] Build pipeline
* [ ] Deployment pipeline
* [ ] Environment secrets
* [ ] Production deployment

---

# Phase 18 — AI/LLM APIs

## 18.1 AI API Fundamentals

* [ ] FastAPI + OpenAI
* [ ] FastAPI + Gemini
* [ ] FastAPI + Claude
* [ ] API key management
* [ ] Prompt handling
* [ ] Structured outputs

## 18.2 AI Streaming

* [ ] Streaming responses
* [ ] Server-Sent Events
* [ ] Token streaming
* [ ] Streaming AI responses
* [ ] Frontend streaming integration

## 18.3 AI API Architecture

* [ ] AI service layer
* [ ] Model abstraction
* [ ] Provider switching
* [ ] Retry handling
* [ ] Token usage tracking
* [ ] Cost tracking
* [ ] AI request logging

---

# Phase 19 — RAG Backend

* [ ] RAG architecture
* [ ] Document upload API
* [ ] Document parsing
* [ ] Chunking
* [ ] Embeddings
* [ ] Vector databases
* [ ] PostgreSQL + pgvector
* [ ] Similarity search
* [ ] Retrieval pipeline
* [ ] Context construction
* [ ] RAG API
* [ ] Streaming RAG responses
* [ ] RAG evaluation

---

# Phase 20 — Agent & Automation APIs

* [ ] Agent architecture
* [ ] Tool calling
* [ ] Function calling
* [ ] Agent state
* [ ] Agent memory
* [ ] Multi-step workflows
* [ ] Human-in-the-loop
* [ ] Background agents
* [ ] Agent job queues
* [ ] Long-running tasks
* [ ] Webhooks
* [ ] Automation APIs

---

# Phase 21 — MCP & Modern AI Backends

* [ ] MCP fundamentals
* [ ] MCP server concepts
* [ ] MCP tools
* [ ] MCP resources
* [ ] FastAPI + MCP
* [ ] Authentication for MCP
* [ ] Secure tool execution
* [ ] External service integration

---

# Phase 22 — Production AI Systems

* [ ] AI SaaS architecture
* [ ] Multi-user AI applications
* [ ] Multi-tenancy
* [ ] Usage limits
* [ ] AI quotas
* [ ] Billing integration
* [ ] Subscription management
* [ ] AI cost controls
* [ ] Rate limiting
* [ ] Prompt security
* [ ] AI abuse prevention
* [ ] Observability
* [ ] AI evaluation
* [ ] Model fallback
* [ ] Production reliability

---

# 🏗️ Portfolio Projects

## Project 1 — Production CRUD API

* [ ] FastAPI
* [ ] PostgreSQL
* [ ] SQLAlchemy
* [ ] Alembic
* [ ] Authentication
* [ ] RBAC
* [ ] Pagination
* [ ] Filtering
* [ ] Testing
* [ ] Docker
* [ ] Deployment

## Project 2 — Real-Time Backend

* [ ] FastAPI
* [ ] WebSockets
* [ ] Authentication
* [ ] PostgreSQL
* [ ] Redis
* [ ] Background jobs
* [ ] Notifications
* [ ] Docker
* [ ] Deployment

## Project 3 — AI RAG API

* [ ] FastAPI
* [ ] Document upload
* [ ] Embeddings
* [ ] pgvector
* [ ] RAG pipeline
* [ ] LLM integration
* [ ] Streaming
* [ ] Authentication
* [ ] Usage tracking
* [ ] Evaluation
* [ ] Deployment

## Project 4 — AI Agent Backend

* [ ] FastAPI
* [ ] Agent
* [ ] Tool calling
* [ ] Memory
* [ ] Background jobs
* [ ] Redis
* [ ] MCP
* [ ] Authentication
* [ ] Observability
* [ ] Production deployment
