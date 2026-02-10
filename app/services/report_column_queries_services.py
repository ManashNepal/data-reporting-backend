from app.models.report_columns_queries import ReportColumnQuery

def create_report_column_query(db, column_id, payload):
    query = ReportColumnQuery(
        report_column_id = column_id,
        **payload.dict()
    )

    db.add(query)
    db.commit()
    db.refresh(query)

    return query

def list_report_column_queries(db, report_column_id):
    queries = db.query(ReportColumnQuery).filter(
        ReportColumnQuery.report_column_id == report_column_id
    ).all()

    return queries

    