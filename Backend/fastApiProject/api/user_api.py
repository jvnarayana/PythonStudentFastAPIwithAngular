from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
import jwt
from ..services.auth_service import create_jwt_token, verify_jwt_token
from datetime import datetime, timedelta
from ..repository.user_repository import UserRepository
from ..Schemas.user import User as UserSchema
from ..models.User import User as UserModel
from ..dbConfig.db import get_db
from ..dbConfig.config import Settings

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register")
async def register_user(user: UserSchema, db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    existing_user = await user_repo.get_user_by_username(user.username)

    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    password_hash = pwd_context.hash(user.password)
    user = UserModel(username=user.username, password_hash=password_hash)
    await user_repo.create_user(user)
    return "User created successfully"


@router.get("/login")
async def login_user(username: str, password: str, db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    user = await user_repo.get_user_by_username(username)
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_jwt_token(user)
    return {"token": token}
