from pydantic import BaseModel, ConfigDict, StringConstraints, Field
from typing import List, Optional, Dict, Any
from typing_extensions import Annotated  
from config.validation import (
    ReportType,
    ReportInterval,
    ReportStatus
)

TitleStr = Annotated[
    str, 
    StringConstraints(min_length = 3, max_length = 255)
]

NameStr = Annotated[
    str, 
    StringConstraints(min_length = 3, max_length = 255)
]

DescriptionStr = Annotated[
    str, 
    StringConstraints(max_length = 1000)
]

class ReportCreate(BaseModel):
    title : TitleStr 
    description : Optional[DescriptionStr] = None 
    type : ReportType
    interval : ReportInterval
    status : ReportStatus
    params: Optional[Dict[str, Any]] = None

class ReportResponse(BaseModel):
    id : int 
    title : TitleStr 
    description : Optional[DescriptionStr] = None

    type : ReportType 
    interval : ReportInterval 
    status : ReportStatus 
    slug : str

    params : Optional[Dict[str, Any]] = None

    model_config = ConfigDict(from_attributes = True)

class ReportUpdate(BaseModel):
    title : Optional[TitleStr] = None  
    description : Optional[DescriptionStr] = None

    type : Optional[ReportType] = None 
    interval : Optional[ReportInterval] = None 
    status : Optional[ReportStatus] = None

    params : Optional[Dict[str, Any]] = None

class ReportColumnCreate(BaseModel):
    name : NameStr 
    description : Optional[DescriptionStr] = None 
    status : ReportStatus 
    query : Optional[str] = None 
    connection_id : str 

class ReportColumnUpdate(BaseModel):
    name : Optional[NameStr] = None
    description : Optional[DescriptionStr] = None 
    status : Optional[ReportStatus] = None 
    query : Optional[str] = None 
    connection_id : Optional[str] = None 

class ReportColumnResponse(BaseModel):
    id : int 
    name : NameStr 
    description : Optional[DescriptionStr] = None 
    status : ReportStatus
    query : Optional[str] = None 
    connection_id : Optional[str] = None 

    model_config = ConfigDict(from_attributes = True) 

    
    
    