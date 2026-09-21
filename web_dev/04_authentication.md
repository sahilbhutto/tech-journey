# Authentication (Sessions, JWT, Google OAuth, RBAC) Syllabus

**Level:** Intermediate → Production
**Total time:** 21 days
**Prerequisites:** TypeScript, React, Node.js, Express, HTTP, REST APIs, MongoDB basics
**Progress:** 0 / 30 topics done

---

## Skip for now

- [ ] Building your own authentication protocol
- [ ] Custom cryptography
- [ ] SAML
- [ ] LDAP / Active Directory
- [ ] Building an OAuth provider
- [ ] Passport.js internals
- [ ] WebAuthn / Passkeys internals
- [ ] Enterprise SSO internals
- [ ] Microservice authentication architecture

---

# Phase 1: Authentication Fundamentals

**Days:** 1–3
**Goal:** Understand how authentication works from browser to backend.
**Done when:** I can build a basic secure login flow without a tutorial.

### 1.1 Authentication vs Authorization

- [ ] **Authentication vs Authorization** (Core)
- [ ] Concept: Authentication verifies identity; authorization controls access.
- [ ] Build: TaskFlow — define users, roles, and protected resources.
- [ ] Done when: I can clearly explain authentication vs authorization.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official OWASP Authorization Cheat Sheet

### 1.2 HTTP Authentication Flow

- [ ] **HTTP Authentication Flow** (Core)
- [ ] Concept: Understand request → credentials → verification → authenticated request.
- [ ] Build: TaskFlow — trace register, login, logout, and protected requests.
- [ ] Done when: I can explain the complete request flow.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://developer.mozilla.org/en-US/docs/Web/HTTP

### 1.3 Password Hashing

- [ ] **Password Hashing** (Core)
- [ ] Concept: Understand hashing, salts, and secure password storage.
- [ ] Build: TaskFlow — hash passwords during registration and verify them during login.
- [ ] Done when: No plaintext passwords are stored in the database.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

### 1.4 Cookies

- [ ] **HTTP Cookies** (Core)
- [ ] Concept: Understand cookies, expiration, HttpOnly, Secure, and SameSite.
- [ ] Build: TaskFlow — store authentication information using a secure cookie.
- [ ] Done when: JavaScript cannot directly read the HttpOnly cookie.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies

### 1.5 CORS

- [ ] **CORS & Credentials** (Core)
- [ ] Concept: Understand origins, preflight, credentials, and CORS configuration.
- [ ] Build: TaskFlow — connect React frontend with Express authentication API.
- [ ] Done when: Cross-origin login and authenticated requests work correctly.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS

### 1.6 Authentication API

- [ ] **Authentication API Design** (Core)
- [ ] Concept: Design register, login, logout, and current-user endpoints.
- [ ] Build: TaskFlow — create:
  - `POST /auth/register`
  - `POST /auth/login`
  - `POST /auth/logout`
  - `GET /auth/me`
- [ ] Done when: React can use the complete authentication API.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Express.js docs

### Phase 1 Checkpoint

- [ ] **Rebuild Authentication Basics**
- [ ] Register
- [ ] Login
- [ ] Secure password storage
- [ ] Cookie
- [ ] Protected `/me`
- [ ] Logout
- [ ] No tutorial
- [ ] No AI-generated code

---

# Phase 2: Session-Based Authentication

**Days:** 4–6
**Goal:** Build server-side session authentication.
**Done when:** I can create, store, expire, and revoke sessions.

### 2.1 Sessions

- [ ] **Session Authentication** (Core)
- [ ] Concept: Understand session IDs and server-side session data.
- [ ] Build: TaskFlow — create a session after successful login.
- [ ] Done when: The browser only stores the session identifier.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official `express-session` docs

### 2.2 Session Storage

- [ ] **Session Storage** (Core)
- [ ] Concept: Understand memory storage vs persistent session stores.
- [ ] Build: TaskFlow — store sessions using Redis.
- [ ] Done when: Sessions survive application restarts.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Redis and `express-session` docs

