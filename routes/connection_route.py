from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.connection_id import ConnectionCreate, ConnectionResponse, ConnectionUpdate
from config.database import get_db

from app.services.connection_id_service import (
    create_connection_id_service,
    update_connection_id_service,
    read_connection_id_service,
    delete_connection_id_service
)

router = APIRouter(prefix="/connection_id", tags = ["Connection ID"])

# CREATE
@router.post("/", response_model = ConnectionResponse)
def create_connection_id(payload : ConnectionCreate, db : Session = Depends(get_db)):
    return create_connection_id_service(payload, db)

# READ
@router.get("/", response_model = list[ConnectionResponse])
def read_connection_id(connection_name : str, db : Session = Depends(get_db)):
    return read_connection_id_service(db, connection_name)

# UPDATE
@router.put("/", response_model = ConnectionResponse)
def update_connection_id(connection_name : str, payload : ConnectionUpdate, db : Session = Depends(get_db)):
    return update_connection_id_service(payload, db, connection_name)

# DELETE
@router.delete("/")
def deleteconnection_id(connection_name : str, db : Session = Depends(get_db)):
    return delete_connection_id_service(db, connection_name)