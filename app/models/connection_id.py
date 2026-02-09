from config.database import Base 

from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, DateTime
from datetime import datetime

class ConnectionID(Base):
    __tablename__ = "connection_id"
    
    id = Column(Integer, primary_key = True, index = True)
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False, index = True)
    
    connection_name = Column(String(255),nullable = False)
    connection_id = Column(String(1024), nullable = False)
    
    __table_args__ = (
        UniqueConstraint(user_id, connection_name, name = "unique_user_connection_name"),   
    )
    
    created_at = Column(DateTime, default = datetime.utcnow) 