### 2.3 Session Lifecycle

- [ ] **Session Lifecycle** (Core)
- [ ] Concept: Understand creation, expiration, regeneration, and destruction.
- [ ] Build: TaskFlow — regenerate session after login and destroy on logout.
- [ ] Done when: Logged-out sessions cannot be reused.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official `express-session` docs

### 2.4 Protected Routes

- [ ] **Session Authentication Middleware** (Core)
- [ ] Concept: Create middleware that identifies the logged-in user.
- [ ] Build: TaskFlow — protect task and project routes.
- [ ] Done when: Unauthenticated requests receive `401`.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Express.js docs

### 2.5 Session Security

- [ ] **Session Security** (Core)
- [ ] Concept: Understand session fixation, theft, expiration, and secure cookies.
- [ ] Build: TaskFlow — harden session configuration.
- [ ] Done when: Authentication passes a basic security review.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

### Phase 2 Checkpoint

- [ ] **Rebuild Session Authentication**
- [ ] Login
- [ ] Session creation
- [ ] Redis storage
- [ ] Protected routes
- [ ] Session regeneration
- [ ] Logout
- [ ] Session expiration
- [ ] No tutorial
- [ ] No AI-generated code

---

# Phase 3: JWT Authentication

**Days:** 7–10
**Goal:** Understand and implement JWT authentication correctly.
**Done when:** I can build JWT authentication and explain its tradeoffs.

### 3.1 JWT Structure

- [ ] **JWT Structure & Claims** (Core)
- [ ] Concept: Understand header, payload, signature, and claims.
- [ ] Build: ChatSpace — create and inspect an authentication JWT.
- [ ] Done when: I can explain the important JWT fields.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://www.jwt.io/introduction

### 3.2 JWT Signing

- [ ] **JWT Signing & Verification** (Core)
- [ ] Concept: Understand signing, verification, keys, and algorithms.
- [ ] Build: ChatSpace — sign and verify JWTs.
- [ ] Done when: Invalid signatures are rejected.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official `jose` documentation

### 3.3 Access Tokens

- [ ] **Access Tokens** (Core)
- [ ] Concept: Understand short-lived access tokens.
- [ ] Build: ChatSpace — implement protected API routes using access tokens.
- [ ] Done when: Expired tokens return `401`.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official JWT library docs

### 3.4 Refresh Tokens

- [ ] **Refresh Tokens** (Core)
- [ ] Concept: Understand token renewal, expiration, rotation, and revocation.
- [ ] Build: ChatSpace — implement `/auth/refresh`.
- [ ] Done when: Access tokens can be renewed securely.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://datatracker.ietf.org/doc/html/rfc9700

### 3.5 JWT Storage

- [ ] **JWT Storage & Browser Security** (Core)
- [ ] Concept: Compare cookies, localStorage, memory, XSS, and CSRF risks.
- [ ] Build: ChatSpace — choose and document your token-storage architecture.
- [ ] Done when: I can explain the security tradeoffs.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html

### 3.6 JWT Middleware

- [ ] **JWT Authentication Middleware** (Core)
- [ ] Concept: Extract, verify, and attach the authenticated user to the request.
- [ ] Build: ChatSpace — protect private API routes.
- [ ] Done when: Invalid or missing tokens cannot access protected resources.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Express.js docs

### 3.7 Sessions vs JWT

- [ ] **Sessions vs JWT** (Next)
- [ ] Concept: Compare server state, revocation, scalability, clients, and security.
- [ ] Build: ChatSpace — create an architecture decision document.
- [ ] Done when: I can explain when each approach makes sense.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official OWASP Authentication guidance

### Phase 3 Checkpoint

- [ ] **Rebuild JWT Authentication**
- [ ] Login
- [ ] Access token
- [ ] Refresh token
- [ ] Token expiration
- [ ] Refresh rotation
- [ ] Logout / revocation
- [ ] Protected routes
- [ ] No tutorial
- [ ] No AI-generated code

---

# Phase 4: Google OAuth

