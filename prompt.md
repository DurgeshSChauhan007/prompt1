# Modern Car Rental Platform — MERN Stack Project Prompt

## Context and Role

As a Full Stack MERN Developer, your task is to build a modern Car Rental Platform with a premium responsive frontend, secure backend APIs, JWT authentication, owner-based vehicle management, and a lightweight booking workflow system.

The platform should provide a smooth vehicle browsing and booking experience while maintaining clean architecture, reusable components, scalable APIs, and modern motion-driven UI interactions.

The project should follow a real-world MERN stack architecture inspired by production-ready car rental applications while keeping the backend simple and maintainable using only three database models:

- User
- Car
- Booking

---

# Project Overview

The platform should support:

- Vehicle browsing
- Vehicle availability checking
- Vehicle booking workflows
- JWT authentication
- Owner-based car listings
- Booking management
- User profile management
- Dashboard analytics
- Responsive UI design
- Motion-enhanced interactions

The application should feel:

- Fast
- Smooth
- Modern
- Lightweight
- Secure
- Production-ready

---

# Frontend Requirements

Build the frontend using:

- React
- Tailwind CSS
- Framer Motion
- Axios
- React Router

---

# Frontend Features

The frontend should include:

- Responsive landing page
- Hero section
- Featured vehicle showcase
- Vehicle listing page
- Vehicle details page
- Booking interface
- Owner dashboard
- User profile page
- Animated modals
- Responsive navigation
- Search and filter functionality

---

# Motion & UI Experience

Use Framer Motion for:

- Smooth page transitions
- Animated vehicle cards
- Hover interactions
- Booking modal animations
- Loading skeletons
- Dashboard animations
- Staggered content reveals

Animations should:

- Use transform and opacity
- Avoid layout shifts
- Maintain smooth performance
- Respect reduced motion accessibility settings

---

# Authentication System

Implement secure JWT authentication.

Features should include:

- User registration
- User login
- Protected routes
- Role-based access

Supported roles:

- user
- owner

Security features:

- bcrypt password hashing
- JWT token validation
- Protected API middleware
- Secure authentication flow

---

# Backend Requirements

Build backend APIs using:

- Node.js
- Express.js
- MongoDB
- Mongoose

The backend should follow:

- Modular architecture
- RESTful API structure
- Controller-based logic
- Middleware separation
- Clean folder structure

---

# Database Models

The backend should use only three database models.

---

## User Model

The User model should handle authentication and account management.

Fields:

- id → MongoDB ObjectId
- name → User full name
- email → Unique email address
- password → Hashed password using bcrypt
- role → user or owner
- image → User profile image URL
- createdAt → Account creation timestamp
- updatedAt → Account update timestamp

---

## Car Model

The Car model should store rental vehicle information.

Fields:

- id → MongoDB ObjectId
- owner → Reference to User model
- brand → Vehicle manufacturer
- model → Vehicle model
- image → Vehicle image URL
- year → Manufacturing year
- category → SUV, Sedan, Sports, etc.
- seating_capacity → Number of seats
- fuel_type → Petrol, Diesel, Electric
- transmission → Automatic or Manual
- pricePerDay → Daily rental price
- location → Vehicle location
- description → Vehicle details
- isAvaliable → Availability status
- createdAt → Vehicle creation timestamp
- updatedAt → Vehicle update timestamp

---

## Booking Model

The Booking model should manage rental reservations.

Fields:

- id → MongoDB ObjectId
- car → Reference to Car model
- user → Reference to User model
- owner → Reference to User model
- pickupDate → Rental start date
- returnDate → Rental end date
- status → pending, confirmed, cancelled
- price → Total booking amount
- createdAt → Booking creation timestamp
- updatedAt → Booking update timestamp

---
