from app.schemas.report import ReportCreate
from app.models.reports import Reports
from config.utils import generate_slug
from config.validation import UserRole

from sqlalchemy.orm import Session

# CREATE
def create_report_service(db: Session, payload: ReportCreate, user_id : int):
    report = Reports(
        user_id = user_id,
        title = payload.title,
        description = payload.description,
        type = payload.type,
        interval = payload.interval,
        status = payload.status,
        slug = generate_slug(payload.title),
        params = payload.params
    )
    db.add(report)
    db.commit()
    db.refresh(report)

    return report

# READ
def get_my_reports(db : Session, user_id : int, limit : int, offset : int):
    return db.query(Reports).filter(Reports.user_id == user_id).order_by(Reports.id.desc()).offset(offset).limit(limit).all()

def get_report_by_id(db : Session, current_user, report_id : int):
    query = db.query(Reports).filter(
        Reports.id == report_id
    )

    if current_user.role != UserRole.admin:
        query = query.filter(Reports.user_id == current_user.id)
    
    return query.first()


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
        return "NO REPORT"

    db.delete(report)
    db.commit()