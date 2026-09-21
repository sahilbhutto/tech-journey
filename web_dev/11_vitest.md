# Testing with Vitest Syllabus

**Topic:** Testing with Vitest
**Focus:** Unit Testing + Integration Testing + React Testing + API Testing
**Level:** Intermediate → Advanced
**Duration:** 10–14 Days
**Prerequisites:** JavaScript/TypeScript, React, Node.js, REST APIs, basic Git

**Projects:**

* TaskFlow — SaaS project
* ChatSpace — Real-time chat
* SupportDesk AI — AI ticketing system

**Goal:** Learn to write reliable, maintainable automated tests for frontend and backend applications using Vitest and the modern JavaScript testing ecosystem.

**Progress:** 0 / 36 topics completed

---

# Phase 1: Testing Fundamentals

**Days 1–2**

**Goal:** Understand what to test, why tests matter, and how professional test suites are structured.

### 1.1 Testing Fundamentals — Core

* [ ] What is software testing?
* [ ] Manual vs automated testing
* [ ] Unit tests
* [ ] Integration tests
* [ ] End-to-end tests
* [ ] Regression testing
* [ ] Test pyramid
* [ ] Build: Testing strategy for TaskFlow
* [ ] Done when: You can decide which type of test a feature needs

### 1.2 What Makes a Good Test — Core

* [ ] Arrange
* [ ] Act
* [ ] Assert
* [ ] Test isolation
* [ ] Deterministic tests
* [ ] Readable tests
* [ ] Single responsibility
* [ ] Build: Rewrite poorly structured tests
* [ ] Done when: Your tests clearly communicate expected behavior

### 1.3 Test Naming & Organization — Core

* [ ] Test file conventions
* [ ] `describe`
* [ ] `it`
* [ ] `test`
* [ ] Nested test groups
* [ ] Setup/teardown organization
* [ ] Build: Organize TaskFlow test suites
* [ ] Done when: Test files remain easy to navigate as the project grows

### 1.4 Testing Behavior vs Implementation — Core

* [ ] Test public behavior
* [ ] Avoid implementation details
* [ ] User-focused assertions
* [ ] Refactoring-safe tests
* [ ] Build: Refactor a component without breaking behavior tests
* [ ] Done when: Tests verify what the application does rather than how it is implemented

### Phase 1 Checkpoint

* [ ] Explain unit/integration/E2E testing
* [ ] Write Arrange → Act → Assert tests
* [ ] Organize test suites
* [ ] Identify bad tests
* [ ] Explain behavior-focused testing

---

# Phase 2: Vitest Setup & Core API

**Days 2–3**

**Goal:** Configure Vitest correctly and become comfortable with its core APIs.

### 2.1 Vitest Setup — Core

* [ ] Install Vitest
* [ ] Configure test scripts
* [ ] Test environment
* [ ] Test file discovery
* [ ] TypeScript integration
* [ ] Configuration file
* [ ] Build: Add Vitest to TaskFlow
* [ ] Done when: Tests run with a single command

### 2.2 Basic Assertions — Core

* [ ] `expect`
* [ ] Equality assertions
* [ ] Truthiness
* [ ] Null/undefined
* [ ] Arrays
* [ ] Objects
* [ ] Strings
* [ ] Numbers
* [ ] Build: Test TaskFlow utility functions
* [ ] Done when: You can write common assertions without looking them up

### 2.3 Test Lifecycle — Core

* [ ] `beforeEach`
* [ ] `afterEach`
* [ ] `beforeAll`
* [ ] `afterAll`
* [ ] Cleanup
* [ ] Shared setup
* [ ] Build: Test setup for application modules
* [ ] Done when: Test setup and cleanup are predictable

### 2.4 Test Filtering & Execution — Core

* [ ] Run all tests
* [ ] Run a single file
* [ ] Run a single test
* [ ] Watch mode
* [ ] Test filtering
* [ ] Verbose output
* [ ] Build: Developer testing workflow
* [ ] Done when: You can quickly run exactly the tests you're working on

