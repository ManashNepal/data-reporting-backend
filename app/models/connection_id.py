from config.database import Base 

from sqlalchemy import Column, String, Text

class ConnectionID(Base):
    __tablename__ = "connection_id"

    connection_name = Column(String(255), unique = True, nullable = False, index = True, primary_key = True)
    connection_id = Column(String(500), unique = True, nullable = False)