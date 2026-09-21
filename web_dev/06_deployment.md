# Deployment (Vercel, Docker Basics, GitHub Actions) Syllabus

**Level:** Intermediate → Production
**Total time:** 14 days
**Prerequisites:** JavaScript, TypeScript, React, Next.js, Node.js, Express, Git/GitHub, REST APIs
**Progress:** 0 / 27 topics done

---

## Skip for now

- [ ] Kubernetes
- [ ] Docker Swarm
- [ ] Terraform / Infrastructure as Code
- [ ] AWS advanced services
- [ ] Complex cloud networking
- [ ] Multi-region deployment
- [ ] Service mesh
- [ ] Advanced Kubernetes CI/CD
- [ ] Self-hosted GitHub Actions runners
- [ ] Advanced Linux server administration
- [ ] Complex AWS/GCP/Azure architecture

---

# Phase 1: Deployment Fundamentals

**Days:** 1–2
**Goal:** Understand what actually happens when a web application moves from local development to production.
**Done when:** I can deploy a full-stack application and explain every major step.

### 1.1 Development vs Production

- [ ] **Development vs Production** (Core)
- [ ] Concept: Understand build, runtime, environment, logging, security, and configuration differences.
- [ ] Build: TaskFlow — document local → build → deploy → production flow.
- [ ] Done when: I can explain what changes between development and production.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Vercel and Node.js docs

### 1.2 Build & Start Commands

- [ ] **Build & Start Process** (Core)
- [ ] Concept: Understand `install → build → start` and how production applications run.
- [ ] Build: TaskFlow — create production scripts for frontend and backend.
- [ ] Done when: I can build and run the application locally in production mode.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Node.js / Next.js docs

### 1.3 Environment Variables

- [ ] **Environment Variables** (Core)
- [ ] Concept: Understand development, production, public, and secret environment variables.
- [ ] Build: TaskFlow — configure database URL, authentication secrets, Stripe keys, and API URLs.
- [ ] Done when: No secret is hard-coded in the repository.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Vercel and Next.js environment variable docs

### 1.4 Production Configuration

- [ ] **Production Configuration** (Core)
- [ ] Concept: Understand CORS, URLs, cookies, HTTPS, database access, and API configuration in production.
- [ ] Build: TaskFlow — create a production configuration checklist.
- [ ] Done when: The application can run without development-only configuration.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Express.js and Next.js docs

### 1.5 Deployment Architecture

- [ ] **Frontend + Backend Deployment Architecture** (Core)
- [ ] Concept: Understand frontend hosting, backend hosting, database hosting, DNS, HTTPS, and environment variables.
- [ ] Build: TaskFlow — draw your production architecture.
- [ ] Done when: I can explain how browser → frontend → API → database works in production.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Vercel documentation

### Phase 1 Checkpoint

- [ ] Prepare TaskFlow for production
- [ ] Configure environment variables
- [ ] Create production build
- [ ] Run production build locally
- [ ] Document deployment architecture
- [ ] No tutorial
- [ ] No AI-generated code

---

# Phase 2: Vercel Deployment

**Days:** 3–5
**Goal:** Deploy modern React/Next.js applications using Vercel and understand the deployment workflow.
**Done when:** I can connect a GitHub repository to Vercel and deploy changes automatically.

### 2.1 Vercel Fundamentals

- [ ] **Vercel Projects & Deployments** (Core)
- [ ] Concept: Understand projects, deployments, builds, domains, and environments.
- [ ] Build: TaskFlow — create a Vercel project from your GitHub repository.
- [ ] Done when: The application is publicly accessible.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://vercel.com/docs

### 2.2 GitHub Integration

- [ ] **GitHub → Vercel Deployment** (Core)
- [ ] Concept: Understand repository connection and automatic deployments.
- [ ] Build: TaskFlow — connect GitHub and deploy from the main branch.
- [ ] Done when: A new GitHub push creates a deployment automatically.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://vercel.com/docs/git

### 2.3 Preview Deployments

- [ ] **Preview Deployments** (Core)
- [ ] Concept: Understand preview environments for branches and pull requests.
- [ ] Build: TaskFlow — create a feature branch and inspect its Vercel preview.
- [ ] Done when: A feature branch produces an isolated preview deployment.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://vercel.com/docs/deployments/environments

### 2.4 Environment Variables

- [ ] **Vercel Environment Variables** (Core)
- [ ] Concept: Configure variables separately for development, preview, and production.
- [ ] Build: TaskFlow — configure API URL, database configuration, and authentication variables.
- [ ] Done when: Preview and production use the correct configuration.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://vercel.com/docs/environment-variables

### 2.5 Custom Domain & HTTPS

- [ ] **Domain & HTTPS** (Next)
- [ ] Concept: Understand custom domains, DNS, SSL/TLS, and HTTPS.
- [ ] Build: TaskFlow — connect a custom domain if available.
- [ ] Done when: The application is accessible through HTTPS.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://vercel.com/docs/domains

### 2.6 Deployment Logs

- [ ] **Build & Runtime Logs** (Core)
- [ ] Concept: Learn how to diagnose failed builds and production errors.
- [ ] Build: TaskFlow — intentionally introduce a deployment error and diagnose it from logs.
- [ ] Done when: I can identify whether an error comes from build, environment, runtime, or application code.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://vercel.com/docs/logs

### Phase 2 Checkpoint

- [ ] Deploy TaskFlow to Vercel
- [ ] Connect GitHub
- [ ] Automatic deployment
- [ ] Preview deployment
- [ ] Environment variables
- [ ] Custom domain
- [ ] HTTPS
- [ ] Read deployment logs
- [ ] Roll back or redeploy a previous version

---

# Phase 3: Docker Basics

**Days:** 6–9
**Goal:** Understand containers and package a Node.js application into a production-style Docker image.
**Done when:** I can write a Dockerfile, build an image, run a container, and debug common container problems.

### 3.1 Containers vs Virtual Machines

- [ ] **Containers & Images** (Core)
- [ ] Concept: Understand images, containers, isolation, and how containers differ from virtual machines.
- [ ] Build: ChatSpace — run the backend inside a Docker container.
- [ ] Done when: I can explain image vs container without notes.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/get-started/

### 3.2 Dockerfile

- [ ] **Dockerfile Fundamentals** (Core)
- [ ] Concept: Understand `FROM`, `WORKDIR`, `COPY`, `RUN`, `ENV`, `EXPOSE`, and `CMD`.
- [ ] Build: ChatSpace — create a Dockerfile for the Node.js backend.
- [ ] Done when: I can build the image successfully.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/reference/dockerfile/

### 3.3 Docker Images

- [ ] **Build & Manage Images** (Core)
- [ ] Concept: Understand image layers, tags, builds, and image size.
- [ ] Build: ChatSpace — build, tag, inspect, and remove Docker images.
- [ ] Done when: I can manage the image from the CLI.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/get-started/docker-concepts/building-images/

### 3.4 Docker Containers

- [ ] **Run & Manage Containers** (Core)
- [ ] Concept: Understand ports, logs, exec, start, stop, restart, and container lifecycle.
- [ ] Build: ChatSpace — run the backend container and expose its API port.
- [ ] Done when: React can communicate with the containerized backend.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/get-started/docker-concepts/running-containers/

### 3.5 Docker Volumes & Bind Mounts

- [ ] **Persistent Data & Mounts** (Next)
- [ ] Concept: Understand container filesystem lifecycle, volumes, and bind mounts.
- [ ] Build: ChatSpace — mount a development directory for live development.
- [ ] Done when: I understand which data disappears with a container and which can persist.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/engine/storage/

### 3.6 Docker Networks

- [ ] **Container Networking** (Core)
- [ ] Concept: Understand container-to-container communication and service names.
- [ ] Build: ChatSpace — connect backend and Redis containers through a Docker network.
- [ ] Done when: Backend can communicate with Redis without using `localhost` incorrectly.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/engine/network/

### 3.7 Docker Compose

- [ ] **Docker Compose Basics** (Core)
- [ ] Concept: Define and run multiple services from one configuration.
- [ ] Build: ChatSpace — create:
  - Backend
  - MongoDB
  - Redis
- [ ] Done when: One command starts the complete development stack.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/compose/

### 3.8 Production Docker Image

- [ ] **Production Dockerfile** (Core)
- [ ] Concept: Understand smaller images, dependency installation, `.dockerignore`, non-root execution, and production commands.
- [ ] Build: ChatSpace — optimize the backend Docker image for production.
- [ ] Done when: The image contains only what the application needs to run.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/build/building/best-practices/

### Phase 3 Checkpoint

- [ ] Write Dockerfile from memory
- [ ] Build image
- [ ] Run container
- [ ] Expose port
- [ ] Inspect logs
- [ ] Execute shell inside container
- [ ] Create Docker network
- [ ] Create Docker Compose setup
- [ ] Run backend + database + Redis
- [ ] Build optimized production image

---

