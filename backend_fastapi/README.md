# Geo-QR Smart Attendance FastAPI Backend

This folder contains the first backend setup for the Geo-QR Smart Attendance Tracker project.

The backend currently has only beginner-friendly dummy APIs. It does not include a database, real authentication, Flutter code, QR validation, or attendance logic yet.

## Files

- `app/main.py` creates the FastAPI app, adds project metadata, defines the `GET /` health check API, and connects route modules.
- `app/routers/auth.py` defines the dummy `POST /login` API.
- `app/__init__.py` marks the `app` folder as a Python package.
- `app/routers/__init__.py` marks the `routers` folder as a Python package.
- `requirements.txt` lists the Python packages needed to run the backend.

## Setup

Open a terminal in the `backend_fastapi` folder.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the backend:

```bash
python -m uvicorn app.main:app --reload
```

## APIs

### Health Check

Request:

```http
GET /
```

Response:

```json
{
  "message": "Geo-QR Smart Attendance API is running"
}
```

### Dummy Login

Request:

```http
POST /login
```

Response:

```json
{
  "token": "dummy-auth-token",
  "user": {
    "id": 1,
    "name": "Test User"
  }
}
```

## Swagger Docs

After starting the backend, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI also provides ReDoc at:

```text
http://127.0.0.1:8000/redoc
```
