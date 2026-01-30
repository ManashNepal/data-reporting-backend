from config.database import Base 

from sqlalchemy import Column, Integer, DateTime, String, Text, JSON, ForeignKey
from datetime import datetime

class Reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key = True, index = True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False, index = True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable = True)
    
    type = Column(String(50)) # realtime | cached
    interval = Column(String(50)) # hourly | daily | monthly | annually
    status = Column(String(50))
    
    slug = Column(String(255), unique=True, index=True)
    params = Column(JSON, nullable=True)

    created_at = Column(DateTime, default = datetime.utcnow)