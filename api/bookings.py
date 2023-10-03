from fastapi import APIRouter

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("/")
def test():
    return "123"