### 2.5 Test Coverage — Core

* [ ] Coverage concept
* [ ] Line coverage
* [ ] Branch coverage
* [ ] Function coverage
* [ ] Statement coverage
* [ ] Coverage reports
* [ ] Build: Add coverage reporting
* [ ] Done when: You can interpret coverage instead of blindly chasing a percentage

### Phase 2 Checkpoint

* [ ] Configure Vitest
* [ ] Write assertions
* [ ] Use lifecycle hooks
* [ ] Run targeted tests
* [ ] Generate coverage

---

# Phase 3: Mocking & Spying

**Days 4–5**

**Goal:** Isolate code from external dependencies and control test behavior.

### 3.1 Mocking Fundamentals — Core

* [ ] Why mock?
* [ ] What should be mocked?
* [ ] What should not be mocked?
* [ ] Mock isolation
* [ ] Fake dependencies
* [ ] Build: Mock TaskFlow service dependencies
* [ ] Done when: You can isolate a unit without over-mocking it

### 3.2 Function Mocks — Core

* [ ] `vi.fn`
* [ ] Mock return values
* [ ] Mock implementations
* [ ] Mock arguments
* [ ] Call counts
* [ ] Call order
* [ ] Build: Test notification services
* [ ] Done when: You can verify how a dependency was called

### 3.3 Spies — Core

* [ ] `vi.spyOn`
* [ ] Observe existing functions
* [ ] Mock implementation
* [ ] Restore original implementation
* [ ] Build: Spy on application services
* [ ] Done when: You can observe behavior without completely replacing a module

### 3.4 Module Mocking — Core

* [ ] `vi.mock`
* [ ] Mock imported modules
* [ ] Mock API clients
* [ ] Mock database modules
* [ ] Mock external services
* [ ] Build: Mock payment/email dependencies
* [ ] Done when: External services don't run during isolated tests

### 3.5 Mock Reset & Cleanup — Core

* [ ] Clear mocks
* [ ] Reset mocks
* [ ] Restore mocks
* [ ] Test isolation
* [ ] Avoid shared mock state
* [ ] Build: Fix leaking mocks
* [ ] Done when: Tests pass independently and in any order

### Phase 3 Checkpoint

* [ ] Create function mocks
* [ ] Create spies
* [ ] Mock modules
* [ ] Verify calls
* [ ] Restore mocks
* [ ] Explain mocking tradeoffs

---

# Phase 4: Testing TypeScript & Business Logic

**Days 6–7**

**Goal:** Build high-value tests around real application logic.

### 4.1 Utility Functions — Core

* [ ] Pure functions
* [ ] Edge cases
* [ ] Invalid input
* [ ] Boundary values
* [ ] Build: TaskFlow utility test suite
* [ ] Done when: Core utilities have meaningful behavioral coverage

### 4.2 Business Logic — Core

* [ ] Service-layer testing
* [ ] Business rules
* [ ] Success paths
* [ ] Failure paths
* [ ] Validation
* [ ] Authorization rules
* [ ] Build: Task creation service
* [ ] Done when: Important business rules are protected by tests

### 4.3 Async Testing — Core

* [ ] Promises
* [ ] `async/await`
* [ ] Rejected promises
* [ ] Async assertions
* [ ] Timeouts
* [ ] Build: Async TaskFlow services
* [ ] Done when: Async success and failure cases are tested correctly

### 4.4 Error Testing — Core

* [ ] Expected errors
* [ ] Error messages
* [ ] Error types
* [ ] Validation errors
* [ ] Authorization errors
* [ ] Build: Service error tests
* [ ] Done when: Error behavior is explicitly verified

### 4.5 Parameterized Tests — Next

* [ ] Repeated test cases
* [ ] `test.each`
* [ ] Multiple input/output combinations
* [ ] Edge-case tables
* [ ] Build: Validation test matrix
* [ ] Done when: Repetitive test cases are concise and readable

