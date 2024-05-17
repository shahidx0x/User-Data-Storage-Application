from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.controllers.child_controller import (
    get_children
)

from app.database.database import get_db

router = APIRouter()

@router.get("/children/", response_model=list)
def read_children(db: Session = Depends(get_db)):
    return get_children(db)
