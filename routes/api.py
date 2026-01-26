from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from app.schemas.report import RequestSchema, ResponseSchema
from app.controller.report_controller import create_report_controller

router = APIRouter()

@router.post("/report", response_model=ResponseSchema)
def create_report(payload: RequestSchema, db: Session = Depends(get_db)):
    report = create_report_controller(db, payload.dict())
    return report