from app.services.report_column_queries_services import create_report_column_query, list_report_column_queries
from app.schemas.report_column_query import ReportColumnQueryCreate, ReportColumnQueryResponse
from config.database import get_db

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix = "/reports/{report_id}/columns/{column_id}/queries", tags = ["Report Column Queries"])

@router.post("/", response_model = ReportColumnQueryResponse)
def create_query(report_id : int, column_id : int, payload : ReportColumnQueryCreate, db : Session = Depends(get_db)):
    return create_report_column_query(db, column_id, payload)

@router.get("/", response_model = list[ReportColumnQueryResponse])
def list_queries(report_id : int, column_id : int, db : Session = Depends(get_db)):
    return list_report_column_queries(db, column_id)