# 🚘 Velocity Rentals — Full Stack Car Rental Platform

A premium full-stack Car Rental Platform built with modern scalable architecture, cinematic UI/UX, secure backend engineering, and motion-driven interactions.

This platform delivers a high-performance luxury vehicle booking experience using React, Framer Motion, Node.js, Prisma, PostgreSQL, JWT authentication, and production-grade deployment architecture.

---

# ✨ Core Features

## Customer Features

* Premium animated landing page
* Real-time vehicle discovery
* Smart vehicle search and filtering
* Vehicle detail pages with gallery and specifications
* Multi-step booking workflow
* Real-time booking availability
* Secure authentication and authorization
* User dashboard and booking history
* Favorite vehicle management
* Payment-ready checkout system
* Responsive mobile-first experience
* Contact and inquiry system
* Email notifications and booking receipts

---

## Admin Features

* Admin dashboard analytics
* Fleet management system
* Booking management
* Vehicle availability management
* Revenue tracking
* Maintenance scheduling
* User management
* Role-based administrative control

---

# 🧠 Tech Stack

## Frontend

* React
* Next.js (Optional)
* Tailwind CSS
* Framer Motion
* shadcn/ui
* React Hook Form
* Zod Validation

---

## Backend

* Node.js
* Express.js
* Prisma ORM
* JWT Authentication
* Nodemailer
* RESTful APIs

---

## Database

### Preferred

* PostgreSQL

### Alternative

* MongoDB

---

## Optional Infrastructure

* Redis
* Docker
* Cloudinary
* AWS S3
* CDN Integration
* Vercel Deployment

---

# 🎬 Motion & Animation System

The platform uses Framer Motion for cinematic UI interactions.

## Motion Features

* Smooth page transitions
* Animated vehicle cards
* Multi-step booking transitions
* Modal and drawer animations
* Staggered content reveals
* Availability indicators
* Skeleton loading states
* Hover micro-interactions
* Smooth scroll animations

## Animation Principles

* 60fps optimized animations
* GPU accelerated transforms
* Transform + opacity animations only
* Reduced motion accessibility support
* Zero layout shift interactions
* Scroll performance optimization

---

# 🏗️ Architecture Overview

## Frontend Architecture

```bash
src/
├── app/
├── components/
│   ├── ui/
│   ├── booking/
│   ├── vehicles/
│   ├── dashboard/
│   ├── admin/
│   └── animations/
├── hooks/
├── lib/
├── services/
├── store/
├── styles/
├── types/
└── utils/
```

---

## Backend Architecture

```bash
server/
├── src/
│   ├── controllers/
│   ├── routes/
│   ├── middleware/
│   ├── services/
│   ├── prisma/
│   ├── validators/
│   ├── utils/
│   ├── config/
│   ├── emails/
│   └── jobs/
├── Dockerfile
├── package.json
└── tsconfig.json
```

---

# 🗄️ Database Schema

## User Model

```prisma
model User {
  id           String   @id @default(uuid())
  name         String
  email        String   @unique
  phone        String
  passwordHash String
  role         Role
  createdAt    DateTime @default(now())
  bookings     Booking[]
}
```

---

## Vehicle Model

```prisma
model Vehicle {
  id             String   @id @default(uuid())
  brand          String
  model          String
  year           Int
  category       String
  transmission   String
  fuelType       String
  seats          Int
  pricePerDay    Float
  mileage        Int
  images         String[]
  status         String
  locationId     String
  bookings       Booking[]
}
```

---

## Booking Model

```prisma
model Booking {
  id              String   @id @default(uuid())
  userId          String
  vehicleId       String
  pickupLocation  String
  dropoffLocation String
  pickupDate      DateTime
  returnDate      DateTime
  bookingStatus   String
  totalAmount     Float
  paymentStatus   String

  user            User     @relation(fields: [userId], references: [id])
  vehicle         Vehicle  @relation(fields: [vehicleId], references: [id])
}
```

---

## Payment Model

```prisma
model Payment {
  id               String   @id @default(uuid())
  bookingId        String
  transactionId    String
  paymentProvider  String
  amount           Float
  currency         String
  paymentStatus    String
}
```

---

## Maintenance Model

```prisma
model Maintenance {
  id              String   @id @default(uuid())
  vehicleId       String
  serviceType     String
  serviceDate     DateTime
  nextServiceDate DateTime
  notes           String
}
```

