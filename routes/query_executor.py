from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from app.auth.dependencies import get_current_user
from app.controller.report_execution_controller import execute_report_column_controller

router = APIRouter(tags = ["Report Execution"])

@router.post("/reports/{report_id}/columns/{column_id}/execute")
def execute_single_report_column(report_id : int, column_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return execute_report_column_controller(db, report_id, column_id, current_user)