**Days:** 11–14
**Goal:** Integrate Google authentication using OAuth 2.0 / OpenID Connect.
**Done when:** I can explain and implement the Google authorization-code flow.

### 4.1 OAuth Fundamentals

- [ ] **OAuth 2.0 vs OpenID Connect** (Core)
- [ ] Concept: Understand delegated authorization vs user authentication.
- [ ] Build: TaskFlow — map the complete Google login flow.
- [ ] Done when: I can explain OAuth and OIDC separately.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://openid.net/developers/how-connect-works/

### 4.2 Google OAuth Setup

- [ ] **Google OAuth Client Setup** (Core)
- [ ] Concept: Understand client ID, client secret, redirect URI, and consent configuration.
- [ ] Build: TaskFlow — configure Google OAuth for development.
- [ ] Done when: Google redirects correctly to the backend callback.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://developers.google.com/identity/openid-connect/openid-connect
- Verify in official Google docs.

### 4.3 Authorization Code Flow

- [ ] **Authorization Code Flow** (Core)
- [ ] Concept: Understand redirect → authorization → callback → code exchange.
- [ ] Build: TaskFlow — implement Google login.
- [ ] Done when: A user can sign in using Google.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://developers.google.com/identity/protocols/oauth2
- Verify in official Google docs.

### 4.4 Google Identity Verification

- [ ] **Google Identity Verification** (Core)
- [ ] Concept: Verify identity information and important OIDC claims.
- [ ] Build: TaskFlow — verify Google identity before creating a local session.
- [ ] Done when: Forged client-side identity information is rejected.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://developers.google.com/identity/openid-connect/openid-connect
- Verify in official Google docs.

### 4.5 Account Linking

- [ ] **Local + Google Account Linking** (Core)
- [ ] Concept: Understand provider IDs, account linking, email conflicts, and takeover risks.
- [ ] Build: TaskFlow — link a Google account to an existing user account.
- [ ] Done when: One user can safely use multiple authentication methods.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://openid.net/specs/openid-connect-core-1_0.html

### 4.6 OAuth Error Handling

- [ ] **OAuth Security & Failure Handling** (Core)
- [ ] Concept: Handle invalid callbacks, denied consent, redirect errors, and failed code exchange.
- [ ] Build: TaskFlow — handle OAuth failures without creating a session.
- [ ] Done when: Failed OAuth flows never authenticate the user.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://datatracker.ietf.org/doc/html/rfc6749
- Verify in official Google docs.

### Phase 4 Checkpoint

- [ ] **Rebuild Google Authentication**
- [ ] Google OAuth setup
- [ ] Authorization code flow
- [ ] Callback endpoint
- [ ] Identity verification
- [ ] Account linking
- [ ] OAuth error handling
- [ ] No tutorial
- [ ] No AI-generated code

---

# Phase 5: RBAC & Authorization

**Days:** 15–17
**Goal:** Build scalable role and permission-based authorization.
**Done when:** I can protect resources using roles, permissions, and ownership rules.

### 5.1 RBAC Fundamentals

- [ ] **Role-Based Access Control** (Core)
- [ ] Concept: Understand users, roles, permissions, resources, and actions.
- [ ] Build: SupportDesk AI — define:
  - Customer
  - Agent
  - Manager
  - Admin
- [ ] Done when: Every role has documented permissions.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

### 5.2 Role Middleware

- [ ] **Role-Based Middleware** (Core)
- [ ] Concept: Build reusable middleware for role checks.
- [ ] Build: SupportDesk AI — protect ticket-management endpoints.
- [ ] Done when: Unauthorized users receive `403`.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Express.js docs

### 5.3 Permissions

- [ ] **Permission-Based Authorization** (Core)
- [ ] Concept: Separate permissions from roles.
- [ ] Build: SupportDesk AI — create:
  - `ticket:read`
  - `ticket:update`
  - `ticket:assign`
  - `ticket:delete`
- [ ] Done when: Routes check permissions rather than hard-coded roles.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

### 5.4 Resource Authorization

