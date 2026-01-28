from pydantic import BaseModel, EmailStr, ConfigDict

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
    role : str 
    isactive: bool

    model_config = ConfigDict(from_attributes = True)

class Token(BaseModel):
    access_token : str 
    token_type : str


