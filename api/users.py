from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import schemas
from db import get_db
from models import User
from datetime import datetime
from api.security import verify_password, get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.CreateUserResponseSchema)
def create_user(data: schemas.CreateUserRequestSchema, db: Session = Depends(get_db)):
    """
    Create new user and return created row
    """
    if db.query(User).filter(User.username == data.username).all():
        raise HTTPException(status_code=409, detail="User with entered username already exist.")
    user = User(
        username=data.username,
        password=get_password_hash(data.password),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, data: schemas.DeleteUserRequestSchema, db: Session = Depends(get_db)):
    """
    Delete existing user
    """
    if user := db.query(User).filter(User.id == user_id).all():
        user = user[0]
    else:
        raise HTTPException(status_code=404, detail="User with entered id not found.")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=403, detail="Wrong password.")
    db.delete(user)
    db.commit()
    return user_id
