from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime

from config.database import get_db
from app.auth.security import ALGORITHM, SECRET_KEY
from app.models.user import User
from app.models.refresh_token import RefreshToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/login")
# refresh_token_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/refresh")

def get_current_user(db : Session = Depends(get_db), token : str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Invalid Token"
            )    
    except JWTError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid or expired token"
        )
    
    user = db.query(User).filter(User.id == int(user_id)).first()
    
    if not user or not user.is_active:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "User not found or inactive"
        )
    
    return user

def require_admin(current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Admin access required"
        )
    return current_user

def verify_refresh_token(token: str, db: Session):
    refresh_token = db.query(RefreshToken).filter(
        RefreshToken.token == token
    ).first()

    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )

    if refresh_token.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token expired"
        )

    return refresh_token



