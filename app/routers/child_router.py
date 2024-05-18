from fastapi import APIRouter,Depends,Query,HTTPException
from sqlalchemy.orm import Session
from app.schemas.Schema import ChildSchema
from app.controllers.child_controller import (
    read_many,
    create
)

from app.database.database import get_db

router = APIRouter()

@router.get("/children",status_code=200)
def get_children(db: Session = Depends(get_db),search:str = Query(default='',description='search by children first name'),page:int=Query(default=1,description='page number'),limit:int =Query(default=10,description='how much content should display in first page')):
    try:
        return read_many(db,search,limit,page)
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal Server Error : {str(e)}")

@router.post("/children",status_code=201)
def make_children(children_data:ChildSchema,db: Session = Depends(get_db)):
    try:
        create(db,children_data)
        return {"message" : "Child Successfully Created!"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal Server Error : {str(e)}")
    
    