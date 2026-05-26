# Modern Car Rental Platform

A modern full-stack Car Rental Platform built with the MERN stack, designed to deliver a smooth, secure, and production-ready booking experience.

The platform allows users to browse vehicles, check availability, book rentals, manage bookings, and update profiles. Vehicle owners can manage listings, handle reservations, and monitor platform analytics through a dedicated dashboard.

---

# Features

## User Features

* Browse available vehicles
* Search and filter cars
* View detailed vehicle information
* Check real-time availability
* Book rental vehicles
* View booking history
* Manage user profile
* Responsive experience across devices

## Owner Features

* Upgrade from user to owner role
* Add and manage vehicle listings
* Toggle vehicle availability
* View owner dashboard analytics
* Manage customer bookings
* Update profile image

## Platform Features

* JWT authentication
* Role-based access control
* Secure password hashing with bcrypt
* RESTful API architecture
* Responsive UI design
* Smooth Framer Motion animations
* Optimized image handling
* Lightweight scalable backend

---

# Tech Stack

## Frontend

* React
* Tailwind CSS
* Framer Motion
* Axios
* React Router
* React Hook Form
* Zod
* shadcn/ui

## Backend

* Node.js
* Express.js
* MongoDB
* Mongoose
* JWT Authentication
* bcrypt
* Multer
* Nodemailer

## Optional Services

* ImageKit
* Cloudinary
* Redis
* AWS S3
* Docker
* Stripe
* Razorpay

---

# Project Structure

```bash
car-rental-app/
│
├── client/                     
│   ├── src/
│   │   ├── components/         
│   │   ├── pages/             
│   │   ├── context/            
│   │   ├── assets/             
│   │   ├── App.js              
│   │   ├── index.js            
│   │
│   └── package.json
│
├── server/                    
│   ├── controllers/           
│   ├── routes/                 
│   ├── models/                 
│   ├── middleware/            
│   ├── .env                    
│   ├── index.js                
│   └── package.json
│
└── README.md
```

# Database Models

The backend uses only three core database models.

## User Model

Handles authentication and user account management.

### Fields

* `id`
* `name`
* `email`
* `password`
* `role`
* `image`
* `createdAt`
* `updatedAt`

---

## Car Model

Stores vehicle listing information.

### Fields

* `id`
* `owner`
* `brand`
* `model`
* `image`
* `year`
* `category`
* `seating_capacity`
* `fuel_type`
* `transmission`
* `pricePerDay`
* `location`
* `description`
* `isAvailable`
* `createdAt`
* `updatedAt`

---

## Booking Model

Handles rental reservations.

### Fields

* `id`
* `car`
* `user`
* `owner`
* `pickupDate`
* `returnDate`
* `status`
* `price`
* `createdAt`
* `updatedAt`

---

# API Routes

## User Routes

```bash
POST   /api/user/register
POST   /api/user/login
GET    /api/user/data
GET    /api/user/cars
```

## Owner Routes

```bash
POST   /api/owner/change-role
POST   /api/owner/add-car
GET    /api/owner/cars
POST   /api/owner/toggle-car
POST   /api/owner/delete-car
GET    /api/owner/dashboard
POST   /api/owner/update-image
```

## Booking Routes

```bash
POST   /api/bookings/check-availability
POST   /api/bookings/create
GET    /api/bookings/user
GET    /api/bookings/owner
POST   /api/bookings/change-status
```

---

# Authentication

The platform uses JWT-based authentication.

## Features

* User registration
* User login
* Protected routes
* Role-based access control
* Secure password hashing
* Token validation middleware

---

# UI & Animations

Framer Motion is used throughout the application to create a premium user experience.

## Included Animations

* Smooth page transitions
* Animated car cards
* Hover effects
* Modal animations
* Dashboard transitions
* Loading skeletons
* Staggered content reveals

---

# Performance Optimizations

The platform is optimized for scalability and smooth performance.

## Optimization Techniques

* Lazy loading
* Dynamic imports
* Debounced searches
* Optimized image delivery
* Reduced bundle sizes
* CDN-ready deployment

---

# Accessibility & SEO

The platform follows modern accessibility and SEO practices.

## Included

* Semantic HTML
* Keyboard accessibility
* ARIA labels
* Proper heading hierarchy
* Open Graph metadata
* Responsive layouts

---

# Environment Variables

Create a `.env` file inside the server folder.

```env
PORT=5000
MONGODB_URI=your_mongodb_uri
JWT_SECRET=your_jwt_secret
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_URL_ENDPOINT=your_url_endpoint
```

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
```

## Install Frontend Dependencies

```bash
cd client
npm install
```

## Install Backend Dependencies

```bash
cd server
npm install
```

---

# Run Development Server

## Start Backend

```bash
npm run server
```

## Start Frontend

```bash
npm run dev
```

---

# Deployment

The project can be deployed using:

* Vercel
* Render
* Railway
* Docker

---

# Future Improvements

* Stripe integration
* Razorpay integration
* Real-time notifications
* Wishlist functionality
* Review and rating system
* Redis caching
* Admin dashboard
* Multi-image vehicle gallery

---

# Final Goal

The goal of this project is to build a scalable and production-ready car rental platform that combines modern UI design, secure authentication, optimized backend architecture, and a smooth booking experience.
