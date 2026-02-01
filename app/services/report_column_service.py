from config.utils import get_owned_report
from app.models.report_columns import ReportColumn 

# CREATE
def create_report_column(db, payload, report_id, user_id):
    report = get_owned_report(db, report_id, user_id)

    if not report:
        return None 
    
    column = ReportColumn(
        report_id = report.id,
        **payload.dict()
    )

    db.add(column)
    db.commit()
    db.refresh(column)

    return column

# READ
def read_report_column(db, report_id, user_id, limit, offset):
    report = get_owned_report(db, report_id, user_id)

    if not report:
        return None 
    
    report_column = db.query(ReportColumn).filter(
        ReportColumn.report_id == report.id
    ).order_by(ReportColumn.id.desc()).offset(offset).limit(limit).all()

    return report_column

def get_report_column_by_id(db, report_id, user_id, column_id):
    report = get_owned_report(db, report_id, user_id)

    if not report:
        return None 
    
    report_column = db.query(ReportColumn).filter(
        ReportColumn.report_id == report_id,
        ReportColumn.id == column_id
    ).first()

    return report_column

# UPDATE
def update_report_column(db, column, payload):
    for key, value in payload.dict(exclude_unset = True).items():
        setattr(column, key, value)
    
    db.commit()
    db.refresh(column)

    return column

# DELETE
def delete_report_column(db, column):
    db.delete(column)
    db.commit()