---

# 🔐 Authentication & Security

## Authentication System

* JWT Authentication
* Refresh token support
* Secure password hashing using bcrypt
* Session management
* Role-based access control

## User Roles

* Customer
* Admin
* Fleet Manager

---

## Security Features

### Protection Against

* XSS attacks
* Injection attacks
* API abuse
* Spam submissions
* Unauthorized access

### Security Stack

* Helmet.js
* Rate limiting
* Input sanitization
* Zod validation
* Secure HTTP headers
* CSRF protection
* Environment variable isolation

---

# 🚗 Vehicle Discovery System

## Vehicle Listing Features

* Search vehicles
* Filter by category
* Sort by popularity
* Sort by pricing
* Real-time availability indicators
* Animated hover interactions
* Infinite scroll or pagination
* Optimized image loading

---

# 📅 Booking Workflow

## Multi-Step Reservation Flow

### Step 1

* Pickup location
* Drop-off location
* Pickup date
* Return date

### Step 2

* Vehicle selection
* Insurance options
* Coupon support
* Rental add-ons

### Step 3

* Payment checkout
* Booking confirmation
* Email dispatch
* Receipt generation

---

# 💳 Payment Architecture

Prepared for:

* Stripe
* Razorpay

## Payment Features

* Secure checkout
* Webhook processing
* Refund handling
* Payment tracking
* Transaction logs
* Receipt generation

---

# 📧 Email Notification System

Automated emails are sent for:

* Booking confirmations
* Inquiry submissions
* Rental reminders
* Payment receipts

## Email Stack

* Nodemailer
* SMTP Provider
* Email API integration

---

# 📊 Admin Dashboard

## Admin Controls

* Fleet management
* Booking monitoring
* User management
* Revenue analytics
* Vehicle maintenance schedules
* Availability updates
* Platform analytics

---

# ⚡ Performance Optimization

## Frontend Optimization

* Lazy loading
* Dynamic imports
* Route splitting
* Optimized animations
* Image optimization
* Debounced search
* CDN-ready assets

## Backend Optimization

* Prisma query optimization
* Redis caching
* Horizontal scaling
* API response compression
* Database indexing
* Background job queues

---

# ♿ Accessibility & SEO

## Accessibility

* Keyboard navigation
* Screen-reader support
* Reduced motion accessibility
* Semantic HTML
* ARIA labels
* Focus management

## SEO Features

* Open Graph metadata
* Dynamic meta tags
* Structured heading hierarchy
* Sitemap generation
* Fast Core Web Vitals

---

# 🌍 Deployment

## Supported Deployment Targets

* Vercel
* Docker Containers
* AWS
* DigitalOcean
* Railway

---

# 🐳 Docker Setup

## Build Container

```bash
docker build -t velocity-rentals .
```

## Run Container

```bash
docker run -p 3000:3000 velocity-rentals
```

---

# ⚙️ Environment Variables

Create a `.env` file:

```env
DATABASE_URL=
JWT_SECRET=
JWT_REFRESH_SECRET=
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASSWORD=
STRIPE_SECRET_KEY=
RAZORPAY_KEY_ID=
RAZORPAY_SECRET=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
REDIS_URL=
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/velocity-rentals.git
```

## Install Frontend Dependencies

```bash
npm install
```

## Install Backend Dependencies

```bash
cd server
npm install
```

---

# ▶️ Run Development Server

## Frontend

```bash
npm run dev
```

## Backend

```bash
npm run server
```

---

# 🧪 API Architecture

## REST Endpoints

### Authentication

```bash
POST /api/auth/register
POST /api/auth/login
POST /api/auth/refresh
```

### Vehicles

```bash
GET /api/vehicles
GET /api/vehicles/:id
POST /api/vehicles
PATCH /api/vehicles/:id
DELETE /api/vehicles/:id
```

### Bookings

```bash
POST /api/bookings
GET /api/bookings
PATCH /api/bookings/:id
```

### Payments

```bash
POST /api/payments/create
POST /api/payments/webhook
POST /api/payments/refund
```

---

# 📱 Responsive Design

The platform is fully optimized for:

* Mobile devices
* Tablets
* Desktop systems
* Ultra-wide displays

---
---

# 📄 License

MIT License

---

# 👨‍💻 Author

Durgesh SIngh Chauhan
