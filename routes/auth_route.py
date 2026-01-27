from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse, UserCreate
from config.database import get_db
from sqlalchemy.orm import Session
from app.auth.auth_controller import signup_controller, login_controller

router = APIRouter(prefix = "auth")

@router.post("/signup", response_model = UserResponse)
def signup(payload : UserCreate, db : Session = Depends(get_db)):
    return signup_controller(db, payload)

@router.get("/login", response_model = UserResponse)
def login(payload : UserCreate, db : Session = Depends(get_db)):
    return login_controller(db, payload)