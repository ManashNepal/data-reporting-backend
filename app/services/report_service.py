from app.models.reports import Reports
from sqlalchemy.orm import Session

def create_report(db: Session, data: dict):
    report = Reports(**data)

    db.add(report)
    db.commit()

    return report 
