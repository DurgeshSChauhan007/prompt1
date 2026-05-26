# Full Stack Car Rental Platform

## Context and Role

As a Full Stack Developer specializing in modern scalable web applications, you are responsible for designing and implementing a high-performance Car Rental Platform that delivers a premium booking experience using modern UI/UX principles, motion-driven interactions, and scalable backend architecture.

The platform must provide a seamless vehicle browsing and reservation experience using Framer Motion for immersive animations while maintaining accessibility, responsiveness, security, and production-level engineering standards.

The system must support:

* Vehicle discovery
* Real-time booking workflows
* User authentication
* Payment-ready architecture
* Fleet management
* Admin dashboard
* Secure contact and inquiry handling
* Scalable backend APIs

---

# Project Overview

The platform should support:

* Vehicle browsing and discovery
* Real-time booking workflows
* User authentication and authorization
* Secure inquiry/contact handling
* Payment-ready architecture
* Fleet and booking management
* Admin dashboard
* Scalable backend APIs
* Responsive modern UI

---

# Frontend

Create a premium user experience with smooth interactions and motion-driven UI.

## Use Framer Motion for:

* Smooth page transitions
* Animated vehicle cards
* Modal and drawer animations
* Booking step transitions
* Staggered content reveals
* Availability indicators
* Loading skeletons

## Animations should:

* Feel modern and cinematic
* Stay smooth at 60fps
* Use performant properties like transform and opacity
* Respect reduced motion accessibility settings
* Avoid scroll lag or layout shifts

---

# Website Sections

# Landing Page

Include:

* Hero section with strong visuals
* Featured vehicle showcase
* Search and booking CTA
* Popular rental destinations
* Customer testimonials
* Smooth scroll transitions

---

# Vehicle Listing Page

Users should be able to:

* Search vehicles
* Filter by category
* Sort by price or popularity
* View real-time availability

## Each vehicle card should display:

* Brand and model
* Price per day
* Fuel type
* Transmission
* Seat capacity
* Rating
* Location
* Vehicle image

Add hover animations and smooth interactions.

---

# Vehicle Details Page

Include:

* Animated image gallery
* Vehicle specifications
* Pricing breakdown
* Availability calendar
* Booking widget
* Similar vehicle recommendations

---

# Booking Flow

The booking process should feel simple and polished.

Include:

* Pickup and drop-off selection
* Date and time pickers
* Pricing summary
* Insurance options
* Coupon support
* Smooth multi-step animations

---

# User Dashboard

Allow users to:

* View booking history
* Manage active rentals
* Save favorite vehicles
* Update profile details
* Track payment history

---

# Admin Dashboard

Admins and fleet managers should be able to:

* Manage vehicles
* Track bookings
* Manage users
* Monitor revenue analytics
* Handle maintenance schedules
* Update vehicle availability

---

# Contact & Inquiry System

Clicking “Get in Touch” or “Book Now” should open an animated modal form.

## The form should collect:

* Full name
* Email
* Phone number
* Pickup location
* Drop-off location

## Optional:

* Preferred vehicle
* Additional message/request

Use smooth modal entrance and exit animations with Framer Motion.

---

# Authentication & Security

Implement secure authentication using:

* JWT authentication
* Role-based access control
* Secure password hashing
* Session handling

## Roles should include:

* Customer
* Admin
* Fleet Manager

Protect the application against:

* XSS attacks
* Injection attacks
* Spam submissions
* API abuse

## Use:

* Helmet.js
* Input sanitization
* API validation
* Rate limiting
* Secure headers

## Validate:

* Emails
* Phone numbers
* Booking dates

---

# Backend Requirements

Build scalable backend APIs using:

* Node.js + Express

OR

* Next.js API routes

## Architecture should follow:

* Modular structure
* RESTful API design
* Clean separation of concerns
* Production-ready scalability

---

# Database Models

# User

* id
* name
* email
* phone
* passwordHash
* role
* createdAt

---

# Vehicle

* id
* brand
* model
* year
* category
* transmission
* fuelType
* seats
* pricePerDay
* mileage
* images
* status
* locationId

---

# Booking

* id
* userId
* vehicleId
* pickupLocation
* dropoffLocation
* pickupDate
* returnDate
* bookingStatus
* totalAmount
* paymentStatus

---

# Payment

* id
* bookingId
* transactionId
* paymentProvider
* amount
* currency
* paymentStatus

---

# Maintenance

* id
* vehicleId
* serviceType
* serviceDate
* nextServiceDate
* notes

---

# Contact Inquiry

* id
* name
* email
* phone
* message
* createdAt

---

# Email & Notifications

Automatically send emails for:

* Booking confirmations
* Inquiry submissions
* Rental reminders
* Payment receipts

## Emails should include:

* Customer details
* Booking details
* Vehicle information
* Timestamp

## Use:

* Nodemailer
* SMTP provider or email API

Store credentials securely using environment variables.

---

# Payment Architecture

Prepare the platform for:

* Stripe
* Razorpay

## Include support for:

* Secure checkout
* Payment tracking
* Refund handling
* Webhook processing

---

# Performance & Scalability

Optimize the application for production use.

## Focus on:

* Fast page loads
* Optimized API responses
* Smooth animations
* Efficient image loading
* Reduced bundle sizes

## Use:

* Lazy loading
* Dynamic imports
* Image optimization
* Debounced searches

The system should support:

* High traffic
* Concurrent bookings
* CDN-ready deployments
* Horizontal scaling

---

# Accessibility & SEO

Ensure the platform is:

* Fully responsive
* Keyboard accessible
* Screen-reader friendly
* SEO optimized

## Include:

* Semantic HTML
* ARIA labels
* Open Graph metadata
* Proper heading structure

---

# Recommended Tech Stack

# Frontend

* React
* Framer Motion
* Tailwind CSS
* shadcn/ui
* React Hook Form
* Zod

---

# Backend

* Node.js
* Express.js or Next.js API routes
* Prisma ORM
* JWT Authentication
* Nodemailer

---

# Database

## Preferred:

* PostgreSQL

## Alternative:

* MongoDB

---

# Optional Services

* Redis
* Cloudinary
* AWS S3
* Docker

---

# Final Deliverables

The finished platform should include:

* Premium responsive UI
* Motion-enhanced user experience
* Functional authentication system
* Vehicle booking workflow
* Admin dashboard
* Email notification system
* Secure APIs
* Database integration
* Error handling
* Production-ready structure

---

# Documentation

Include documentation for:

* Folder structure
* API architecture
* Database schema
* Environment variables
* Deployment setup
* Animation architecture
* Authentication flow
* State management

---

# Deployment

The project should be deployable on:

* Vercel
* Docker containers

## Ensure:

* Production optimization
* Environment-based configuration
* Scalable deployment setup