### Phase 4 Checkpoint

* [ ] Test business logic
* [ ] Test async code
* [ ] Test failures
* [ ] Test edge cases
* [ ] Use parameterized tests

---

# Phase 5: React Testing

**Days 8–9**

**Goal:** Test React components based on user-visible behavior.

### 5.1 React Testing Library Fundamentals — Core

* [ ] Why React Testing Library?
* [ ] Render components
* [ ] Queries
* [ ] User behavior
* [ ] Accessibility-oriented queries
* [ ] Build: Test TaskFlow UI components
* [ ] Done when: Components can be tested from a user's perspective

### 5.2 DOM Queries — Core

* [ ] `getByRole`
* [ ] `getByLabelText`
* [ ] `getByText`
* [ ] `getByPlaceholderText`
* [ ] `queryBy...`
* [ ] `findBy...`
* [ ] Query priority
* [ ] Build: Test login/task forms
* [ ] Done when: You choose queries based on accessible user interaction

### 5.3 User Interactions — Core

* [ ] `userEvent`
* [ ] Click
* [ ] Typing
* [ ] Form submission
* [ ] Keyboard interactions
* [ ] Build: Task creation form
* [ ] Done when: Tests reproduce realistic user interactions

### 5.4 Component States — Core

* [ ] Loading
* [ ] Success
* [ ] Error
* [ ] Empty
* [ ] Disabled
* [ ] Validation
* [ ] Build: TaskFlow state-based UI tests
* [ ] Done when: Important UI states are covered

### 5.5 Forms — Core

* [ ] Input validation
* [ ] Required fields
* [ ] Invalid values
* [ ] Submission
* [ ] Error messages
* [ ] Successful submission
* [ ] Build: TaskFlow project form
* [ ] Done when: Form behavior is tested end-to-end within the component boundary

### Phase 5 Checkpoint

* [ ] Render React components
* [ ] Query accessible elements
* [ ] Simulate user interactions
* [ ] Test loading/error/empty states
* [ ] Test forms

---

# Phase 6: API & Integration Testing

**Days 10–11**

**Goal:** Test frontend/API interactions without depending on real external services.

### 6.1 API Mocking with MSW — Core

* [ ] Why API mocking?
* [ ] Mock Service Worker
* [ ] Request handlers
* [ ] Mock responses
* [ ] HTTP methods
* [ ] Request matching
* [ ] Build: Mock TaskFlow API
* [ ] Done when: Frontend tests can use realistic API responses

### 6.2 API Success Scenarios — Core

* [ ] GET requests
* [ ] POST requests
* [ ] PUT/PATCH requests
* [ ] DELETE requests
* [ ] Response data
* [ ] Build: TaskFlow CRUD integration tests
* [ ] Done when: UI behavior is tested against realistic API responses

### 6.3 API Error Scenarios — Core

* [ ] 400 errors
* [ ] 401 errors
* [ ] 403 errors
* [ ] 404 errors
* [ ] 409 errors
* [ ] 500 errors
* [ ] Network failures
* [ ] Build: Production API failure tests
* [ ] Done when: UI handles important backend failures correctly

### 6.4 TanStack Query Testing — Core

* [ ] Query client setup
* [ ] Query loading state
* [ ] Cached data
* [ ] Refetching
* [ ] Query errors
* [ ] Mutation testing
* [ ] Build: Test TaskFlow query hooks
* [ ] Done when: Server-state behavior is tested without real API calls

### 6.5 Integration Test Boundaries — Core

* [ ] Component + API
* [ ] Query + API
* [ ] Form + mutation
* [ ] Error handling
* [ ] Cache invalidation
* [ ] Build: TaskFlow task workflow
* [ ] Done when: Multiple application layers work together under test

### Phase 6 Checkpoint

* [ ] Mock API requests
* [ ] Test success responses
* [ ] Test API failures
* [ ] Test TanStack Query
* [ ] Write integration tests

---

# Phase 7: Backend Testing with Vitest

