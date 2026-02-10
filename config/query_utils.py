from sqlalchemy import text
import json

from app.services.connection_resolver import resolve_sql_connection, resolve_mongo_connection

def execute_sql_metric(db, user_id, connection_name, query, params):
    engine = resolve_sql_connection(connection_name, db, user_id)

    with engine.connect() as conn:
        result = conn.execute(text(query), params)
        return result

def inject_mongo_params(pipeline, params):
    pipeline_str = json.dumps(pipeline)

    for key, value in params.items():
        pipeline_str = pipeline_str.replace(f"${key}", json.dumps(value))
    
    return json.loads(pipeline_str)

def execute_mongo_metric(db, user_id, connection_name, database, collection, pipeline, params):
    collection = resolve_mongo_connection(db, user_id, connection_name, database, collection)

    pipeline = inject_mongo_params(pipeline, params)
    result = list(collection.aggregate(pipeline))

    return result[0]["total"] if result else 0


