from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse, UserCreate, Token
from config.database import get_db
from sqlalchemy.orm import Session
from app.auth.auth_controller import signup_controller, login_controller, refresh_controller, logout_controller
from app.auth.dependencies import get_refresh_token

router = APIRouter(prefix = "/auth", tags = ["Authentication"])

@router.post("/signup", response_model = UserResponse)
def signup(payload : UserCreate, db : Session = Depends(get_db)):   
    return signup_controller(db, payload)

@router.get("/login", response_model = Token)
def login(payload : UserCreate, db : Session = Depends(get_db)):
    return login_controller(db, payload)

@router.post("/refresh", response_model=Token)
def refresh(db : Session = Depends(get_db), refresh_token_obj = Depends(get_refresh_token)):
    return refresh_controller(db, refresh_token_obj)

@router.post("/logout")
def logout(db : Session = Depends(get_db), refresh_token_obj  = Depends(get_refresh_token)):
    return logout_controller(db, refresh_token_obj)