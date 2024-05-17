from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.controllers.parent_controller import (
    create,
    read_parrent,
    read_parents,
    delete_parent,
    update_parent
)

from app.database.database import get_db
from app.models.parent_model import Parent

router = APIRouter()

parent_example = {
    "first_name": "John",
    "last_name": "Doe",
    "address_city": "Anytown",
    "address_zip": "12345",
    "address_street": "123 Main St",
    "address_state": "CA"
}

@router.post("/parents",status_code=201)
def create_parent(parent_data:dict,db:Session = Depends(get_db)):
    try:
        create(db,parent_data)
        return {"message" : "Parent Successfully Created!"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal Server Error : {str(e)}")

@router.get("/parents")
def get_parents(db:Session=Depends(get_db)):
    try:
        parent =  read_parents(db)
        return parent
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal Server Error : {str(e)}")




