# Technical Decisions

## Project Type
Geo-QR Smart Attendance Tracker

## Frontend
Flutter is selected because it supports Android and iOS using a single codebase.

## State Management
Riverpod is selected for predictable state management and better testability.

## Backend
FastAPI is selected because it is lightweight, beginner-friendly, and provides automatic Swagger/OpenAPI documentation.

## Architecture
The Flutter app will follow Clean Architecture.

The backend will follow a modular layered architecture:
Route → Service → Repository → Database

## Storage
Local storage will be used for offline attendance and location records.

## Security
Secrets, API keys, keystore files, and environment files will not be committed to the public repository.
