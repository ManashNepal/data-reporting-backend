from sqlalchemy.orm import Session
from app.services.report_service import create_report

def create_report_controller(db: Session, payload : dict):
    return create_report(db, payload)  
