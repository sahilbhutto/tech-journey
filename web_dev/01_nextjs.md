# Next.js Syllabus

**Level:** Intermediate → Advanced
**Total time:** 30 days
**Prerequisites:** React, TypeScript, JavaScript, Basics of Backend
**Progress:** 0 / 35 topics done

---

# Phase 1: App Router Foundations

**Days:** 1–5
**Goal:** Understand modern Next.js structure, routing, layouts, and Server/Client Components.
**Done when:** I can build a multi-page Next.js application from memory.

---

## 1.1 Next.js Architecture

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Understand Next.js as a React full-stack framework.
  - Understand App Router and server-first architecture.

- [ ] Build
  - Create the initial **TaskFlow** Next.js application.
  - Done when I can explain the purpose of the major folders/files.

**Docs:** https://nextjs.org/docs

---

## 1.2 File-System Routing

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `app/`
  - `page.tsx`
  - Nested routes
  - Route groups
  - `layout.tsx`

- [ ] Build
  - Create TaskFlow routes:
    - `/`
    - `/login`
    - `/dashboard`
    - `/projects`
    - `/settings`
  - Done when all routes work with shared layouts.

**Docs:** https://nextjs.org/docs/app

---

## 1.3 Dynamic Routes

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `[id]`
  - `[slug]`
  - Nested dynamic routes
  - Route parameters

- [ ] Build
  - Create:
    - `/projects/[projectId]`
    - `/tasks/[taskId]`
  - Done when route parameters are correctly displayed.

**Docs:** https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes

---

## 1.4 Navigation

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `Link`
  - `redirect`
  - `notFound`
  - Programmatic navigation

- [ ] Build
  - Create TaskFlow sidebar navigation.
  - Add project/task redirects.
  - Add 404 pages.
  - Done when navigation works without unnecessary full-page reloads.

**Docs:** https://nextjs.org/docs/app/api-reference/functions/redirect

---

## 1.5 Server Components

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Server Components
  - Server/client boundary
  - `'use client'`
  - Serialization
  - When Client Components are required

- [ ] Build
  - Make the TaskFlow dashboard server-rendered.
  - Keep interactive filters/modals on the client.
  - Done when I can explain every `'use client'` in the application.

**Docs:** https://nextjs.org/docs/app/getting-started/server-and-client-components

---

## Phase 1 Checkpoint

- [ ] Rebuild TaskFlow dashboard from an empty project.
- [ ] Create nested routes.
- [ ] Create layouts.
- [ ] Create dynamic routes.
- [ ] Add navigation.
- [ ] Add 404 handling.
- [ ] Use Server + Client Components correctly.
- [ ] No tutorial.
- [ ] No AI-generated code.

---

# Phase 2: Data Fetching & Rendering

**Days:** 6–12
**Goal:** Learn how Next.js fetches, renders, streams, and displays application data.
**Done when:** I can choose the correct rendering and data-fetching approach.

---

## 2.1 Server-Side Data Fetching

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Fetch data inside Server Components.
  - Understand server-side data access.

- [ ] Build
  - Fetch TaskFlow projects/tasks.
  - Done when dashboard data loads without `useEffect`.

**Docs:** https://nextjs.org/docs/app/building-your-application/data-fetching

---

## 2.2 Loading UI

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `loading.tsx`
  - Suspense
  - Streaming
  - Skeleton UI

- [ ] Build
  - Add TaskFlow dashboard skeletons.
  - Done when slow content does not block the entire page.

**Docs:** https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming

---

## 2.3 Static vs Dynamic Rendering

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Static rendering
  - Dynamic rendering
  - Request-time data
  - Rendering decisions

- [ ] Build
  - Make TaskFlow marketing pages static.
  - Make dashboard pages dynamic.
  - Done when I can explain why each route uses its rendering strategy.

**Docs:** https://nextjs.org/docs/app/building-your-application/rendering

---

## 2.4 Search Params

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - URL search parameters
  - Filters
  - Sorting
  - Pagination
  - URL-driven state

- [ ] Build
  - Add TaskFlow task search/filtering.
  - Example:
    - `?status=todo`
    - `?search=api`
  - Done when filters survive refresh and can be shared.

**Docs:** https://nextjs.org/learn/dashboard-app/adding-search-and-pagination

---

## 2.5 Error Handling

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `error.tsx`
  - `not-found.tsx`
  - `notFound()`
  - Error boundaries

- [ ] Build
  - Add TaskFlow error states.
  - Add project/task 404 handling.
  - Done when expected failures show useful UI.

**Docs:** https://nextjs.org/docs/app/building-your-application/routing/error-handling

---

## 2.6 Image & Font Optimization

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `next/image`
  - `next/font`
  - Responsive images
  - Asset optimization

