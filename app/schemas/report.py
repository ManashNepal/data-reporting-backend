from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Dict, Any 

# Base Schema
class ReportBase(BaseModel):
    title: str 
    description: Optional[str] = None 
    type: str 
    interval: str 
    status: str 
    slug: str 
    params: Optional[List[Dict[str, Any]]] = None

class RequestSchema(ReportBase):
    pass 

class ResponseSchema(ReportBase):
    id: int 

    model_config = ConfigDict(from_attributes=True)
    