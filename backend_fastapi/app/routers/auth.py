from fastapi import APIRouter


router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login():
    """Return a temporary dummy login response for early API testing."""
    return {
        "token": "dummy-auth-token",
        "user": {
            "id": 1,
            "name": "Test User",
        },
    }
