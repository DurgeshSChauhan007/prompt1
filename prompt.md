# Car Rental Platform — MERN Stack Project Prompt

## Project Overview

Build a modern full-stack Car Rental Platform using the MERN stack that delivers a smooth, premium, and production-ready booking experience.

The platform should feel fast, responsive, and intuitive while maintaining clean architecture, reusable components, scalable APIs, and polished UI interactions.

Users should be able to:

- Browse vehicles
- Check availability
- Book rentals
- Manage profiles
- Track bookings

Owners should have access to a dedicated dashboard where they can:

- Manage vehicles
- Handle bookings
- View analytics
- Monitor platform activity

The overall experience should reflect the quality of a real-world rental platform with modern UI design, secure authentication, and seamless booking workflows.

---

# Core Features

The platform should support:

- Vehicle browsing and discovery
- Real-time availability checking
- Car booking workflow
- JWT-based authentication
- Owner-based vehicle management
- Booking history and management
- User profile management
- Dashboard analytics
- Responsive design
- Smooth animations and transitions

The application should feel:

- Modern
- Fast
- Smooth
- Secure
- Lightweight
- Scalable
- Production-ready

---

# Frontend Requirements

## Technologies

- React
- Tailwind CSS
- Framer Motion
- Axios
- React Router

## Frontend Pages & Features

- Responsive landing page
- Hero section
- Featured car showcase
- Vehicle listing page
- Vehicle details page
- Booking interface
- Owner dashboard
- User profile page
- Search and filtering system
- Animated modals and drawers
- Responsive navigation menu

---

# UI & Animation Experience

Use Framer Motion to create smooth and engaging interactions throughout the platform.

## Required Animations

- Smooth page transitions
- Animated vehicle cards
- Hover interactions
- Booking modal animations
- Dashboard transitions
- Staggered content reveals
- Loading skeletons

## Animation Guidelines

- Use transform and opacity for performance
- Avoid layout shifts
- Keep animations lightweight
- Respect reduced motion accessibility settings

The UI should feel polished without becoming overly heavy or distracting.

---

# Authentication System

Implement a secure JWT-based authentication system.

## Features

- User registration
- User login
- Protected routes
- Role-based access control

## Supported Roles

- user
- owner

## Security Requirements

- bcrypt password hashing
- JWT token validation
- Authentication middleware
- Secure route protection

---

# Backend Requirements

## Technologies

- Node.js
- Express.js
- MongoDB
- Mongoose

## Backend Architecture

- Modular folder structure
- RESTful API design
- Controller-based architecture
- Middleware separation
- Clean and maintainable codebase

The API should be scalable, readable, and easy to extend.

---

# Database Models

The platform uses only three core database models to keep the backend clean, scalable, and easy to maintain.

---

# User Model

The User model is responsible for handling authentication, account management, and role-based access control across the platform.

## Fields

- `id` — Unique MongoDB ObjectId
- `name` — Full name of the user
- `email` — Unique email address used for authentication
- `password` — Securely hashed password using bcrypt
- `role` — Defines whether the account is a `user` or an `owner`
- `image` — Profile image URL
- `createdAt` — Account creation timestamp
- `updatedAt` — Last account update timestamp

---

# Car Model

The Car model stores all vehicle listing information added by owners and used throughout the booking system.

## Fields

- `id` — Unique MongoDB ObjectId
- `owner` — Reference to the User who listed the vehicle
- `brand` — Vehicle manufacturer name
- `model` — Vehicle model name
- `image` — Vehicle image URL
- `year` — Manufacturing year
- `category` — Vehicle category such as SUV, Sedan, Sports, etc.
- `seating_capacity` — Total seating capacity
- `fuel_type` — Petrol, Diesel, Electric, or Hybrid
- `transmission` — Automatic or Manual transmission type
- `pricePerDay` — Rental price per day
- `location` — Vehicle pickup location
- `description` — Detailed vehicle information
- `isAvailable` — Availability status of the vehicle
- `createdAt` — Vehicle listing creation timestamp
- `updatedAt` — Last vehicle update timestamp

---

# Booking Model

The Booking model manages rental reservations between customers and vehicle owners.

## Fields

- `id` — Unique MongoDB ObjectId
- `car` — Reference to the booked vehicle
- `user` — Reference to the customer who made the booking
- `owner` — Reference to the vehicle owner
- `pickupDate` — Rental start date
- `returnDate` — Rental return date
- `status` — Booking status (`pending`, `confirmed`, or `cancelled`)
- `price` — Total booking amount
- `createdAt` — Booking creation timestamp
- `updatedAt` — Last booking update timestamp

---

# API Architecture

The backend should follow a clean route-controller architecture with three primary route groups:

```bash
/api/user
/api/owner
/api/bookings
```

Protected routes should use JWT middleware to validate users and attach authenticated user data to `req.user`.