**Days 12–13**

**Goal:** Use Vitest to test Node.js/Express backend code.

### 7.1 Service Layer Testing — Core

* [ ] Business services
* [ ] Dependency mocking
* [ ] Success cases
* [ ] Failure cases
* [ ] Build: TaskFlow service tests
* [ ] Done when: Business logic can be tested without starting the server

### 7.2 Controller Testing — Core

* [ ] Request handling
* [ ] Response status
* [ ] Response body
* [ ] Error forwarding
* [ ] Mock services
* [ ] Build: TaskFlow controller tests
* [ ] Done when: Controllers correctly translate HTTP requests into service calls

### 7.3 Database Testing — Next

* [ ] Database test strategy
* [ ] Test database
* [ ] Seed data
* [ ] Cleanup
* [ ] Transactions
* [ ] Isolated database tests
* [ ] Build: PostgreSQL integration tests
* [ ] Done when: Important database behavior is tested against a real database environment

### 7.4 Express API Integration Tests — Core

* [ ] HTTP requests
* [ ] Routes
* [ ] Middleware
* [ ] Authentication
* [ ] Validation
* [ ] Error handling
* [ ] Build: TaskFlow API test suite
* [ ] Done when: Critical API endpoints are tested through the HTTP boundary

### 7.5 Authentication Testing — Core

* [ ] Login
* [ ] Registration
* [ ] Protected routes
* [ ] Invalid credentials
* [ ] Expired sessions/tokens
* [ ] Authorization
* [ ] Build: TaskFlow authentication tests
* [ ] Done when: Authentication failures are explicitly covered

### Phase 7 Checkpoint

* [ ] Test services
* [ ] Test controllers
* [ ] Test middleware
* [ ] Test API routes
* [ ] Test database interactions
* [ ] Test authentication

---

# Phase 8: Advanced Testing

**Day 14**

**Goal:** Make your test suite reliable enough for production CI/CD.

### 8.1 Fake Timers — Next

* [ ] Fake timers
* [ ] Time-dependent logic
* [ ] Delays
* [ ] Intervals
* [ ] Debounced functions
* [ ] Build: Test debounced search
* [ ] Done when: Time-dependent code can be tested deterministically

### 8.2 Testing Retries — Next

* [ ] Retry logic
* [ ] Failed requests
* [ ] Recovery
* [ ] Backoff concept
* [ ] Build: Test API retry behavior
* [ ] Done when: Retry behavior is deterministic and verifiable

### 8.3 Testing Race Conditions — Bonus

* [ ] Concurrent operations
* [ ] Request ordering
* [ ] Shared state
* [ ] Async race conditions
* [ ] Build: Test optimistic updates
* [ ] Done when: You understand how concurrency can create flaky tests

### 8.4 Snapshot Testing — Bonus

* [ ] Snapshot concept
* [ ] When snapshots help
* [ ] Snapshot maintenance
* [ ] Snapshot limitations
* [ ] Build: Evaluate snapshots on UI components
* [ ] Done when: You know when NOT to use snapshots

### 8.5 Test Flakiness — Core

* [ ] What makes tests flaky?
* [ ] Shared state
* [ ] Timing assumptions
* [ ] Randomness
* [ ] Network dependencies
* [ ] Poor cleanup
* [ ] Build: Find and fix flaky tests
* [ ] Done when: Tests produce consistent results

### Phase 8 Checkpoint

* [ ] Use fake timers
* [ ] Test retries
* [ ] Understand race conditions
* [ ] Evaluate snapshots
* [ ] Eliminate flaky tests

---

# Phase 9: CI/CD & Production Testing

**Days 15–16**

**Goal:** Make automated testing part of the development and deployment workflow.

### 9.1 Test Scripts — Core

* [ ] Development test command
* [ ] CI test command
* [ ] Coverage command
* [ ] Watch mode
* [ ] Build verification
* [ ] Build: Standardize TaskFlow test scripts
* [ ] Done when: Anyone can run the same test commands locally and in CI

