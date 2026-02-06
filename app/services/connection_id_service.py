from app.models.connection_id import ConnectionID 

from fastapi import HTTPException, status

# CREATE
def create_connection_id_service(payload, db):
    connection = ConnectionID(
        connection_name = payload.connection_name,
        connection_id = payload.connection_id
    )

    db.add(connection)
    db.commit()
    db.refresh(connection)

    return connection

# READ
def read_connection_id_service(db, connection_name):
    connection = db.query(ConnectionID).filter(
        ConnectionID.connection_name == connection_name
    ).all()

    if not connection:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No connection with such connection name"
        )
    
    return connection

# UPDATE
def update_connection_id_service(payload, db, connection_name):
    connection = db.query(ConnectionID).filter(
        ConnectionID.connection_name == connection_name
    ).first()

    if not connection:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No connection with such connection name"
        )
    
    for key, value in payload.dict(exclude_unset = True).items():
        setattr(connection, key, value)

    db.commit()
    db.refresh(connection)

    return connection

def delete_connection_id_service(db, connection_name):
    connection = db.query(ConnectionID).filter(
        ConnectionID.connection_name == connection_name
    ).first()

    if not connection:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No connection with such connection name"
        )
    
    db.delete(connection)
    db.commit()

