from sqlalchemy import Column, String, Integer, Boolean, DateTime
from config.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, index = True, primary_key = True)
    email = Column(String(100), nullable = False, unique = True, index = True)
    hashed_password = Column(String(255), nullable = False)
        
    role = Column(String(20), nullable = False, default = "user") # User | Admin
    is_active = Column(Boolean, nullable = False, default = True)
    created_at = Column(DateTime, nullable = False, default = datetime.utcnow)


