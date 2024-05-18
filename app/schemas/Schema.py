from typing import List,Optional
from pydantic import BaseModel, Field


class ChildSchema(BaseModel):
    first_name: str = Field(..., description="The child's first name")
    last_name: str = Field(..., description="The child's last name")
    parent_id: int = Field(..., description="The ID of the parent this child belongs to")

    class Config:
        arbitrary_types_allowed = True 

class ParentSchema(BaseModel):
    first_name: str = Field(..., description="The parent's first name")
    last_name: str = Field(..., description="The parent's last name")
    address_street: str = Field(..., description="The parent's street address")
    address_city: str = Field(..., description="The parent's city")
    address_state: str = Field(..., description="The parent's state")
    address_zip: str = Field(..., description="The parent's zip code")
    children: List[ChildSchema] = Field(default_factory=list, description="List of child objects associated with the parent")

    class Config:
        arbitrary_types_allowed = True

class ParentsDataResponse(BaseModel):
    status:str
    results:int
    data:List[ParentSchema]
    
class ParentUpdateSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    address_street: Optional[str]
    address_city: Optional[str]
    address_state: Optional[str]
    address_zip: Optional[str]

class ChildrenUpdateSchema(BaseModel):
    first_name:Optional[str]
    last_name:Optional[str]
    parent_id:Optional[int]
