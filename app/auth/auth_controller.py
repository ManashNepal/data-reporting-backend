from app.auth.auth_service import create_user, login
from fastapi import HTTPException, status
from app.auth.security import create_access_token, create_refresh_token, get_refresh_token_expiry
from app.models.refresh_token import RefreshToken
from app.auth.dependencies import verify_refresh_token
from app.schemas.user import UserLogin

def signup_controller(db, user_data):
    user = create_user(db, user_data)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email already registered!"
        )
    return user 

def login_controller(db, form_data):
    user_data = UserLogin(
        email = form_data.username, 
        password = form_data.password
    )

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
    # Access Token (JWT)
    access_token = create_access_token(
        data = {"sub" : str(user.id)}
    )

    refresh_token = create_refresh_token()

    # Store refresh token in DB
    refresh_token_obj = RefreshToken(
        token = refresh_token,
        user_id = user.id,
        expires_at = get_refresh_token_expiry()
    )

    db.add(refresh_token_obj)
    db.commit()

    return {
        "access_token" : access_token,
        "refresh_token" : refresh_token,
        "token_type" : "bearer"
    }

def refresh_controller(db, payload):
    stored_token = verify_refresh_token(payload.refresh_token, db)

    new_access_token = create_access_token(
        data={"sub": str(stored_token.user_id)}
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }

def logout_controller(db, payload):
    refresh_token_obj = verify_refresh_token(
        payload.refresh_token,
        db
    )

    db.delete(refresh_token_obj)
    db.commit()

    return {"message": "Logged out successfully"}