# Phase 4: GitHub Actions & CI

**Days:** 10–12
**Goal:** Automate testing, linting, building, and deployment using GitHub Actions.
**Done when:** Every important GitHub change can automatically pass through a CI pipeline.

### 4.1 GitHub Actions Fundamentals

- [ ] **Workflows, Jobs & Steps** (Core)
- [ ] Concept: Understand workflows, jobs, steps, runners, triggers, and actions.
- [ ] Build: SupportDesk AI — create your first CI workflow.
- [ ] Done when: A GitHub push triggers an automated workflow.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.github.com/en/actions

### 4.2 Workflow Triggers

- [ ] **Workflow Triggers** (Core)
- [ ] Concept: Understand `push`, `pull_request`, manual, and other workflow triggers.
- [ ] Build: SupportDesk AI — run CI on pushes and pull requests.
- [ ] Done when: Pull requests automatically run checks.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

### 4.3 Node.js CI

- [ ] **Node.js CI Pipeline** (Core)
- [ ] Concept: Automate dependency installation, linting, tests, and builds.
- [ ] Build: SupportDesk AI — create:
  - Install
  - Lint
  - Test
  - Build
- [ ] Done when: Broken code causes the CI workflow to fail.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-nodejs

### 4.4 Secrets

- [ ] **GitHub Actions Secrets** (Core)
- [ ] Concept: Safely provide credentials to CI without committing them.
- [ ] Build: SupportDesk AI — configure required CI secrets.
- [ ] Done when: No secret appears directly in workflow files.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions

### 4.5 Dependency & Cache Strategy

- [ ] **CI Dependency Caching** (Next)
- [ ] Concept: Understand dependency caching and why it can reduce CI execution time.
- [ ] Build: SupportDesk AI — configure dependency caching.
- [ ] Done when: Repeated CI runs reuse appropriate cached dependencies.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows

### 4.6 Branch Protection & Required Checks

- [ ] **CI as a Merge Gate** (Core)
- [ ] Concept: Understand why automated checks should protect the main branch.
- [ ] Build: SupportDesk AI — require CI checks before merging pull requests.
- [ ] Done when: Broken CI cannot be merged through the normal workflow.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official GitHub branch protection / rulesets docs
- Verify current GitHub UI and ruleset behavior in official docs.

### Phase 4 Checkpoint

- [ ] GitHub Actions workflow
- [ ] Push trigger
- [ ] Pull request trigger
- [ ] Install dependencies
- [ ] Lint
- [ ] Test
- [ ] Build
- [ ] Secrets
- [ ] Dependency cache
- [ ] Required checks
- [ ] Protected main branch

---

# Phase 5: Production CI/CD

**Days:** 13–14
**Goal:** Connect testing, Docker, GitHub, and deployment into a reliable production workflow.
**Done when:** A production deployment can happen through a controlled, repeatable pipeline.

### 5.1 CI vs CD

- [ ] **Continuous Integration vs Continuous Deployment** (Core)
- [ ] Concept: Understand CI, continuous delivery, and continuous deployment.
- [ ] Build: TaskFlow — document your complete CI/CD pipeline.
- [ ] Done when: I can explain where testing ends and deployment begins.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official GitHub Actions docs

### 5.2 Docker Build in CI

- [ ] **Build Docker Images in GitHub Actions** (Core)
- [ ] Concept: Build reproducible Docker images automatically.
- [ ] Build: ChatSpace — build the backend Docker image in CI.
- [ ] Done when: Every valid main-branch change can produce a Docker image.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.docker.com/build/ci/github-actions/

### 5.3 Container Registry

- [ ] **Docker Image Registry** (Next)
- [ ] Concept: Understand image registries, tags, authentication, and image publishing.
- [ ] Build: ChatSpace — publish the Docker image to a container registry.
- [ ] Done when: The deployed environment can pull your application image.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official GitHub Container Registry / Docker Hub docs

### 5.4 Automated Deployment

- [ ] **Automated Deployment Pipeline** (Core)
- [ ] Concept: Connect GitHub Actions to the deployment platform.
- [ ] Build: TaskFlow — deploy after successful CI.
- [ ] Done when: Deployment cannot happen if required tests fail.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Vercel and GitHub Actions docs
- Verify current deployment integration in official docs.

### 5.5 Rollback & Recovery

- [ ] **Deployment Rollback** (Core)
- [ ] Concept: Understand failed deployments, previous versions, rollback, and recovery.
- [ ] Build: TaskFlow — intentionally deploy a broken version and recover using a previous deployment.
- [ ] Done when: I can restore a working version without rebuilding the application manually.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Vercel deployment/rollback docs

