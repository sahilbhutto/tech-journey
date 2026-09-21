# File Uploads Syllabus

**Topic:** File Uploads with S3 / Cloudflare R2 + Presigned URLs
**Level:** Intermediate → Advanced
**Duration:** 12–14 Days
**Prerequisites:** Node.js, Express, REST APIs, authentication, basic cloud concepts

**Projects:**
- TaskFlow — SaaS project
- ChatSpace — Real-time chat
- SupportDesk AI — AI ticketing system

**Goal:** Build a secure, scalable, production-ready file upload system using object storage and presigned URLs.

**Progress:** 0 / 31 topics completed

---

# Phase 1: File Upload Fundamentals

**Days 1–2**

**Goal:** Understand how files move from browser → backend → storage.

### 1.1 File Upload Architecture — Core

- [ ] Browser → Backend → Storage
- [ ] Browser → Storage directly
- [ ] Temporary files
- [ ] Permanent object storage
- [ ] File metadata
- [ ] Build: Basic avatar upload in TaskFlow
- [ ] Done when: You can explain the complete upload flow

### 1.2 HTTP File Uploads — Core

- [ ] `multipart/form-data`
- [ ] FormData
- [ ] File objects
- [ ] Multipart requests
- [ ] Request size limits
- [ ] Build: Profile image upload
- [ ] Done when: You can upload a file from React to Express

### 1.3 Node.js File Handling — Core

- [ ] Buffers
- [ ] Streams
- [ ] File system basics
- [ ] Temporary files
- [ ] Memory vs disk uploads
- [ ] Build: Temporary document upload
- [ ] Done when: You understand why streams matter for large files

### 1.4 Express File Upload Middleware — Core

- [ ] Multer
- [ ] Memory storage
- [ ] Disk storage
- [ ] File metadata
- [ ] Multiple files
- [ ] Upload limits
- [ ] Build: Multiple attachment upload
- [ ] Done when: Express can safely receive multiple files

### Phase 1 Checkpoint

- [ ] Explain multipart/form-data
- [ ] Explain Buffer vs Stream
- [ ] Upload one file
- [ ] Upload multiple files
- [ ] Validate basic file metadata

---

# Phase 2: Object Storage

**Days 3–4**

**Goal:** Move uploaded files from local storage to production object storage.

### 2.1 Object Storage Fundamentals — Core

- [ ] Object storage
- [ ] Buckets
- [ ] Objects
- [ ] Object keys
- [ ] Metadata
- [ ] Regions
- [ ] Public vs private objects
- [ ] Build: File storage architecture for TaskFlow
- [ ] Done when: You understand object-storage architecture

### 2.2 Amazon S3 — Core

- [ ] S3 buckets
- [ ] Objects
- [ ] Object keys
- [ ] AWS credentials
- [ ] IAM basics
- [ ] Bucket permissions
- [ ] Build: Upload files to S3
- [ ] Done when: Your backend can upload an object to S3

### 2.3 Cloudflare R2 — Core

- [ ] R2 buckets
- [ ] S3-compatible API
- [ ] Access credentials
- [ ] Endpoint configuration
- [ ] Public/private storage
- [ ] Build: Upload files to R2
- [ ] Done when: You can switch between S3 and R2 concepts

### 2.4 AWS SDK / S3-Compatible SDK — Core

- [ ] S3 client
- [ ] Upload commands
- [ ] Download commands
- [ ] Delete commands
- [ ] Head object
- [ ] Object metadata
- [ ] Error handling
- [ ] Build: File storage service
- [ ] Done when: Storage logic is separated from Express routes

### Phase 2 Checkpoint

- [ ] Create a bucket
- [ ] Upload an object
- [ ] Read object metadata
- [ ] Delete an object
- [ ] Understand private vs public files

---

# Phase 3: Presigned URLs

**Days 5–6**

**Goal:** Build direct browser → storage uploads without sending large files through your backend.

### 3.1 Presigned URL Fundamentals — Core

- [ ] What is a presigned URL?
- [ ] Why presigned URLs exist
- [ ] Backend-generated URLs
- [ ] Temporary permissions
- [ ] Expiration
- [ ] HTTP methods
- [ ] Build: Generate upload URL
- [ ] Done when: You understand the complete presigned upload flow

### 3.2 Presigned Upload Flow — Core

- [ ] Client requests upload URL
- [ ] Backend validates request
- [ ] Backend generates URL
- [ ] Browser uploads directly to storage
- [ ] Client confirms upload
- [ ] Backend stores metadata
- [ ] Build: Direct avatar upload in TaskFlow
- [ ] Done when: Large files bypass your Express server

### 3.3 Presigned Download URLs — Core

- [ ] Private file access
- [ ] Temporary download URLs
- [ ] Expiration
- [ ] Authorization before URL generation
- [ ] Build: Private document downloads
- [ ] Done when: Users can securely download private files

### 3.4 Upload Status & Confirmation — Next

- [ ] Upload initiated
- [ ] Upload completed
- [ ] Upload failed
- [ ] Upload cancelled
- [ ] File verification
- [ ] Build: Upload status system
- [ ] Done when: Your database never assumes an upload succeeded without verification

### Phase 3 Checkpoint

- [ ] Generate presigned upload URL
- [ ] Upload directly from browser
- [ ] Generate download URL
- [ ] Configure expiration
- [ ] Protect private files

---

# Phase 4: Secure File Uploads

**Days 7–8**

**Goal:** Prevent malicious, invalid, oversized, or unauthorized uploads.

### 4.1 File Validation — Core

- [ ] File size validation
- [ ] MIME type validation
- [ ] File extension validation
- [ ] Filename validation
- [ ] Content-type validation
- [ ] Allowlist strategy
- [ ] Build: Secure attachment validation
- [ ] Done when: Invalid files are rejected consistently

### 4.2 Authentication & Authorization — Core

- [ ] Authenticated uploads
- [ ] User ownership
- [ ] Resource ownership
- [ ] Role-based permissions
- [ ] Private files
- [ ] Admin access
- [ ] Build: User-owned files in TaskFlow
- [ ] Done when: Users cannot access another user's files

### 4.3 Upload Limits & Quotas — Core

- [ ] Per-file limits
- [ ] Per-user limits
- [ ] Storage quotas
- [ ] Request limits
- [ ] Upload count limits
- [ ] Rate limiting
- [ ] Build: User storage quota
- [ ] Done when: Abuse cannot easily exhaust storage

### 4.4 Secure Object Keys — Core

- [ ] Never trust user filenames
- [ ] UUID-based object keys
- [ ] User-scoped directories
- [ ] Tenant-scoped directories
- [ ] File naming strategy
- [ ] Build: Multi-user storage structure
- [ ] Done when: Object keys are predictable only where intentionally designed

### 4.5 Malware Scanning — Bonus

- [ ] Virus scanning concept
- [ ] ClamAV concept
- [ ] Third-party scanning services
- [ ] Quarantine workflow
- [ ] Scan before publishing
- [ ] Build: Attachment scanning architecture
- [ ] Done when: You understand where malware scanning belongs in production

### Phase 4 Checkpoint

- [ ] Validate file size
- [ ] Validate content type
- [ ] Authorize upload
- [ ] Protect private files
- [ ] Implement quotas
- [ ] Generate safe object keys

---

# Phase 5: Database & File Metadata

**Days 9–10**

**Goal:** Design the database layer that tracks files without storing file binaries in the database.

### 5.1 File Metadata Model — Core

- [ ] File ID
- [ ] User ID
- [ ] Original filename
- [ ] Object key
- [ ] MIME type
- [ ] File size
- [ ] Storage provider
- [ ] Storage bucket
- [ ] Status
- [ ] Created date
- [ ] Build: File model for TaskFlow
- [ ] Done when: Database contains everything needed to manage a file

### 5.2 Upload Lifecycle — Core

- [ ] Pending
- [ ] Uploading
- [ ] Completed
- [ ] Failed
- [ ] Deleted
- [ ] Quarantined
- [ ] Build: File lifecycle state machine
- [ ] Done when: File states are handled explicitly

### 5.3 File Relationships — Next

