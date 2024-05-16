from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.controllers.parent_controller import (
    create_parent
)

from app.database.database import get_db

router = APIRouter()

@router.post("/parents")
def create_parent(parent_data:dict,db:Session = Depends(get_db)):
    return create_parent(db,parent_data)