### 5.6 Production Health Checks

- [ ] **Deployment Verification** (Core)
- [ ] Concept: Verify that a deployment is actually working after it becomes live.
- [ ] Build: SupportDesk AI — add a `/health` endpoint and post-deployment smoke test.
- [ ] Done when: The pipeline can detect a basic production failure.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official GitHub Actions and Express.js docs

### Phase 5 Checkpoint

- [ ] CI pipeline
- [ ] Tests
- [ ] Lint
- [ ] Build
- [ ] Docker build
- [ ] Image registry
- [ ] Deployment
- [ ] Health check
- [ ] Rollback
- [ ] Production verification

---

# Final Phase: Prove It

## Mini-Project: Production Deployment Pipeline

### TaskFlow

- [ ] React / Next.js frontend
- [ ] Production build
- [ ] Vercel deployment
- [ ] GitHub integration
- [ ] Preview deployments
- [ ] Production environment variables
- [ ] Custom domain
- [ ] HTTPS

### ChatSpace

- [ ] Node.js backend
- [ ] Dockerfile
- [ ] Docker image
- [ ] Docker Compose
- [ ] MongoDB container
- [ ] Redis container
- [ ] Docker network
- [ ] Production image

### SupportDesk AI

- [ ] GitHub Actions
- [ ] Lint
- [ ] Tests
- [ ] Build
- [ ] Secrets
- [ ] Dependency caching
- [ ] Required checks
- [ ] Docker build
- [ ] Image registry
- [ ] Deployment
- [ ] Health check
- [ ] Rollback

---

## 10 Interview Questions

- [ ] What happens when you deploy a web application?
- [ ] What is the difference between development and production?
- [ ] What is Vercel?
- [ ] What is a Docker image?
- [ ] What is a Docker container?
- [ ] Docker image vs container?
- [ ] Why use Docker?
- [ ] What is Docker Compose?
- [ ] What is GitHub Actions?
- [ ] CI vs CD?

---

## Production Checklist

### Application

- [ ] Production build works
- [ ] Environment variables configured
- [ ] No secrets committed
- [ ] Production API URL configured
- [ ] CORS configured
- [ ] HTTPS enabled
- [ ] Database connection verified
- [ ] Authentication configuration verified
- [ ] Error handling verified
- [ ] Health endpoint available

### Vercel

- [ ] GitHub repository connected
- [ ] Preview deployments working
- [ ] Production deployment working
- [ ] Environment variables configured
- [ ] Domain configured
- [ ] HTTPS working
- [ ] Build logs checked
- [ ] Runtime logs checked
- [ ] Rollback procedure tested

### Docker

- [ ] Dockerfile works
- [ ] `.dockerignore` configured
- [ ] Image builds successfully
- [ ] Image size reviewed
- [ ] Correct production command configured
- [ ] Non-root execution considered
- [ ] Ports configured correctly
- [ ] Container logs available
- [ ] Docker Compose works locally
- [ ] Database/Redis networking works

### GitHub Actions

- [ ] CI workflow exists
- [ ] Pull request checks run
- [ ] Dependencies install
- [ ] Lint runs
- [ ] Tests run
- [ ] Production build runs
- [ ] Secrets configured
- [ ] Dependency caching configured
- [ ] Main branch protected
- [ ] Failed checks block normal merges
- [ ] Docker image builds
- [ ] Deployment runs only after required checks
- [ ] Deployment failure is visible

### Reliability

- [ ] Health check works
- [ ] Logs are available
- [ ] Errors are monitored
- [ ] Previous deployment can be restored
- [ ] Database backups are configured where applicable
- [ ] Production environment is reproducible
- [ ] Deployment process is documented
- [ ] Current Vercel, Docker, and GitHub Actions behavior verified in official docs before production deployment

---

# What to Learn Next

- [ ] Linux production servers
- [ ] Nginx
- [ ] Reverse proxy
- [ ] DNS
- [ ] SSL/TLS
- [ ] PostgreSQL production deployment
- [ ] Redis production deployment
- [ ] Cloud deployment fundamentals
- [ ] AWS fundamentals
- [ ] Monitoring & observability
- [ ] Logging
- [ ] Error tracking
- [ ] Infrastructure as Code (Next)
- [ ] Kubernetes (Later)
- [ ] Terraform (Later)

---

# Weekly Review Log

| Week | Topics finished | What I forgot | Fix |
|------|-----------------|---------------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |
