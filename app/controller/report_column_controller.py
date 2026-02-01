from fastapi import HTTPException, status 

from app.services.report_column_service import (
    create_report_column, 
    read_report_column,
    get_report_column_by_id,
    update_report_column,
    delete_report_column
)
from config.utils import get_owned_column

# CREATE
def create_report_column_controller(db, payload, current_user, report_id):
    column = create_report_column(db, payload, report_id, current_user.id)

    if column is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report not found"
        )
    
    return column

# READ
def read_report_column_controller(db, report_id, current_user, limit, offset):
    report_column = read_report_column(db, report_id, current_user.id, limit, offset)

    if report_column is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report column not found"
        )
    
    return report_column

def read_report_column_by_id_controller(db, report_id, column_id, current_user):
    report_column = get_report_column_by_id(db, report_id, current_user.id, column_id)

    if report_column is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report column not found"
        )
    
    return report_column

# UPDATE
def update_report_column_controller(db, payload, report_id, column_id, current_user):
    column = get_owned_column(db, current_user.id, report_id, column_id)

    if not column:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report Column not found"
        )
    
    return update_report_column(db, column, payload)

# DELETE
def delete_report_column_controller(db, report_id, column_id, current_user):
    column = get_owned_column(db, current_user.id, report_id, column_id)

    if not column:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report Column not found"
        )
    
    delete_report_column(db, column)

    return {
        "detail" : "Report Column successfully deleted"
    }