### 9.2 GitHub Actions — Core

* [ ] Run tests on push
* [ ] Run tests on pull request
* [ ] Install dependencies
* [ ] Cache dependencies
* [ ] Type checking
* [ ] Test coverage
* [ ] Build verification
* [ ] Build: TaskFlow CI pipeline
* [ ] Done when: Broken tests prevent bad code from merging

### 9.3 Test Environment — Core

* [ ] Environment variables
* [ ] Test database
* [ ] Mock services
* [ ] Test secrets
* [ ] Separate environments
* [ ] Build: Dedicated test environment
* [ ] Done when: Tests never depend on production resources

### 9.4 Coverage Strategy — Core

* [ ] Critical-path coverage
* [ ] Business logic coverage
* [ ] API coverage
* [ ] UI coverage
* [ ] Coverage thresholds
* [ ] Avoid meaningless coverage
* [ ] Build: Define TaskFlow coverage strategy
* [ ] Done when: Coverage measures useful risk rather than becoming a vanity metric

### 9.5 Pre-Deployment Testing — Core

* [ ] Unit tests
* [ ] Integration tests
* [ ] Type checking
* [ ] Build
* [ ] Smoke tests
* [ ] Deployment gates
* [ ] Build: Production deployment pipeline
* [ ] Done when: Deployments are blocked when critical verification fails

### Phase 9 Checkpoint

* [ ] Run tests in GitHub Actions
* [ ] Configure test environments
* [ ] Configure coverage
* [ ] Add deployment gates
* [ ] Understand CI testing strategy

---

# Final Phase: Production Testing System

**Goal:** Build a professional test suite covering the most important parts of TaskFlow.

---

## Final Project: TaskFlow Testing Architecture

### Unit Tests

* [ ] Utility functions
* [ ] Business rules
* [ ] Validation
* [ ] Data transformations
* [ ] Permission logic

### React Tests

* [ ] Components
* [ ] Forms
* [ ] User interactions
* [ ] Loading states
* [ ] Empty states
* [ ] Error states

### Integration Tests

* [ ] React + API
* [ ] TanStack Query + API
* [ ] Forms + mutations
* [ ] Cache invalidation
* [ ] Backend services
* [ ] Database operations

### API Tests

* [ ] Authentication
* [ ] Authorization
* [ ] CRUD endpoints
* [ ] Validation
* [ ] Pagination
* [ ] Error handling

### CI/CD

* [ ] Tests on pull request
* [ ] Tests on push
* [ ] Type checking
* [ ] Coverage
* [ ] Production build
* [ ] Deployment gate

---

# ChatSpace Testing

### Real-Time Features

* [ ] Message sending
* [ ] Message rendering
* [ ] Conversation loading
* [ ] Pagination
* [ ] Optimistic messages
* [ ] Failed message rollback
* [ ] Socket event handling
* [ ] Reconnection behavior
* [ ] Duplicate message prevention

### Integration

* [ ] PostgreSQL
* [ ] API
* [ ] Socket.io
* [ ] TanStack Query
* [ ] Authentication

---

# SupportDesk AI Testing

### Ticket System

* [ ] Ticket creation
* [ ] Ticket assignment
* [ ] Ticket status changes
* [ ] Ticket comments
* [ ] File attachments
* [ ] Pagination
* [ ] Search
* [ ] Filtering

### AI Features

* [ ] Mock LLM responses
* [ ] Successful AI response
* [ ] AI API failure
* [ ] Timeout handling
* [ ] Invalid AI output
* [ ] Retry behavior
* [ ] Fallback behavior

### RAG Features

* [ ] Document ingestion
* [ ] Retrieval
* [ ] Empty retrieval results
* [ ] AI response generation
* [ ] Retrieval failure
* [ ] End-to-end workflow boundaries

---

# Interview Preparation

## Testing Fundamentals

