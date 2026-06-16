# Architecture

## 1. System Architecture

The system follows a client-server architecture.

Flutter Mobile App
↓
FastAPI Backend
↓
Database

The Flutter app handles user interaction, QR scanning, location capture, offline storage, and sync.

The backend handles authentication, QR validation, geo-fencing validation, attendance records, and audit trail.

---

## 2. Flutter App Architecture

The Flutter application will follow Clean Architecture with Riverpod.

Layers:

### Presentation Layer
- Screens
- Widgets
- Riverpod Providers
- UI State

### Domain Layer
- Entities
- Use Cases
- Repository Contracts

### Data Layer
- API Services
- Local Database
- Repository Implementations
- Models

Flow:

Screen
↓
Provider
↓
Use Case
↓
Repository
↓
API / Local DB

---

## 3. Backend Architecture

The backend will use FastAPI with a modular structure.

Modules:

- Auth Module
- QR Module
- Attendance Module
- Location Module
- User Module

Backend flow:

API Route
↓
Service Layer
↓
Repository Layer
↓
Database

---

## 4. Database Design

Initial database tables:

- users
- workplaces
- qr_codes
- attendance_records
- location_logs
- sync_queue

---

## 5. Core Flow

User Login
↓
Scan QR Code
↓
Capture Current Location
↓
Validate QR + Location Radius
↓
Mark Check-In
↓
Track Location Every 15 Minutes
↓
Store Offline If No Internet
↓
Auto Sync When Internet Returns
↓
Mark Check-Out
