from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import os 
from dotenv import load_dotenv
import secrets

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)

def hash_password(plain_password : str) -> str:
    return pwd_context.hash(plain_password)

def verify_password(plain_password : str, hashed_password : str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data : dict, expires_delta : timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return encoded_jwt

def create_refresh_token() -> str:
    return secrets.token_urlsafe(64) # 64 bytes token str

def get_refresh_token_expiry():
    return datetime.utcnow() + timedelta(days = REFRESH_TOKEN_EXPIRE_DAYS)