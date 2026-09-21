# Stripe (Checkout, Subscriptions, Webhooks) Syllabus

**Level:** Intermediate → Production
**Total time:** 14 days
**Prerequisites:** TypeScript, React, Node.js, Express, REST APIs, authentication, MongoDB/PostgreSQL basics
**Progress:** 0 / 28 topics done

---

## Skip for now

- [ ] Stripe Connect marketplace payments
- [ ] Multi-party payouts
- [ ] Stripe Issuing
- [ ] Stripe Treasury
- [ ] Stripe Terminal
- [ ] Advanced tax automation
- [ ] Complex international payment regulations
- [ ] Building your own payment processor
- [ ] Deep Stripe API internals
- [ ] Advanced accounting integrations

---

# Phase 1: Payment Fundamentals & Stripe Setup

**Days:** 1–2
**Goal:** Understand Stripe's payment architecture and safely connect it to a full-stack application.
**Done when:** I can explain the complete payment flow from frontend → backend → Stripe → webhook → database.

### 1.1 Stripe Architecture

- [ ] **Stripe Payment Architecture** (Core)
- [ ] Concept: Understand customers, products, prices, checkout sessions, payments, invoices, subscriptions, and webhooks.
- [ ] Build: TaskFlow — map the complete SaaS payment architecture.
- [ ] Done when: I can explain how every Stripe object is related.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/

### 1.2 Stripe Account & Test Mode

- [ ] **Stripe Account & Test Mode** (Core)
- [ ] Concept: Understand test mode, API keys, publishable keys, secret keys, and test data.
- [ ] Build: TaskFlow — configure Stripe test mode.
- [ ] Done when: Backend can securely communicate with Stripe.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/keys

### 1.3 Stripe SDK

- [ ] **Stripe Node.js SDK** (Core)
- [ ] Concept: Learn how to initialize Stripe and call Stripe APIs from the backend.
- [ ] Build: TaskFlow — create a Stripe service module.
- [ ] Done when: Stripe API calls are isolated from controllers.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/sdks

### 1.4 Products & Prices

- [ ] **Products & Prices** (Core)
- [ ] Concept: Understand the difference between products and prices and how recurring prices work.
- [ ] Build: TaskFlow — create:
  - Free plan
  - Pro plan
  - Business plan
- [ ] Done when: Each plan has a correctly configured Stripe Price ID.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/products-prices

### Phase 1 Checkpoint

- [ ] Create Stripe test account
- [ ] Configure environment variables
- [ ] Install Stripe SDK
- [ ] Create products
- [ ] Create prices
- [ ] Connect backend to Stripe
- [ ] Explain Stripe's core objects from memory

---

# Phase 2: Stripe Checkout

**Days:** 3–5
**Goal:** Build a complete Stripe Checkout payment flow.
**Done when:** A user can select a plan and complete a test payment without exposing secret Stripe credentials to the frontend.

### 2.1 Checkout Sessions

- [ ] **Checkout Session** (Core)
- [ ] Concept: Understand what a Checkout Session represents and how Stripe hosts the payment page.
- [ ] Build: TaskFlow — create a Checkout Session from the backend.
- [ ] Done when: Backend returns a valid Stripe Checkout URL.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/api/checkout/sessions

### 2.2 Checkout Frontend Flow

- [ ] **Frontend → Backend → Checkout** (Core)
- [ ] Concept: Understand why secret Stripe operations belong on the backend.
- [ ] Build: TaskFlow — React pricing page → Express endpoint → Stripe Checkout.
- [ ] Done when: User can click "Upgrade" and reach Checkout.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/checkout/quickstart

### 2.3 Success & Cancel URLs

- [ ] **Checkout Success & Cancel Flow** (Core)
- [ ] Concept: Understand redirect URLs and why a success page alone is not proof of payment.
- [ ] Build: TaskFlow — create success and cancel pages.
- [ ] Done when: Users return to the correct page after Checkout.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/payments/checkout

### 2.4 Customer Creation

- [ ] **Stripe Customers** (Core)
- [ ] Concept: Understand Stripe Customer objects and linking them to application users.
- [ ] Build: TaskFlow — create/store a Stripe Customer ID for each paying user.
- [ ] Done when: Your user record and Stripe Customer remain correctly linked.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/api/customers

### 2.5 Checkout Metadata

- [ ] **Checkout Metadata** (Core)
- [ ] Concept: Understand metadata for connecting Stripe events to your application's users/workspaces.
- [ ] Build: TaskFlow — attach `userId` and `workspaceId` to Checkout metadata.
- [ ] Done when: A webhook can identify the correct application user/workspace.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/metadata

### 2.6 Checkout Security

- [ ] **Checkout Security** (Core)
- [ ] Concept: Understand server-side price validation and why clients must not control final prices.
- [ ] Build: TaskFlow — accept only trusted plan IDs and retrieve price information server-side.
- [ ] Done when: A modified frontend request cannot change the subscription price.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/security

### Phase 2 Checkpoint

- [ ] Pricing page
- [ ] Backend Checkout endpoint
- [ ] Stripe Customer
- [ ] Stripe Price
- [ ] Checkout Session
- [ ] Metadata
- [ ] Success page
- [ ] Cancel page
- [ ] Server-side price validation
- [ ] Complete test payment

---

# Phase 3: Subscriptions

**Days:** 6–9
**Goal:** Build a production-style SaaS subscription system.
**Done when:** TaskFlow can create, track, change, cancel, and recover subscriptions.

### 3.1 Subscription Lifecycle

- [ ] **Subscription Lifecycle** (Core)
- [ ] Concept: Understand trialing, active, past_due, unpaid, canceled, and incomplete states.
- [ ] Build: TaskFlow — create a subscription lifecycle diagram.
- [ ] Done when: I can explain what should happen for each important state.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/billing/subscriptions/overview

### 3.2 Create Subscription

- [ ] **Create Subscription** (Core)
- [ ] Concept: Understand how Checkout creates a subscription for a recurring Price.
- [ ] Build: TaskFlow — implement Pro subscription checkout.
- [ ] Done when: A successful Checkout creates a Stripe Subscription.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/billing/subscriptions/overview

### 3.3 Store Subscription Data

- [ ] **Subscription Database Model** (Core)
- [ ] Concept: Decide which Stripe identifiers and subscription state your application needs.
- [ ] Build: TaskFlow — create a subscription collection/table containing:
  - `userId`
  - `stripeCustomerId`
  - `stripeSubscriptionId`
  - `stripePriceId`
  - `status`
  - `currentPeriodEnd`
- [ ] Done when: Your database can represent the user's current billing state.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/billing/subscriptions/overview

### 3.4 Subscription Access Control

- [ ] **Subscription-Based Feature Access** (Core)
- [ ] Concept: Connect billing state with application permissions.
- [ ] Build: TaskFlow — restrict Pro features to active/trialing subscribers.
- [ ] Done when: Users without the required subscription cannot use Pro features.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Stripe Billing docs

### 3.5 Upgrade & Downgrade

- [ ] **Change Subscription Price** (Core)
- [ ] Concept: Understand changing subscription items/prices and proration.
- [ ] Build: TaskFlow — implement Pro → Business and Business → Pro.
- [ ] Done when: The Stripe subscription and local database stay synchronized.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/billing/subscriptions/change-price
- Verify current Stripe behavior in official docs.

### 3.6 Cancel Subscription

- [ ] **Subscription Cancellation** (Core)
- [ ] Concept: Understand immediate cancellation vs cancel-at-period-end.
- [ ] Build: TaskFlow — implement "Cancel at end of billing period."
- [ ] Done when: The user keeps access until the correct subscription end date.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/billing/subscriptions/cancel

### 3.7 Billing Portal

- [ ] **Stripe Customer Portal** (Next) | ~2h
- [ ] Concept: Understand how Stripe can handle common customer billing management tasks.
- [ ] Build: TaskFlow — add a "Manage Billing" button.
- [ ] Done when: Users can access their Stripe-hosted billing portal.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/customer-management

### Phase 3 Checkpoint

- [ ] Create subscription
- [ ] Store subscription data
- [ ] Display current plan
- [ ] Protect paid features
- [ ] Upgrade
- [ ] Downgrade
- [ ] Cancel
- [ ] Cancel at period end
- [ ] Billing Portal

---

# Phase 4: Stripe Webhooks

**Days:** 10–12
**Goal:** Build reliable server-side synchronization using Stripe webhooks.
**Done when:** Your application does not depend on browser redirects to determine payment status.

### 4.1 Webhook Fundamentals

- [ ] **Stripe Webhooks** (Core)
- [ ] Concept: Understand event-driven communication between Stripe and your backend.
- [ ] Build: TaskFlow — create a webhook endpoint.
- [ ] Done when: Your backend receives Stripe test events.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/webhooks

### 4.2 Webhook Signature Verification