---

# User Routes

## POST `/api/user/register`

Create a new user account.

### Features

- Validate input data
- Hash passwords using bcrypt
- Store users in MongoDB
- Generate JWT tokens

---

## POST `/api/user/login`

Authenticate users.

### Features

- Verify email and password
- Compare hashed passwords
- Generate JWT tokens

---

## GET `/api/user/data`

Fetch authenticated user profile data.

### Features

- Protected route
- Return logged-in user information

---

## GET `/api/user/cars`

Fetch all available vehicles.

### Features

- Return cars where `isAvailable` is true
- Used for frontend listing pages

---

# Owner Routes

## POST `/api/owner/change-role`

Upgrade a normal user to owner role.

### Features

- Change role from user to owner
- Enable vehicle listing access

---

## POST `/api/owner/add-car`

Create a new vehicle listing.

### Features

- Upload vehicle images
- Optimize images using ImageKit
- Convert images to WebP
- Store vehicle data in MongoDB

### Supported Fields

- brand
- model
- category
- transmission
- fuel_type
- seating_capacity
- pricePerDay
- location
- description

---

## GET `/api/owner/cars`

Fetch all vehicles added by the authenticated owner.

### Features

- Filter cars using `owner: req.user._id`

---

## POST `/api/owner/toggle-car`

Toggle vehicle availability.

### Features

- Update `isAvailable`
- Mark cars available or unavailable

---

## POST `/api/owner/delete-car`

Soft delete vehicle listings.

### Features

- Mark cars unavailable instead of permanently deleting

---

## GET `/api/owner/dashboard`

Fetch dashboard analytics.

### Dashboard Data

- Total cars
- Total bookings
- Pending bookings
- Completed bookings
- Monthly revenue
- Recent bookings

---

## POST `/api/owner/update-image`

Update profile images.

### Features

- Upload images
- Optimize images
- Convert images to WebP

---

# Booking Routes

## POST `/api/bookings/check-availability`

Check whether cars are available for selected dates.

### Features

- Prevent overlapping bookings
- Validate booking dates
- Filter available cars by location

---

## POST `/api/bookings/create`

Create a booking.

### Features

- Validate vehicle availability
- Calculate rental duration
- Calculate total booking price
- Store booking data in MongoDB

### Pricing Formula

```txt
pricePerDay × totalDays
```

---

## GET `/api/bookings/user`

Fetch booking history for authenticated users.

### Features

- Populate booked car details
- Sort latest bookings first

---

## GET `/api/bookings/owner`

Fetch bookings related to owner-listed vehicles.

### Features

- Populate vehicle details
- Populate customer details
- Accessible only for owners

---

## POST `/api/bookings/change-status`

Update booking status.

### Supported Statuses

- pending
- confirmed
- cancelled

### Features

- Only the vehicle owner can update status

---

# Middleware Architecture

## protect Middleware

Handles:

- JWT verification
- Protected routes
- Authentication validation
- Attaching user data to `req.user`

---

## upload Middleware

Handles:

- Multipart uploads
- Vehicle image uploads
- Profile image uploads
- Multer configuration

---

# Payment Architecture

Prepare the platform for future payment integration using:

- Stripe
- Razorpay

## Planned Payment Features

- Secure checkout
- Payment tracking
- Refund handling
- Webhook processing

---

# Performance & Scalability

Optimize the platform for:

- Fast page loading
- Smooth animations
- Efficient API responses
- Optimized image delivery
- Reduced bundle size

## Optimization Techniques

- Lazy loading
- Dynamic imports
- Debounced searches
- Image optimization

The platform should support:

- High traffic
- Concurrent bookings
- CDN-ready deployment
- Horizontal scaling

---

# Accessibility & SEO

Ensure the platform is:

- Fully responsive
- Keyboard accessible
- Screen-reader friendly
- SEO optimized

## Include

- Semantic HTML
- ARIA labels
- Open Graph metadata
- Proper heading hierarchy

---

# Recommended Tech Stack

## Frontend

- React
- Tailwind CSS
- Framer Motion
- shadcn/ui
- React Hook Form
- Zod

## Backend

- Node.js
- Express.js
- JWT Authentication
- Nodemailer

## Database

- MongoDB

## Optional Services

- Redis
- Cloudinary
- AWS S3
- Docker

---

# Final Deliverables

The completed project should include:

- Premium responsive UI
- Smooth motion-based interactions
- Secure authentication system
- Vehicle booking workflow
- Owner dashboard
- RESTful backend APIs
- Database integration
- Proper error handling
- Production-ready architecture

---

# Documentation

Include documentation for:

- Folder structure
- API architecture
- Database schema
- Environment variables
- Deployment setup
- Authentication flow
- Animation system

---

# Deployment

The project should be deployable on:

- Vercel
- Render
- Railway
- Docker containers

---
