from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse, UserCreate, Token, RefreshTokenRequest
from config.database import get_db
from sqlalchemy.orm import Session
from app.auth.auth_controller import signup_controller, login_controller, refresh_controller, logout_controller
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix = "/auth", tags = ["Authentication"])

@router.post("/signup", response_model = UserResponse)
def signup(payload : UserCreate, db : Session = Depends(get_db)):   
    return signup_controller(db, payload)

@router.post("/login", response_model = Token)
def login(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    return login_controller(db, form_data)

@router.post("/refresh", response_model=Token)
def refresh(payload: RefreshTokenRequest, db : Session = Depends(get_db)):
    return refresh_controller(db, payload)

@router.post("/logout")
def logout(payload : RefreshTokenRequest , db : Session = Depends(get_db)):
    return logout_controller(db, payload)