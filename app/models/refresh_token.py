from config.database import Base 
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id = Column(Integer, primary_key = True, index = True)
    token = Column(String(512), nullable = False, unique = True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete = "CASCADE"), 
        nullable = False,
        index = True
    )

    expires_at = Column(DateTime, nullable = False)
    created_at = Column(DateTime, nullable = False, default = datetime.utcnow)