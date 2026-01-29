from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from app.schemas.report import ReportCreate, ReportResponse, ReportUpdate
from app.auth.dependencies import get_current_user
from app.controller.report_controller import (
    create_report_controller, 
    get_report_controller, 
    get_report_by_id_controller, 
    update_report_controller,
    delete_report_controller)

router = APIRouter()

# CREATE
@router.post("/reports", response_model = ReportResponse)
def create_report(payload: ReportCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    report = create_report_controller(db, payload.dict(), current_user)
    return report

# READ
@router.get("/reports", response_model = list[ReportResponse])
def get_reports(db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    report = get_report_controller(db, current_user)
    return report

@router.get("/reports/{report_id}", response_model = ReportResponse)
def get_report_by_id(report_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_report_by_id_controller(db, current_user, report_id)

# UPDATE
@router.put("/reports/{report_id}", response_model = ReportResponse)
def update_report(report_id : int, payload : ReportUpdate, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_report_controller(db, report_id, current_user, payload)

# DELETE
@router.default("/reports/{report_id}")
def delete_report(report_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_report_controller(db, report_id, current_user)