- [ ] User → files
- [ ] Project → files
- [ ] Task → attachments
- [ ] Ticket → attachments
- [ ] Message → attachments
- [ ] Build: ChatSpace message attachments
- [ ] Done when: Files can be attached to application resources

### 5.4 Orphaned Files — Core

- [ ] What are orphaned files?
- [ ] Upload succeeds but DB fails
- [ ] DB succeeds but upload fails
- [ ] Cleanup strategy
- [ ] Scheduled cleanup jobs
- [ ] Build: Orphan file cleanup
- [ ] Done when: Storage does not accumulate abandoned objects

### Phase 5 Checkpoint

- [ ] Design file metadata schema
- [ ] Implement upload states
- [ ] Connect files to application resources
- [ ] Handle failed uploads
- [ ] Clean orphaned files

---

# Phase 6: Production File Management

**Days 11–12**

**Goal:** Handle large files, performance, reliability, and production operations.

### 6.1 Large File Uploads — Core

- [ ] Streaming uploads
- [ ] Multipart uploads
- [ ] Chunked uploads
- [ ] Resume capability
- [ ] Upload progress
- [ ] Large file limits
- [ ] Build: Large document upload
- [ ] Done when: Large files don't unnecessarily consume backend memory

### 6.2 File Deletion — Core

- [ ] Soft delete
- [ ] Permanent deletion
- [ ] Storage deletion
- [ ] Database deletion
- [ ] Delete authorization
- [ ] Cleanup jobs
- [ ] Build: Secure file deletion
- [ ] Done when: Database and object storage remain consistent

### 6.3 CDN & File Delivery — Next

- [ ] CDN fundamentals
- [ ] Cache behavior
- [ ] Cache invalidation
- [ ] Public assets
- [ ] Private asset delivery
- [ ] Signed URLs
- [ ] Build: CDN-backed media delivery
- [ ] Done when: Frequently accessed files can be delivered efficiently

### 6.4 Image Processing — Next

- [ ] Image dimensions
- [ ] Image resizing
- [ ] Thumbnail generation
- [ ] Compression
- [ ] WebP / AVIF concepts
- [ ] Background processing
- [ ] Build: User avatar processing
- [ ] Done when: Uploaded images are optimized automatically

### 6.5 Background Jobs — Core

- [ ] Upload processing
- [ ] Image processing
- [ ] Malware scanning
- [ ] Cleanup jobs
- [ ] Retry logic
- [ ] BullMQ
- [ ] Build: Background file-processing pipeline
- [ ] Done when: Heavy processing doesn't block API requests

### 6.6 Monitoring & Logging — Core

- [ ] Upload success rate
- [ ] Upload failures
- [ ] Storage usage
- [ ] Processing failures
- [ ] Request duration
- [ ] Structured logs
- [ ] Alerts
- [ ] Build: File-service observability
- [ ] Done when: You can diagnose upload failures in production

### Phase 6 Checkpoint

- [ ] Handle large files
- [ ] Implement deletion
- [ ] Understand CDN delivery
- [ ] Process images asynchronously
- [ ] Add retry logic
- [ ] Monitor failures

---

# Final Phase: Production File Service

**Days 13–14**

**Goal:** Build a reusable file-upload service that can be used across your applications.

---

## Final Project: Production File Service

Build a complete reusable file service for **TaskFlow**.

### Backend

- [ ] File upload API
- [ ] Presigned upload API
- [ ] Presigned download API
- [ ] File metadata API
- [ ] File deletion API
- [ ] File listing API
- [ ] Authorization
- [ ] Validation
- [ ] Storage quotas
- [ ] Error handling
- [ ] Logging

### Storage

- [ ] S3 or Cloudflare R2
- [ ] Private bucket
- [ ] Safe object keys
- [ ] Presigned URLs
- [ ] File metadata

### Database

- [ ] File model
- [ ] User relationship
- [ ] Resource relationship
- [ ] Upload status
- [ ] Storage metadata

### Security

- [ ] Authentication
- [ ] Authorization
- [ ] File-size limits
- [ ] MIME validation
- [ ] Extension validation
- [ ] Rate limiting
- [ ] Storage quotas
- [ ] Secure object keys

