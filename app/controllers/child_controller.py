from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.child_model import Child
from app.models.parent_model import Parent

def get_children(db: Session):
    return db.query(Child).all()