- [ ] Build
  - Optimize TaskFlow avatars and project images.
  - Done when images and fonts are properly optimized.

**Docs:** https://nextjs.org/docs/app/getting-started/images

---

## Phase 2 Checkpoint

- [ ] Rebuild TaskFlow dashboard.
- [ ] Server data fetching.
- [ ] Loading states.
- [ ] Streaming.
- [ ] Search params.
- [ ] Pagination.
- [ ] Error handling.
- [ ] Optimized images.
- [ ] No tutorial.
- [ ] No AI-generated code.

---

# Phase 3: Full-Stack Next.js

**Days:** 13–20
**Goal:** Build backend functionality directly inside Next.js.
**Done when:** I can build a complete CRUD feature with validation and database persistence.

---

## 3.1 Route Handlers

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - `route.ts`
  - GET
  - POST
  - PATCH
  - DELETE
  - Request/Response

- [ ] Build
  - Create TaskFlow API routes.
  - Done when task CRUD works through Route Handlers.


**Docs:** https://nextjs.org/docs/app/building-your-application/routing/route-handlers

---

## 3.2 Server Actions

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Server-side mutations
  - Forms
  - Server/client boundary

- [ ] Build
  - Create/update/delete TaskFlow tasks using Server Actions.
  - Done when appropriate mutations execute on the server.


**Docs:** https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations

**Verify in official docs:** Server Actions APIs may change between Next.js releases.

---

## 3.3 Forms & Validation

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Server-side validation
  - Form errors
  - Untrusted input
  - Zod

- [ ] Build
  - Create TaskFlow task form.
  - Validate with Zod.
  - Done when invalid data cannot reach the database.


**Docs:** https://nextjs.org/docs

---

## 3.4 Database Integration

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Database access from server code
  - ORM
  - Environment variables
  - Connection management

- [ ] Build
  - Connect TaskFlow to PostgreSQL.
  - Use Prisma or Drizzle.
  - Done when users/projects/tasks persist correctly.


**Docs:** Search official Prisma or Drizzle docs.

---

## 3.5 Cache & Revalidation

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Next.js caching
  - Revalidation
  - `revalidatePath`
  - `revalidateTag`

- [ ] Build
  - Update TaskFlow task lists after mutations.
  - Done when stale data is invalidated correctly.


**Docs:** https://nextjs.org/docs/app/api-reference/functions/revalidatePath

**Verify in official docs:** Next.js caching behavior is evolving.

---

## 3.6 Cookies & Headers

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - Cookies
  - Headers
  - Request context
  - Server-side session data

- [ ] Build
  - Implement TaskFlow session-related server logic.
  - Done when sensitive state is handled server-side.


**Docs:** https://nextjs.org/docs/app/api-reference/functions/cookies

---

## Phase 3 Checkpoint

- [ ] Build complete TaskFlow CRUD.
- [ ] Database.
- [ ] Route Handler.
- [ ] Server Action.
- [ ] Form.
- [ ] Validation.
- [ ] Authentication-aware server logic.
- [ ] Cache invalidation.
- [ ] Error handling.
- [ ] No tutorial.
- [ ] No AI-generated code.

---

# Phase 4: Authentication & Realtime

**Days:** 21–27
**Goal:** Build secure multi-user applications and understand realtime architecture.
**Done when:** I can implement authentication, authorization, and realtime application boundaries.

---

## 4.1 Authentication

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Authentication
  - Sessions
  - Cookies
  - Password hashing
  - OAuth
  - Login/logout

- [ ] Build
  - Add authentication to TaskFlow.
  - Done when users can register, login, logout, and maintain sessions.

**Docs:** https://nextjs.org/docs/app/guides/authentication

**Verify in official docs:** Authentication libraries and recommended patterns change over time.

---

## 4.2 Authorization

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Roles
  - Permissions
  - Resource ownership
  - Server-side authorization

- [ ] Build
  - TaskFlow roles:
    - Owner
    - Admin
    - Member
  - Done when unauthorized users cannot perform restricted mutations.

**Docs:** https://nextjs.org/docs/app/guides/authentication

---

## 4.3 Proxy

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - `proxy.ts`
  - Matchers
  - Request interception
  - Authentication-aware routing

- [ ] Build
  - Protect TaskFlow routes with Proxy.
  - Done when unauthenticated users cannot access protected areas.


**Docs:** https://nextjs.org/docs/app/api-reference/file-conventions/proxy

**Verify in official docs:** `proxy.ts` replaced the older `middleware.ts` convention in modern Next.js.

---

## 4.4 ChatSpace Realtime Architecture

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - HTTP vs WebSocket
  - Realtime events
  - Connection lifecycle
  - Presence
  - Message delivery