- [ ] **Webhook Signature Verification** (Core)
- [ ] Concept: Verify that webhook requests actually came from Stripe.
- [ ] Build: TaskFlow — verify the Stripe webhook signature before processing events.
- [ ] Done when: Invalid webhook signatures are rejected.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/webhooks/signature
- Verify current implementation requirements in official docs.

### 4.3 Important Billing Events

- [ ] **Subscription Webhook Events** (Core)
- [ ] Concept: Understand important events such as:
  - `checkout.session.completed`
  - `customer.subscription.created`
  - `customer.subscription.updated`
  - `customer.subscription.deleted`
  - `invoice.paid`
  - `invoice.payment_failed`
- [ ] Build: TaskFlow — map each event to a database action.
- [ ] Done when: I know which events affect access and billing state.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/webhooks

### 4.4 Webhook Database Sync

- [ ] **Stripe → Database Synchronization** (Core)
- [ ] Concept: Treat Stripe events as the source of billing events and synchronize local state.
- [ ] Build: TaskFlow — update subscription records from webhook events.
- [ ] Done when: Local subscription state updates without relying on frontend redirects.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/billing/subscriptions/webhooks

### 4.5 Idempotent Webhooks

- [ ] **Webhook Idempotency** (Core)
- [ ] Concept: Understand duplicate events and why webhook handlers must safely process an event more than once.
- [ ] Build: TaskFlow — store processed Stripe event IDs.
- [ ] Done when: Processing the same event twice does not duplicate or corrupt data.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/webhooks

### 4.6 Webhook Failure & Retry

- [ ] **Webhook Reliability** (Core)
- [ ] Concept: Understand failed webhook processing, retries, timeouts, and safe event handling.
- [ ] Build: TaskFlow — intentionally fail webhook processing and test recovery.
- [ ] Done when: Failed events can be retried without corrupting billing state.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/webhooks
- Verify current retry behavior in official Stripe docs.

### Phase 4 Checkpoint

- [ ] Webhook endpoint
- [ ] Signature verification
- [ ] Event parsing
- [ ] Subscription events
- [ ] Payment events
- [ ] Database synchronization
- [ ] Event ID tracking
- [ ] Idempotency
- [ ] Retry handling
- [ ] Local webhook testing

---

# Phase 5: Production Billing

**Days:** 13–14
**Goal:** Turn the Stripe implementation into a reliable production billing system.
**Done when:** I can test payment failures, subscription changes, webhook failures, and deployment configuration.

### 5.1 Failed Payments

- [ ] **Payment Failure Handling** (Core)
- [ ] Concept: Understand failed invoices, payment retries, and subscription state changes.
- [ ] Build: TaskFlow — handle failed subscription payments.
- [ ] Done when: The user's billing state changes correctly after payment failure.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/billing/subscriptions/overview

### 5.2 Subscription Access States

- [ ] **Billing State → Application Access** (Core)
- [ ] Concept: Define exactly what application access means for each subscription state.
- [ ] Build: TaskFlow — create access rules for active, trialing, past_due, canceled, and unpaid states.
- [ ] Done when: Access behavior is predictable for every important state.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: Search official Stripe Billing docs
- Verify current subscription states in official docs.

### 5.3 Stripe Idempotency

- [ ] **API Idempotency** (Core)
- [ ] Concept: Prevent duplicate Stripe operations when requests are retried.
- [ ] Build: TaskFlow — use idempotency keys for appropriate create/update operations.
- [ ] Done when: A retried request does not accidentally create duplicate billing operations.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/api/idempotent_requests

### 5.4 Billing Security

- [ ] **Stripe Security** (Core)
- [ ] Concept: Protect secret keys, validate server-side input, verify webhooks, and avoid trusting client payment state.
- [ ] Build: TaskFlow — perform a billing security audit.
- [ ] Done when: No Stripe secret or billing decision is controlled only by the browser.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/security

### 5.5 Testing Stripe

- [ ] **Stripe Test Mode & Test Scenarios** (Core)
- [ ] Concept: Test successful payments, failed payments, subscriptions, cancellations, and webhook events.
- [ ] Build: TaskFlow — create a billing test checklist.
- [ ] Done when: Critical billing scenarios can be reproduced in test mode.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/testing

### 5.6 Production Webhook Deployment

- [ ] **Production Webhooks** (Core)
- [ ] Concept: Configure production webhook endpoints, secrets, HTTPS, monitoring, and event handling.
- [ ] Build: TaskFlow — deploy the webhook endpoint.
- [ ] Done when: Stripe production/test events can reach the deployed backend correctly.
- [ ] Note written in dev-notes
- [ ] Recall test after 1 day / 3 days / 7 days
- Docs: https://docs.stripe.com/webhooks
- Verify current Stripe Dashboard configuration in official docs.

