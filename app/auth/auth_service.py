from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.auth.security import hash_password, verify_password


def create_user(db : Session, user_data : UserCreate):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    
    if existing_user:
        return None
    # no existing user with such mail
    password_hash = hash_password(user_data.password)
    new_user = User(
        email = user_data.email,
        hashed_password = password_hash
    )                                                                
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

def login(db : Session, user_data: UserLogin):
    existing_user = db.query(User).filter(User.email == user_data.email).first()

    if not existing_user:
        return "NOT_REGISTERED" 
    
    user_entered_password = user_data.password
    stored_password = existing_user.hashed_password
    
    is_valid_password = verify_password(user_entered_password, stored_password)

    if not is_valid_password:
        return "INVALID_PASSWORD"
    
    return existing_user

       