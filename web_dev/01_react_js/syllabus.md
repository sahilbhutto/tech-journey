# React.js Syllabus

## PHASE 1: React Fundamentals

* [ ] What is React?
* [ ] Why React?
* [ ] React vs Vanilla JavaScript
* [ ] React application architecture
* [ ] React DOM
* [ ] JSX
* [ ] JSX expressions
* [ ] JSX rules and limitations
* [ ] Components
* [ ] Functional components
* [ ] Component composition
* [ ] Props
* [ ] Props destructuring
* [ ] `children` prop
* [ ] Rendering elements
* [ ] Conditional rendering
* [ ] Rendering lists
* [ ] `key` prop
* [ ] Fragments

---

## PHASE 2: State & User Interaction

* [ ] What is state?
* [ ] Props vs State
* [ ] `useState`
* [ ] State updates
* [ ] Functional state updates
* [ ] State immutability
* [ ] Updating objects in state
* [ ] Updating arrays in state
* [ ] Event handling
* [ ] Form events
* [ ] Controlled components
* [ ] Form inputs
* [ ] Multiple state values
* [ ] Lifting state up
* [ ] Derived state
* [ ] Avoiding unnecessary state

---

## PHASE 3: React Hooks

### Core Hooks

* [ ] `useState`
* [ ] `useEffect`
* [ ] `useContext`
* [ ] `useRef`
* [ ] `useReducer`

### Effect & Lifecycle Concepts

* [ ] What is an Effect?
* [ ] Dependency array
* [ ] Effect cleanup
* [ ] When `useEffect` runs
* [ ] Common `useEffect` mistakes
* [ ] When NOT to use `useEffect`

### Advanced Hooks

* [ ] Custom Hooks
* [ ] `useMemo`
* [ ] `useCallback`
* [ ] `useTransition`
* [ ] `useDeferredValue`

---

## PHASE 4: Forms & Validation

* [ ] Controlled forms
* [ ] Uncontrolled forms
* [ ] Form submission
* [ ] Input validation
* [ ] Client-side validation
* [ ] Error handling
* [ ] Loading states
* [ ] Form UX
* [ ] Formik
* [ ] React Hook Form
* [ ] Schema validation
* [ ] Zod integration

---

## PHASE 5: Component Architecture

* [ ] Component design principles
* [ ] Presentational vs container concepts
* [ ] Reusable components
* [ ] Compound components
* [ ] Component composition
* [ ] Prop drilling
* [ ] Avoiding excessive prop drilling
* [ ] Context API
* [ ] Custom Hooks for shared logic
* [ ] Component boundaries
* [ ] Feature-based architecture
* [ ] Reusable UI patterns
* [ ] Design system basics

---

## PHASE 6: Data Fetching & APIs

* [ ] Fetching API data
* [ ] `fetch`
* [ ] Axios
* [ ] GET requests
* [ ] POST requests
* [ ] PUT / PATCH requests
* [ ] DELETE requests
* [ ] Request states
* [ ] Loading states
* [ ] Error states
* [ ] Empty states
* [ ] API error handling
* [ ] Request cancellation
* [ ] Authentication API integration
* [ ] Pagination
* [ ] Search
* [ ] Filtering
* [ ] Sorting
* [ ] Optimistic UI

### Server State

* [ ] What is server state?
* [ ] Server state vs client state
* [ ] TanStack Query
* [ ] Queries
* [ ] Mutations
* [ ] Query keys
* [ ] Query invalidation
* [ ] Caching
* [ ] Background refetching
* [ ] Pagination with TanStack Query
* [ ] Infinite queries
* [ ] Optimistic updates

---

## PHASE 7: Routing

* [ ] Client-side routing
* [ ] React Router
* [ ] Routes
* [ ] Nested routes
* [ ] Route parameters
* [ ] Query parameters
* [ ] Navigation
* [ ] `Link`
* [ ] Programmatic navigation
* [ ] Protected routes
* [ ] Authentication routing
* [ ] 404 pages
* [ ] Route-based layouts
* [ ] Lazy-loaded routes

---

## PHASE 8: State Management

### Understand First

* [ ] Local state
* [ ] Lifted state
* [ ] Context state
* [ ] Server state
* [ ] Global client state
* [ ] When global state is actually needed