### Phase 5 Checkpoint

- [ ] Successful payment
- [ ] Failed payment
- [ ] Subscription update
- [ ] Subscription cancellation
- [ ] Webhook retry
- [ ] Duplicate webhook
- [ ] Idempotent API request
- [ ] Production webhook
- [ ] Security audit
- [ ] Test-mode billing scenarios

---

# Final Phase: Prove It

## Mini-Project: TaskFlow SaaS Billing

- [ ] Pricing page
- [ ] Free plan
- [ ] Pro plan
- [ ] Business plan
- [ ] Stripe Products
- [ ] Stripe Prices
- [ ] Stripe Customers
- [ ] Checkout Sessions
- [ ] Subscription creation
- [ ] Subscription database model
- [ ] Subscription status
- [ ] Upgrade
- [ ] Downgrade
- [ ] Cancel subscription
- [ ] Cancel at period end
- [ ] Stripe Customer Portal
- [ ] Checkout success page
- [ ] Checkout cancel page
- [ ] Webhook endpoint
- [ ] Webhook signature verification
- [ ] Webhook event processing
- [ ] Idempotent webhook handling
- [ ] Payment failure handling
- [ ] Subscription access control
- [ ] API idempotency
- [ ] Test-mode scenarios
- [ ] Production webhook deployment

---

## 10 Interview Questions

- [ ] What is Stripe Checkout?
- [ ] What is a Stripe Customer?
- [ ] What is the difference between a Product and a Price?
- [ ] What is a Checkout Session?
- [ ] How does a Stripe subscription work?
- [ ] Why should you use webhooks?
- [ ] Why can't a success URL be trusted as proof of payment?
- [ ] What is webhook signature verification?
- [ ] What is webhook idempotency?
- [ ] How would you synchronize Stripe subscription state with your database?

---

## Production Checklist

### Security

- [ ] Stripe secret key exists only on the backend
- [ ] Publishable key is used only where appropriate
- [ ] Prices are validated server-side
- [ ] Users cannot control Stripe Price IDs arbitrarily
- [ ] Webhook signatures are verified
- [ ] Webhook secrets are stored securely
- [ ] Payment status is not trusted from the frontend
- [ ] Sensitive Stripe data is not logged
- [ ] HTTPS is enabled
- [ ] Environment variables are configured correctly

### Webhooks

- [ ] Webhook endpoint exists
- [ ] Signature verification works
- [ ] Events are validated
- [ ] Important events are handled
- [ ] Duplicate events are safe
- [ ] Event IDs are tracked
- [ ] Failed events can be retried
- [ ] Webhook processing is monitored

### Subscriptions

- [ ] Subscription status is stored
- [ ] Stripe Customer ID is stored
- [ ] Stripe Subscription ID is stored
- [ ] Stripe Price ID is stored
- [ ] Subscription period is stored
- [ ] Upgrade works
- [ ] Downgrade works
- [ ] Cancellation works
- [ ] Payment failures are handled
- [ ] Application access follows billing state

### Testing

- [ ] Successful Checkout
- [ ] Failed payment
- [ ] Subscription creation
- [ ] Subscription update
- [ ] Subscription cancellation
- [ ] Duplicate webhook
- [ ] Invalid webhook signature
- [ ] Webhook failure/retry
- [ ] Unauthorized billing request
- [ ] Modified client price request

### Deployment

- [ ] Stripe test mode verified
- [ ] Production Stripe keys configured
- [ ] Production webhook endpoint configured
- [ ] Production webhook secret configured
- [ ] HTTPS enabled
- [ ] Logs configured
- [ ] Error monitoring configured
- [ ] Billing events monitored
- [ ] Current Stripe API/documentation behavior verified before production deployment

---

# What to Learn Next

- [ ] Payment security
- [ ] Stripe Payment Intents
- [ ] Stripe Elements
- [ ] Refunds
- [ ] Invoices
- [ ] Coupons & promotion codes
- [ ] Trials
- [ ] Usage-based billing
- [ ] Metered billing
- [ ] Stripe Tax (Next)
- [ ] Stripe Connect (Bonus)
- [ ] Marketplace payouts (Bonus)
- [ ] Advanced billing analytics (Bonus)

---

# Weekly Review Log

| Week | Topics finished | What I forgot | Fix |
|------|-----------------|---------------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |
