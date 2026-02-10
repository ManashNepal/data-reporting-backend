from config.database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey, Text, JSON

class ReportColumnQuery(Base):
    __tablename__ = "report_column_queries"

    id = Column(Integer, primary_key = True, index = True)

    report_column_id = Column(
        Integer,
        ForeignKey("report_columns.id", ondelete = "CASCADE"),
        nullable = False,
        index = True 
    )

    source_type = Column(String(50), nullable = False)
    connection_key = Column(String(255), nullable = False)

    query = Column(JSON, nullable = False)

    database_name = Column(String(255), nullable=True)
    collection_name = Column(String(255), nullable=True)

    param_mapping = Column(JSON, nullable = True) # maps reports.params -> query

    status = Column(String(50), default = "active")
