from app.auth.auth_service import create_user, login
from fastapi import HTTPException, status
from app.auth.security import create_access_token

def signup_controller(db, user_data):
    user = create_user(db, user_data)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email already registered!"
        )
    return user 

def login_controller(db, user_data):
    user = login(db, user_data)

    if user == "NOT_REGISTERED":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email not registered!"
        )
    
    if user == "INVALID_PASSWORD":
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect Password!"
        )

    access_token = create_access_token(
        data = {"sub" : str(user.id)}
    )

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }