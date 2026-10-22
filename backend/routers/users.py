from fastapi import APIRouter, Depends
from auth import get_current_user
from sqlalchemy.orm import session
from database import get_db
from models import User
from schemas import UserResponse
from auth import create_access_token, get_current_user
import crud
import schemas
import models

router = APIRouter()

@router.post("/register")
def register_user(user:schemas.UserCreate,db:session=Depends(get_db)):
    return crud.create_user(db,user)

@router.post("/login")
def login_user(user:schemas.UserLogin,db:session=Depends(get_db)):
    authenticated_user = crud.user_login(db,user)

    access_token = create_access_token({
        "sub": str(authenticated_user.id)
    })
    return{
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/user/me",response_model=UserResponse)
def read_current_user(current_user:User=Depends(get_current_user)):
    return current_user


