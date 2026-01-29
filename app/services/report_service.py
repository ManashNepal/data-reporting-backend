from app.schemas.report import ReportCreate
from app.models.reports import Reports
from config.utils import generate_slug

from sqlalchemy.orm import Session

# CREATE
def create_report_service(db: Session, payload: ReportCreate, user_id : int):
    report = Reports(
        user_id = user_id,
        title = payload.title,
        description = payload.description,
        type = payload.type,
        interval = payload.type,
        status = payload.status,
        slug = generate_slug(payload.title)
    )
    db.add(report)
    db.commit()
    db.refresh(report)

    return report

# READ
def get_my_reports(db : Session, user_id : int):
    return db.query(Reports).filter(Reports.user_id == user_id).all()

def get_report_by_id(db : Session, user_id : int, report_id : int):
    return db.query(Reports).filter(
        Reports.id == report_id,
        Reports.user_id == user_id
    ).first()

# UPDATE
def update_report(db, report_id, user_id, payload):
    report = db.query(Reports).filter(
        Reports.id == report_id,
        Reports.user_id == user_id
    ).first()
    
    if not report:
        return None 
    
    for key, value in payload.dict(exclude_unset = True).items():
        setattr(report, key, value)
    
    db.commit()
    db.refresh(report)
    return report

# DELETE
def delete_report(db, report_id, user_id):
    report = db.query(Reports).filter(
        Reports.id == report_id,
        Reports.user_id == user_id
    ).first()

    if not report:
        return None

    db.delete(report)
    db.commit()