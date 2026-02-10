from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any

class ReportColumnQueryCreate(BaseModel):
    source_type : str 
    connection_key : str 
    query : Any # str for SQL, list for Mongo and so on  
    database_name : Optional[str] = None 
    collection_name : Optional[str] = None 
    param_mapping : Optional[Dict[str,str]] = None 

class ReportColumnQueryResponse(BaseModel):
    id : int
    source_type : str 
    connection_key : str 
    query : Any
    param_mapping : Optional[Dict[str, str]] = None 

    model_config = ConfigDict(from_attributes = True)