* [ ] Unit vs integration vs E2E
* [ ] Test pyramid
* [ ] What makes a good test?
* [ ] Behavior vs implementation testing
* [ ] What should be mocked?
* [ ] What should not be mocked?

## Vitest

* [ ] `describe`
* [ ] `it`
* [ ] `test`
* [ ] `expect`
* [ ] `vi.fn`
* [ ] `vi.spyOn`
* [ ] `vi.mock`
* [ ] Lifecycle hooks
* [ ] Fake timers
* [ ] Coverage
* [ ] Test isolation

## React

* [ ] Why React Testing Library?
* [ ] `getByRole`
* [ ] `findBy`
* [ ] `queryBy`
* [ ] `userEvent`
* [ ] Testing forms
* [ ] Testing async UI
* [ ] Testing loading/error states

## API

* [ ] API mocking
* [ ] MSW
* [ ] Integration testing
* [ ] Authentication testing
* [ ] Database testing
* [ ] Error testing

## Production

* [ ] How do you prevent flaky tests?
* [ ] How do you decide what to test?
* [ ] How do you test third-party APIs?
* [ ] How do you test database interactions?
* [ ] How do you test optimistic UI?
* [ ] How do you structure tests in a large project?
* [ ] How do you integrate tests into CI/CD?

---

# Production Checklist

## Test Quality

* [ ] Tests are deterministic
* [ ] Tests are isolated
* [ ] Tests are readable
* [ ] Tests verify behavior
* [ ] Critical business logic is covered
* [ ] Important failure paths are covered

## Frontend

* [ ] Components tested
* [ ] Forms tested
* [ ] User interactions tested
* [ ] Loading states tested
* [ ] Error states tested
* [ ] TanStack Query tested
* [ ] Optimistic updates tested

## Backend

* [ ] Services tested
* [ ] Controllers tested
* [ ] Middleware tested
* [ ] APIs tested
* [ ] Authentication tested
* [ ] Authorization tested
* [ ] Database behavior tested

## CI/CD

* [ ] Tests run automatically
* [ ] Type checking runs automatically
* [ ] Coverage generated
* [ ] Production build verified
* [ ] Pull requests protected
* [ ] Test environment isolated

---

# Testing Strategy

Use different testing levels for different risks:

**Unit Test**
→ Pure logic
→ Utilities
→ Business rules

**Integration Test**
→ Components + API
→ Services + database
→ TanStack Query + API

**E2E Test**
→ Critical user journeys
→ Login
→ Checkout
→ Core workflows

Do not try to test everything at the same level.

---

# Completion Standard

You can mark this syllabus **COMPLETE** when you can independently:

* [ ] Set up Vitest in a TypeScript project
* [ ] Write unit tests
* [ ] Test async code
* [ ] Mock dependencies
* [ ] Spy on functions
* [ ] Mock modules
* [ ] Test React components
* [ ] Test forms and user interactions
* [ ] Mock APIs with MSW
* [ ] Test TanStack Query
* [ ] Test Express APIs
* [ ] Test backend services
* [ ] Test database interactions
* [ ] Test authentication
* [ ] Test optimistic UI
* [ ] Generate coverage
* [ ] Run tests in GitHub Actions
* [ ] Diagnose flaky tests

---

# Recommended Learning Order

1. [ ] Testing fundamentals
2. [ ] Vitest setup
3. [ ] Assertions
4. [ ] Mocking
5. [ ] Spies
6. [ ] Business-logic testing
7. [ ] React Testing Library
8. [ ] User interactions
9. [ ] MSW
10. [ ] API integration testing
11. [ ] TanStack Query testing
12. [ ] Backend testing
13. [ ] Database testing
14. [ ] Advanced async testing
15. [ ] CI/CD
16. [ ] Production test architecture

---

# What Comes After This

* [ ] Playwright — End-to-End Testing
* [ ] Advanced CI/CD
* [ ] Docker Testing
* [ ] PostgreSQL Test Environments
* [ ] Observability
* [ ] Performance Testing
* [ ] Security Testing
* [ ] System Design
