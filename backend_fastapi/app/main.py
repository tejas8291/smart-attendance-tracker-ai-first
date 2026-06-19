from fastapi import FastAPI

from app.routers import auth


app = FastAPI(
    title="Geo-QR Smart Attendance API",
    description="Backend API for the Geo-QR Smart Attendance Tracker project.",
    version="0.1.0",
)


@app.get("/")
def health_check():
    """Return a simple message to confirm that the API server is running."""
    return {"message": "Geo-QR Smart Attendance API is running"}


app.include_router(auth.router)
