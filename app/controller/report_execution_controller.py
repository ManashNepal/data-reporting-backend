from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException, status
import json

from app.models.reports import Reports
from app.models.report_columns import ReportColumn
from app.models.report_columns_queries import ReportColumnQuery
from app.services.connection_resolver import resolve_sql_connection, resolve_mongo_connection

def resolve_query_params(report_params : dict, param_mapping : dict | None):
    if not param_mapping:
        return {}
    
    resolved = {}

    for query_param, report_param in param_mapping.items():
        resolved[query_param] = report_params.get(report_param)
    
    return resolved

def inject_params(obj, params):
    if isinstance(obj, dict):
        return {
            k: inject_params(v, params)
            for k, v in obj.items()
        }
    elif isinstance(obj, list):
        return [inject_params(i, params) for i in obj]
    elif isinstance(obj, str) and obj.startswith("$"):
        return params.get(obj[1:], obj)
    else:
        return obj


def execute_report_column_controller(db : Session, report_id : int, column_id : int, current_user):
    # Load report
    report = db.query(Reports).filter(
        Reports.id == report_id,
        Reports.user_id == current_user.id
    ).first()

    if not report:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report not found"
        )
    
    # Load column
    column = db.query(ReportColumn).filter(
        ReportColumn.id == column_id,
        ReportColumn.report_id == report.id
    ).first()


    if not column:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Report Column not found"
        )
    
    
    queries = db.query(ReportColumnQuery).filter(
        ReportColumnQuery.report_column_id == column.id
    ).all()

    if not queries:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No queries defined for this column"
        )
    
    output = {}

    for q in queries:
        params = resolve_query_params(report.params or {}, q.param_mapping)

        if q.source_type == "mysql":
            engine = resolve_sql_connection(db, current_user.id, q.connection_key)

            with engine.connect() as conn:
                value = conn.execute(text(q.query), params).scalar()

        elif q.source_type == "mongodb":
            collection = resolve_mongo_connection(
                db,
                current_user.id,
                q.connection_key,
                q.database_name,
                q.collection_name
            )

            pipeline = inject_params(q.query, params)

            result = list(collection.aggregate(pipeline))
            value = result[0]["total"] if result else 0

        else:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Unsupported source type!"
            )
        
        output[q.connection_key] = value
        
    return {
        "column" : column.name,
        "result" : output 
    } 

