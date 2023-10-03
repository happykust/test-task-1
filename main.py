from fastapi import FastAPI
from db import engine
from models import User

from api.users import router as users_router
from api.bookings import router as bookings_router

app = FastAPI()

app.include_router(users_router)
app.include_router(bookings_router)


@app.on_event("startup")
def start():
    User.metadata.create_all(engine)
