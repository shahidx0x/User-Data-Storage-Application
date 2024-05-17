from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.controllers.parent_controller import (
    create
)

from app.database.database import get_db

router = APIRouter()

@router.post("/parents")
async def create_parent(parent_data:dict,db:Session = Depends(get_db)):
    parent = await create(db,parent_data)
    return parent