- [ ] Build
  - Design ChatSpace using Next.js + Socket.IO/WebSockets/Supabase Realtime.
  - Done when I can explain which responsibilities belong to Next.js and the realtime layer.


**Docs:** Search official Next.js and chosen realtime provider docs.

---

## 4.5 Optimistic UI

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Pending state
  - Optimistic updates
  - Rollback
  - Error recovery

- [ ] Build
  - Add optimistic task completion to TaskFlow.
  - Add optimistic messages to ChatSpace.
  - Done when failed mutations safely recover.

**Docs:** https://nextjs.org/docs

---

## Phase 4 Checkpoint

- [ ] Authentication.
- [ ] Authorization.
- [ ] Protected routes.
- [ ] Role-based permissions.
- [ ] Optimistic UI.
- [ ] ChatSpace realtime architecture.
- [ ] No tutorial.
- [ ] No AI-generated code.

---

# Phase 5: Production Engineering

**Days:** 28–35
**Goal:** Make Next.js applications secure, fast, testable, observable, and deployable.
**Done when:** I can deploy and maintain a production Next.js application.

---

## 5.1 Metadata & SEO

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Metadata
  - `generateMetadata`
  - Open Graph
  - Robots
  - Sitemap

- [ ] Build
  - Add SEO to TaskFlow.
  - Done when important pages have correct metadata and social previews.

**Docs:** https://nextjs.org/docs/app/getting-started/metadata-and-og-images

---

## 5.2 Performance Optimization

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Client JavaScript
  - Code splitting
  - Dynamic imports
  - Images
  - Fonts
  - Bundle size

- [ ] Build
  - Audit TaskFlow.
  - Remove unnecessary Client Components.
  - Done when I can identify the major performance bottlenecks.

**Docs:** https://nextjs.org/docs/app/building-your-application/optimizing

---

## 5.3 Modern Caching

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - `use cache`
  - Cache boundaries
  - Revalidation
  - Partial rendering concepts

- [ ] Build
  - Design caching for TaskFlow dashboard/project data.
  - Done when I can explain what is cached and when it becomes fresh.


**Docs:** https://nextjs.org/docs/app/getting-started/cache-components

**Verify in official docs:** Cache Components behavior and APIs may change.

---

## 5.4 Security

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - XSS
  - CSRF
  - Injection
  - Secret exposure
  - Authorization bugs
  - Unsafe redirects
  - Input validation

- [ ] Build
  - Perform a security review of TaskFlow.
  - Done when I can document major threats and mitigations.

**Docs:** https://nextjs.org/docs/app/guides/security

**Verify in official docs:** Check current Next.js security advisories before production.

---

## 5.5 Testing

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Unit testing
  - Integration testing
  - Component testing
  - E2E testing

- [ ] Build
  - Test TaskFlow authentication and CRUD.
  - Use:
    - Vitest/Jest
    - React Testing Library
    - Playwright
  - Done when critical workflows are automated.

**Docs:** https://nextjs.org/docs/app/guides/testing

---

## 5.6 Environment Variables

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Server secrets
  - `NEXT_PUBLIC_*`
  - Environment-specific configuration

- [ ] Build
  - Configure:
    - Local
    - Preview
    - Production
  - Done when no secret is exposed to the browser.

**Docs:** https://nextjs.org/docs/app/guides/environment-variables

---

## 5.7 Deployment

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Production build
  - Environment variables
  - Preview deployments
  - Logs
  - Rollbacks

- [ ] Build
  - Deploy TaskFlow.
  - Done when I can deploy and diagnose a failed production build.

**Docs:** https://nextjs.org/docs/app/building-your-application/deploying

---

## Phase 5 Checkpoint

- [ ] SEO.
- [ ] Performance audit.
- [ ] Caching.
- [ ] Security review.
- [ ] Automated tests.
- [ ] Environment configuration.
- [ ] Production deployment.
- [ ] Logs and error handling.
- [ ] No tutorial.
- [ ] No AI-generated code.

---

# Phase 6: Advanced Next.js & AI Applications

**Days:** 36–42
**Goal:** Use Next.js for complex SaaS, realtime, and AI-powered applications.
**Done when:** I can architect and build production-level Next.js features independently.

---

## 6.1 Advanced Routing

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - Route Groups
  - Parallel Routes
  - Intercepting Routes
  - Advanced layouts

- [ ] Build
  - Design ChatSpace conversation/modal routing.
  - Done when I can explain why advanced routing is useful.

**Docs:** https://nextjs.org/docs/app/building-your-application/routing

**Verify in official docs:** Advanced routing behavior can change.

---

## 6.2 Multi-Tenant SaaS

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Organizations
  - Memberships
  - Tenant isolation
  - Workspace routing
  - Permissions

