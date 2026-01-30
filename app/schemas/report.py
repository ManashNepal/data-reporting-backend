from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Dict, Any 

class ReportCreate(BaseModel):
    title : str 
    description : Optional[str] = None 
    type : str
    interval : str
    status : str
    params: Optional[List[Dict[str, Any]]] = None

class ReportResponse(BaseModel):
    id : int 
    title : str 
    description : Optional[str] = None

    type : str 
    interval : str 
    status : str 
    slug : str

    params : Optional[List[Dict[str, Any]]] = None

class ReportUpdate(BaseModel):
    title : Optional[str] = None  
    description : Optional[str] = None

    type : Optional[str] = None 
    interval : Optional[str] = None 
    status : Optional[str] = None 
    slug : Optional[str] = None

    params : Optional[List[Dict[str, Any]]] = None

class ReportColumnCreate(BaseModel):
    name : str 
    description : Optional[str] = None 
    status : str 
    query : Optional[str] = None 
    connection_id : str 
    params : Optional[List[Dict[str, Any]]] = None

class ReportColumnUpdate(BaseModel):
    name : Optional[str] = None
    description : Optional[str] = None 
    status : Optional[str] = None 
    query : Optional[str] = None 
    connection_id : Optional[str] = None 
    params : Optional[List[Dict[str, Any]]] = None

    