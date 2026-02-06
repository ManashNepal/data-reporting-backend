from pydantic import BaseModel, ConfigDict
from typing import Optional

class ConnectionCreate(BaseModel):
    connection_name : str 
    connection_id : str 

class ConnectionUpdate(BaseModel):
    connection_name : Optional[str] = None
    connection_id : Optional[str] = None 

class ConnectionResponse(BaseModel):
    connection_name : str 
    connection_id : str 

    model_config = ConfigDict(from_attributes = True)
