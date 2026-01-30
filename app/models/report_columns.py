from config.database import Base 
from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey 

class ReportColumn(Base):
    __tablename__ = "report_columns"

    id = Column(Integer, primary_key=True, index=True)

    report_id = Column(Integer, ForeignKey("reports.id", ondelete = "CASCADE"), nullable = False, index = True) 

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    status = Column(String(50))
    query = Column(Text)
    
    connection_id = Column(String(255))

