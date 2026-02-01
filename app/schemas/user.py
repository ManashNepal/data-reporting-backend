from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

from config.validation import UserRole

class UserBase(BaseModel):
    email : EmailStr
    password : str

# Signup
class UserCreate(UserBase):
    pass

# Login
class UserLogin(UserBase):
    pass 

class UserResponse(BaseModel):
    id : int 
    email : EmailStr
    role : UserRole 
    is_active: bool

    model_config = ConfigDict(from_attributes = True)

class Token(BaseModel):
    access_token : str 
    refresh_token : Optional[str] = None
    token_type : str

class RefreshTokenRequest(BaseModel):
    refresh_token : str


