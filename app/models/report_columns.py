from config.database import Base 
from sqlalchemy import Column, Integer, String, Text, JSON 

class Report_Columns(Base):
    __tablename__ = "report_columns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    status = Column(String(50))
    query = Column(Text)
    
    connection_id = Column(String(255))
    params = Column(JSON, nullable=True)

