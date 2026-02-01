from fastapi import HTTPException, status

from app.services.report_service import (
    create_report_service, get_my_reports, 
    get_report_by_id, 
    update_report, 
    delete_report)

# CREATE
def create_report_controller(db, payload, current_user):
    return create_report_service(db, payload, current_user.id)  

# READ
def get_report_controller(db, current_user, limit, offset):
    return get_my_reports(db, current_user.id, limit, offset)

def get_report_by_id_controller(db, current_user, report_id):
    report = get_report_by_id(db, current_user, report_id)
    if not report:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report not Found"
        )
    return report

# UPDATE
def update_report_controller(db, report_id, current_user, payload):
    report = update_report(db, report_id, current_user.id, payload)

    if report is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report not Found"
        )
    
    return report

# DELETE
def delete_report_controller(db, report_id, current_user):
    report = delete_report(db, report_id, current_user.id)

    if report == "NO REPORT":
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report not Found"
        )
    
    return {
        "detail" : "Report deleted successfully"
    }