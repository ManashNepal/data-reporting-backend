import re
from uuid import uuid4

from app.models.reports import Reports
from app.models.report_columns import ReportColumn

def generate_slug(title: str) -> str:
    base = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
    return f"{base}-{uuid4().hex[:8]}"

def get_owned_report(db, report_id, user_id):
    report = db.query(Reports).filter(
        Reports.id == report_id,
        Reports.user_id == user_id
    ).first()
    return report

def get_owned_column(db, user_id, report_id, column_id):
    report = db.query(ReportColumn).join(Reports, ReportColumn.report_id == Reports.id).filter(
        ReportColumn.id == column_id,
        ReportColumn.report_id == report_id,
        Reports.user_id == user_id
    ).first()

    return report