### Performance

- [ ] Direct-to-storage uploads
- [ ] Streaming where appropriate
- [ ] Multipart uploads for large files
- [ ] CDN strategy
- [ ] Background processing
- [ ] Redis/BullMQ integration

### Reliability

- [ ] Failed upload handling
- [ ] Retry strategy
- [ ] Orphan cleanup
- [ ] Upload status tracking
- [ ] Background cleanup jobs
- [ ] Monitoring

---

# Integration Projects

## TaskFlow

- [ ] User avatars
- [ ] Project attachments
- [ ] Task attachments
- [ ] Private documents
- [ ] File permissions
- [ ] Storage quotas

## ChatSpace

- [ ] Image messages
- [ ] Video messages
- [ ] Voice/audio attachments
- [ ] File messages
- [ ] Upload progress
- [ ] Message attachment previews

## SupportDesk AI

- [ ] Ticket attachments
- [ ] PDF uploads
- [ ] Image attachments
- [ ] Secure customer documents
- [ ] File processing pipeline
- [ ] AI document ingestion
- [ ] Connect uploads to RAG pipeline

---

# Interview Preparation

## Core Questions

- [ ] What is object storage?
- [ ] Why use S3/R2 instead of storing files in MongoDB/PostgreSQL?
- [ ] What is multipart/form-data?
- [ ] What is a presigned URL?
- [ ] Why use presigned URLs?
- [ ] Backend upload vs direct-to-storage upload?
- [ ] What is a signed URL?
- [ ] Public vs private objects?
- [ ] How do you protect private files?
- [ ] How do you validate uploaded files?
- [ ] How do you prevent oversized uploads?
- [ ] How do you prevent malicious files?
- [ ] What are orphaned files?
- [ ] How do you handle failed uploads?
- [ ] How do you upload very large files?
- [ ] What is multipart upload?
- [ ] Why use a CDN?
- [ ] How would you design a multi-tenant file system?
- [ ] How would you implement storage quotas?
- [ ] How would you monitor file uploads?

---

# Production Checklist

### Architecture

- [ ] Object storage instead of database binaries
- [ ] Direct browser → storage uploads
- [ ] Presigned URLs
- [ ] File metadata stored in database
- [ ] Background processing

### Security

- [ ] Authentication
- [ ] Authorization
- [ ] File validation
- [ ] Size limits
- [ ] Rate limiting
- [ ] Safe object keys
- [ ] Private storage
- [ ] Expiring URLs
- [ ] Malware scanning strategy

### Performance

- [ ] Direct uploads
- [ ] Streaming
- [ ] Multipart uploads
- [ ] CDN
- [ ] Image optimization
- [ ] Background jobs

### Reliability

- [ ] Upload status
- [ ] Retry handling
- [ ] Failed upload cleanup
- [ ] Orphan cleanup
- [ ] Monitoring
- [ ] Logging
- [ ] Alerts

---

# What to Learn Next

After completing File Uploads:

1. [ ] Redis
2. [ ] BullMQ
3. [ ] PostgreSQL
4. [ ] Prisma / Drizzle
5. [ ] Docker
6. [ ] CI/CD
7. [ ] CDN fundamentals
8. [ ] Background job architecture
9. [ ] Observability
10. [ ] Security hardening

---

# Weekly Review Log

## Week 1

- [ ] Learned file upload fundamentals
- [ ] Learned object storage
- [ ] Implemented S3/R2 upload
- [ ] Implemented presigned URLs

## Week 2

- [ ] Implemented secure validation
- [ ] Added file metadata
- [ ] Added quotas
- [ ] Added cleanup
- [ ] Added background processing
- [ ] Completed production file service

---

# Completion Standard

You can mark this syllabus **COMPLETE** when you can independently build:

**React Browser**
→ **Request Presigned URL**
→ **Express API**
→ **S3 / Cloudflare R2**
→ **Upload File**
→ **Store Metadata**
→ **Process File**
→ **Authorize Access**
→ **Generate Secure Download URL**
→ **Deliver File via CDN**

And you can explain the architecture, security decisions,
failure cases, performance tradeoffs, and production concerns.
