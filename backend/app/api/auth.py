from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.db.database import get_db
from app.db import models
from app.schemas.auth_schemas import SignupSchema, LoginSchema, ForgotPasswordSchema
from app.core.security import create_access_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/signup")
def signup(data: SignupSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pwd = pwd_context.hash(data.password)
    new_user = models.User(
        fullname=data.fullname,
        email=data.email,
        password=hashed_pwd,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Account created successfully"}


@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not pwd_context.verify(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid login credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "user": user.fullname}


@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Email not found")

    # Normally send email — skipping
    return {"message": "Password reset link sent!"}