- [ ] **Resource-Level Authorization** (Core)
- [ ] Concept: Verify that the authenticated user can access the specific resource.
- [ ] Build: SupportDesk AI — prevent access to another team's ticket.
- [ ] Done when: Changing a ticket ID cannot expose another user's data.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/

### 5.5 Multi-Tenant Authorization

- [ ] **Multi-Tenant Authorization** (Next)
- [ ] Concept: Understand workspace/tenant boundaries.
- [ ] Build: TaskFlow — isolate users by workspace.
- [ ] Done when: Every database query is scoped to the authenticated workspace.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official OWASP Authorization Cheat Sheet

### 5.6 Frontend vs Backend Authorization

- [ ] **Frontend vs Backend Authorization** (Core)
- [ ] Concept: Frontend checks improve UX; backend checks provide security.
- [ ] Build: SupportDesk AI — hide unavailable actions in React and enforce permissions on the API.
- [ ] Done when: Direct API calls cannot bypass authorization.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/

### Phase 5 Checkpoint

- [ ] **Rebuild RBAC**
- [ ] Roles
- [ ] Permissions
- [ ] Role middleware
- [ ] Permission middleware
- [ ] Resource authorization
- [ ] Tenant isolation
- [ ] Frontend permission UI
- [ ] Backend enforcement
- [ ] No tutorial
- [ ] No AI-generated code

---

# Phase 6: Production Authentication Security

**Days:** 18–21
**Goal:** Harden authentication for production applications.
**Done when:** I can audit and test an authentication system before deployment.

### 6.1 Authentication Errors

- [ ] **Authentication Error Handling** (Core)
- [ ] Concept: Use appropriate `400`, `401`, `403`, `409`, and `429` responses.
- [ ] Build: SupportDesk AI — standardize authentication errors.
- [ ] Done when: Frontend receives predictable authentication errors.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status

### 6.2 Rate Limiting

- [ ] **Login Rate Limiting** (Core)
- [ ] Concept: Protect authentication endpoints from brute-force attacks.
- [ ] Build: TaskFlow — add rate limiting to login and password reset.
- [ ] Done when: Excessive attempts are throttled.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

### 6.3 CSRF & XSS

- [ ] **CSRF & XSS Protection** (Core)
- [ ] Concept: Understand browser attacks against authenticated applications.
- [ ] Build: TaskFlow — document CSRF/XSS risks for your authentication architecture.
- [ ] Done when: I can explain which defense protects against which attack.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

### 6.4 Password Reset

- [ ] **Password Reset & Email Verification** (Core)
- [ ] Concept: Understand one-time tokens, expiration, and invalidation.
- [ ] Build: SupportDesk AI — implement email verification and password reset.
- [ ] Done when: Reset tokens expire and cannot be reused.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html

### 6.5 Authentication Testing

- [ ] **Authentication Testing** (Core)
- [ ] Concept: Test valid, invalid, expired, revoked, and unauthorized scenarios.
- [ ] Build: SupportDesk AI — write authentication API integration tests.
- [ ] Done when: Critical authentication flows have automated tests.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Jest/Vitest and Supertest docs

### 6.6 Environment & Secrets

- [ ] **Authentication Secrets & Environment Variables** (Core)
- [ ] Concept: Securely manage JWT secrets, OAuth credentials, and database credentials.
- [ ] Build: TaskFlow — move all authentication secrets to environment configuration.
- [ ] Done when: No active credentials exist in source code.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Node.js environment variable documentation

### 6.7 Authentication Logging

- [ ] **Authentication Logging & Monitoring** (Next)
- [ ] Concept: Log useful security events without exposing credentials or tokens.
- [ ] Build: SupportDesk AI — log:
  - Login success
  - Login failure
  - Logout
  - Password changes
  - Role changes
  - Suspicious authentication activity
- [ ] Done when: Authentication events can be investigated safely.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

### Phase 6 Checkpoint

- [ ] **Production Authentication Audit**
- [ ] Password security
- [ ] Cookie security
- [ ] Session/token security
- [ ] OAuth security
- [ ] RBAC
- [ ] Resource authorization
- [ ] Rate limiting
- [ ] CSRF/XSS protection
- [ ] Password reset
- [ ] Testing
- [ ] Logging
- [ ] Secrets
- [ ] Production configuration