- [ ] Build
  - Convert TaskFlow into a multi-tenant SaaS.
  - Done when Organization A cannot access Organization B data.


**Docs:** Search official Next.js multi-tenant documentation.

---

## 6.3 AI Application Architecture

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Server-side AI calls
  - Streaming
  - Secrets
  - Tool execution
  - AI persistence

- [ ] Build
  - Start SupportDesk AI.
  - Add ticket page + AI response endpoint.
  - Done when API keys never reach the browser.

**Docs:** https://nextjs.org/docs

**Verify in official docs and chosen AI SDK/provider documentation.**

---

## 6.4 Streaming AI UX

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Streaming responses
  - Pending UI
  - Cancellation
  - Retries
  - AI errors

- [ ] Build
  - Add streaming AI ticket suggestions to SupportDesk AI.
  - Done when generated content appears progressively.

**Docs:** Search official Next.js streaming docs and chosen AI SDK docs.

**Verify in official docs:** AI SDK and streaming APIs change quickly.

---

## 6.5 Background Jobs

**Priority:** Next
**Time:** ~2h

- [ ] Concept
  - Long-running work
  - Queues
  - Background processing
  - Retries
  - Job status

- [ ] Build
  - Process SupportDesk AI ticket summaries as background jobs.
  - Done when the HTTP request can finish while processing continues safely.


**Docs:** Search official Next.js runtime/deployment docs and chosen queue/workflow provider docs.

---

## 6.6 Observability

**Priority:** Core
**Time:** ~2h

- [ ] Concept
  - Structured logs
  - Error tracking
  - Request IDs
  - Tracing
  - Performance monitoring

- [ ] Build
  - Add observability to SupportDesk AI.
  - Done when I can trace a failed ticket request from UI → server → AI operation.

**Docs:** Search official Next.js instrumentation and observability documentation.

---

## Phase 6 Checkpoint

- [ ] Multi-tenant SaaS.
- [ ] Advanced routing.
- [ ] AI integration.
- [ ] Streaming responses.
- [ ] Background jobs.
- [ ] Observability.
- [ ] Production security.
- [ ] No tutorial.
- [ ] No AI-generated code.

---

# Final Phase: Prove It

## Mini-Project: SupportDesk AI

- [ ] App Router
- [ ] TypeScript
- [ ] Authentication
- [ ] Multi-tenant organizations
- [ ] Role-based authorization
- [ ] Dashboard
- [ ] Ticket CRUD
- [ ] Server Components
- [ ] Client Components
- [ ] Server Actions
- [ ] Route Handlers
- [ ] Zod validation
- [ ] PostgreSQL
- [ ] Prisma/Drizzle
- [ ] Search
- [ ] URL filters
- [ ] Pagination
- [ ] Loading states
- [ ] Error states
- [ ] AI ticket summarization
- [ ] AI reply generation
- [ ] Streaming AI responses
- [ ] Background processing
- [ ] Caching
- [ ] Revalidation
- [ ] SEO
- [ ] Image optimization
- [ ] Testing
- [ ] Security review
- [ ] Deployment
- [ ] Logging
- [ ] Monitoring
- [ ] Production README
- [ ] Architecture diagram
- [ ] Technical decision documentation

---

## Interview Proof

- [ ] Answer 10 Next.js questions out loud.
- [ ] Explain App Router.
- [ ] Explain Server Components.
- [ ] Explain Client Components.
- [ ] Explain Server Actions.
- [ ] Explain Route Handlers.
- [ ] Explain Next.js caching.
- [ ] Explain revalidation.
- [ ] Explain authentication/authorization.
- [ ] Explain Next.js performance optimization.
- [ ] Explain how you would build an AI SaaS with Next.js.

---

## Production Checklist

- [ ] Authentication
- [ ] Authorization
- [ ] Input validation
- [ ] Rate limiting
- [ ] Secret management
- [ ] Security headers
- [ ] Error handling
- [ ] Logging
- [ ] Monitoring
- [ ] Database indexes
- [ ] Database backups
- [ ] Caching
- [ ] Performance testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] E2E tests
- [ ] Accessibility
- [ ] SEO
- [ ] Mobile responsiveness
- [ ] Production deployment
- [ ] Rollback strategy

---

## 5-Minute Explanation Test

- [ ] Explain what Next.js is.
- [ ] Explain App Router.
- [ ] Explain Server Components.
- [ ] Explain Client Components.
- [ ] Explain data fetching.
- [ ] Explain mutations.
- [ ] Explain caching.
- [ ] Explain authentication.
- [ ] Explain deployment.
- [ ] Explain how Next.js fits into a modern full-stack architecture.