### Redux

* [ ] Redux fundamentals
* [ ] Store
* [ ] Actions
* [ ] Reducers
* [ ] Dispatch
* [ ] Selectors
* [ ] Redux Toolkit
* [ ] `createSlice`
* [ ] `configureStore`
* [ ] Async logic
* [ ] Redux DevTools

### Modern Alternatives

* [ ] Zustand
* [ ] Choosing Redux vs Zustand vs Context

---

## PHASE 9: Performance

* [ ] React rendering model
* [ ] Re-rendering
* [ ] Reconciliation
* [ ] Virtual DOM concept
* [ ] Identifying unnecessary re-renders
* [ ] React DevTools Profiler
* [ ] `React.memo`
* [ ] `useMemo`
* [ ] `useCallback`
* [ ] Code splitting
* [ ] `lazy`
* [ ] `Suspense`
* [ ] Dynamic imports
* [ ] Bundle optimization
* [ ] Large list optimization
* [ ] Virtualization
* [ ] Performance measurement
* [ ] Avoiding premature optimization

---

## PHASE 10: Advanced React

* [ ] Refs
* [ ] Forwarding refs
* [ ] Portals
* [ ] Error Boundaries
* [ ] Suspense
* [ ] Lazy loading
* [ ] Concurrent rendering concepts
* [ ] Transitions
* [ ] Deferred rendering
* [ ] Server Components concept
* [ ] React Server Components vs Client Components
* [ ] Hydration concept
* [ ] React Compiler concept
* [ ] React Actions concept
* [ ] Modern React APIs

---

## PHASE 11: TypeScript with React

* [ ] Why TypeScript with React?
* [ ] Typing component props
* [ ] Typing `children`
* [ ] Typing state
* [ ] Typing events
* [ ] Typing forms
* [ ] Typing refs
* [ ] Typing API responses
* [ ] Interfaces vs types
* [ ] Generics
* [ ] Generic components
* [ ] Utility types
* [ ] Discriminated unions
* [ ] Type-safe custom Hooks
* [ ] Type-safe Context
* [ ] Type-safe React Query

---

## PHASE 12: Testing

* [ ] Why test React applications?
* [ ] Unit testing concepts
* [ ] Integration testing concepts
* [ ] Component testing
* [ ] Vitest
* [ ] React Testing Library
* [ ] Testing components
* [ ] Testing user interactions
* [ ] Testing forms
* [ ] Testing async operations
* [ ] Mocking APIs
* [ ] Testing custom Hooks
* [ ] Test coverage
* [ ] End-to-end testing concepts
* [ ] Playwright basics

---

## PHASE 13: Authentication & Security

* [ ] Authentication vs Authorization
* [ ] Login / Signup UI
* [ ] Token-based authentication
* [ ] Cookies
* [ ] HttpOnly cookies
* [ ] Session concepts
* [ ] Protected routes
* [ ] Role-based access
* [ ] Permission-based UI
* [ ] Handling authentication state
* [ ] XSS
* [ ] CSRF
* [ ] CORS
* [ ] Secure API communication
* [ ] Avoiding sensitive data in localStorage

---

## PHASE 14: Production React

* [ ] Environment variables
* [ ] Development vs production configuration
* [ ] Error handling strategy
* [ ] Error boundaries
* [ ] Logging
* [ ] Loading UX
* [ ] Skeleton UI
* [ ] Empty states
* [ ] Error states
* [ ] Accessibility
* [ ] Semantic HTML
* [ ] Keyboard navigation
* [ ] ARIA basics
* [ ] SEO fundamentals
* [ ] Internationalization concepts
* [ ] Responsive UI
* [ ] Production build
* [ ] Deployment
* [ ] CI/CD basics

---

## PHASE 15: React Architecture

* [ ] Scalable folder structure
* [ ] Feature-based architecture
* [ ] Component organization
* [ ] Shared components
* [ ] Shared utilities
* [ ] API layer
* [ ] State layer
* [ ] Custom Hooks architecture
* [ ] Type organization
* [ ] Configuration management
* [ ] Error handling architecture
* [ ] Authentication architecture
* [ ] Permission architecture
* [ ] Large-scale React application patterns
* [ ] Monorepo concepts