---

# Final Phase: Prove It

## Mini-Project: Production Authentication System

- [ ] Register
- [ ] Login
- [ ] Logout
- [ ] Password hashing
- [ ] Secure cookies
- [ ] Sessions
- [ ] Redis session storage
- [ ] JWT access tokens
- [ ] Refresh tokens
- [ ] Token rotation
- [ ] Google OAuth
- [ ] OpenID Connect
- [ ] Account linking
- [ ] Email verification
- [ ] Password reset
- [ ] RBAC
- [ ] Permissions
- [ ] Resource-level authorization
- [ ] Multi-tenant authorization
- [ ] Rate limiting
- [ ] CSRF protection
- [ ] XSS protection
- [ ] Authentication logging
- [ ] Automated tests
- [ ] Production environment configuration

---

## 10 Interview Questions

- [ ] What is authentication?
- [ ] What is authorization?
- [ ] Sessions vs JWT?
- [ ] Why hash passwords?
- [ ] What does HttpOnly mean?
- [ ] What does SameSite mean?
- [ ] What is a JWT?
- [ ] Access token vs refresh token?
- [ ] OAuth 2.0 vs OpenID Connect?
- [ ] `401` vs `403`?

---

## Production Checklist

### Security

- [ ] Passwords are securely hashed
- [ ] Secure cookies are configured
- [ ] HttpOnly is used where appropriate
- [ ] SameSite is configured appropriately
- [ ] HTTPS is enabled
- [ ] CORS is explicitly configured
- [ ] JWT signatures are verified
- [ ] JWT expiration is validated
- [ ] Refresh tokens can be revoked
- [ ] OAuth redirect URIs are restricted
- [ ] OAuth identity is verified
- [ ] Account linking is secure
- [ ] Backend authorization cannot be bypassed
- [ ] Resource ownership is checked
- [ ] Tenant boundaries are enforced
- [ ] Login is rate-limited
- [ ] Password reset is protected
- [ ] Secrets are not committed
- [ ] Tokens are not logged
- [ ] Authentication events are logged safely

### Testing

- [ ] Register test
- [ ] Login test
- [ ] Logout test
- [ ] Invalid password test
- [ ] Expired session test
- [ ] Expired JWT test
- [ ] Refresh-token test
- [ ] OAuth failure test
- [ ] RBAC test
- [ ] Resource authorization test
- [ ] Tenant isolation test
- [ ] Rate-limit test

### Deployment

- [ ] Environment variables configured
- [ ] Production cookies configured
- [ ] HTTPS configured
- [ ] CORS configured
- [ ] Database security reviewed
- [ ] Redis security reviewed
- [ ] OAuth production callback configured
- [ ] Authentication monitoring enabled
- [ ] Dependencies updated
- [ ] Verify current authentication/OAuth library documentation before deployment

---

## Explain Authentication in 5 Minutes

- [ ] Explain authentication
- [ ] Explain authorization
- [ ] Explain sessions
- [ ] Explain JWT
- [ ] Explain refresh tokens
- [ ] Explain Google OAuth
- [ ] Explain OpenID Connect
- [ ] Explain RBAC
- [ ] Explain permissions
- [ ] Explain `401` vs `403`
- [ ] Explain major authentication threats
- [ ] Explain major defenses

---

# What to Learn Next

- [ ] WebSockets / Socket.IO authentication
- [ ] Multi-tenant SaaS architecture
- [ ] API security
- [ ] OWASP Top 10
- [ ] Redis
- [ ] Security testing
- [ ] Webhook signature verification
- [ ] Passkeys / WebAuthn (Bonus)
- [ ] MFA / TOTP (Bonus)
- [ ] Enterprise SSO / SAML (Bonus)
- [ ] Managed identity providers (Bonus)

---

# Weekly Review Log

| Week | Topics finished | What I forgot | Fix |
|------|-----------------|---------------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
