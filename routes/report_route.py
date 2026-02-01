from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from config.database import get_db
from app.schemas.report import ReportCreate, ReportResponse, ReportUpdate
from app.schemas.report import ReportColumnCreate, ReportColumnUpdate, ReportColumnResponse
from app.auth.dependencies import get_current_user, require_admin
from app.models.reports import Reports
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

router = APIRouter(tags = ["Reports"])

# CREATE
@router.post("/reports", response_model = ReportResponse)
def create_report(payload: ReportCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    report = create_report_controller(db, payload, current_user)
    return report

# READ
@router.get("/reports", response_model = list[ReportResponse])
def get_reports(limit : int = Query(10, ge = 1, le = 100), offset : int = Query(0, ge = 0), db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    report = get_report_controller(db, current_user, limit, offset)
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
@router.post("/reports/{report_id}/columns", response_model = ReportColumnResponse)
def create_report_column(payload : ReportColumnCreate, report_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_report_column_controller(db, payload, current_user, report_id)

#READ
@router.get("/reports/{report_id}/columns", response_model = list[ReportColumnResponse])
def read_report_column(report_id : int, limit : int  = Query(10, ge = 1, le = 100), offset : int = Query(0, ge = 0), db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return read_report_column_controller(db, report_id, current_user, limit, offset)

# by id
@router.get("/reports/{report_id}/columns/{column_id}", response_model = ReportColumnResponse)
def read_report_column_by_id(report_id : int, column_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return read_report_column_by_id_controller(db, report_id, column_id, current_user)

#UPDATE
@router.put("/reports/{report_id}/columns/{column_id}", response_model = ReportColumnResponse)
def update_report_column(report_id : int, column_id : int, payload : ReportColumnUpdate, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_report_column_controller(db, payload, report_id, column_id, current_user)

#DELETE
@router.delete("/reports/{report_id}/columns/{column_id}")
def delete_report_column(report_id : int, column_id : int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_report_column_controller(db, report_id, column_id, current_user)


# ADMIN - ONLY ROUTES
@router.get("/admin/reports", response_model = list[ReportResponse])
def get_all_reports(limit : int  = Query(10, ge = 1, le = 100), offset : int = Query(0, ge = 0), db : Session = Depends(get_db), admin  = Depends(require_admin)):
    return db.query(Reports).order_by(Reports.id.desc()).offset(offset).limit(limit).all()
