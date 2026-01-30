from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from app.schemas.report import ReportCreate, ReportResponse, ReportUpdate
from app.schemas.report import ReportColumnCreate, ReportColumnUpdate
from app.auth.dependencies import get_current_user
from app.controller.report_controller import (
    create_report_controller, 
    get_report_controller, 
    get_report_by_id_controller, 
    update_report_controller,
    delete_report_controller
)

from app.controller.report_column_controller import (
    create_report_column_controller,
    read_report_column_controller,
    read_report_column_by_id_controller,
    update_report_column_controller,
    delete_report_column_controller
)

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
@router.delete("/reports/{report_id}")
def delete_report(report_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_report_controller(db, report_id, current_user)

# ----------------- Report Column ------------------

# CREATE
@router.post("/reports/{report_id}/columns")
def create_report_column(payload : ReportColumnCreate, report_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_report_column_controller(db, payload, current_user, report_id)

#READ
@router.get("/reports/{report_id}/columns")
def read_report_column(report_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return read_report_column_controller(db, report_id, current_user)

@router.get("/reports/{report_id}/columns/{column_id}")
def read_report_column_by_id(report_id : int, column_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return read_report_column_by_id_controller(db, report_id, column_id, current_user)

#UPDATE
@router.put("/report_column/{column_id}")
def update_report_column(column_id : int, payload : ReportColumnUpdate, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_report_column_controller(db, payload, column_id, current_user)

#DELETE
@router.delete("/report_column/{column_id}")
def delete_report_column(column_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_report_column_controller(db, column_id, current_user)
