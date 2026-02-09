from app.models.connection_id import ConnectionID

from fastapi import HTTPException, status
from sqlalchemy import create_engine
from pymongo import MongoClient

def resolve_sql_connection(connection_name, db, user_id):
    connection = db.query(ConnectionID).filter(
        ConnectionID.connection_name == connection_name,
        ConnectionID.user_id == user_id
    ).first()

    if not connection:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Connection not found!"
        )
    
    try:
        engine = create_engine(connection.connection_id)
        return engine 
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Failed to initialize SQL connection!"
        )
    
def resolve_mongo_connection(db, user_id, connection_name, database_name, collection_name):
    connection = db.query(ConnectionID).filter(
        ConnectionID.connection_name == connection_name,
        ConnectionID.user_id == user_id
    )

    if not connection:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Connection not found!"
        )
    
    try:
        client = MongoClient(connection.connection_id)
        return client[database_name][collection_name]
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Failed to initialize MongoDB connection"
        )