from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class QueryRequest(BaseModel):
    query : str = None
    params : Dict[str, Any] = Field(default_factory=dict) 
    connection_id : str
    