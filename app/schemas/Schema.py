from typing import List
from pydantic import BaseModel, Field
from app.models.child_model import Child  

class ParentSchema(BaseModel):
    id: int = Field(..., description="The unique identifier of the parent")
    first_name: str = Field(..., description="The parent's first name")
    last_name: str = Field(..., description="The parent's last name")
    address_street: str = Field(..., description="The parent's street address")
    address_city: str = Field(..., description="The parent's city")
    address_state: str = Field(..., description="The parent's state")
    address_zip: str = Field(..., description="The parent's zip code")
    children: List[Child] = Field(default_factory=list, description="List of child objects associated with the parent")

    class Config:
        orm_mode = True 

class ParentsDataResponse(BaseModel):
    status:str
    results:int
    data:List[ParentSchema]
    

class ChildSchema(BaseModel):
    id: int = Field(..., description="The unique identifier of the child")
    first_name: str = Field(..., description="The child's first name")
    last_name: str = Field(..., description="The child's last name")
    parent_id: int = Field(..., description="The ID of the parent this child belongs to")

    class Config:
        orm_mode = True  
