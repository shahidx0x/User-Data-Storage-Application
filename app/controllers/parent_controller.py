from sqlalchemy.orm import Session
from app.models.parent_model import Parent


def create(db:Session,parent_data):
    parent = Parent(**parent_data)
    db.add(parent)
    db.commit()
    db.refresh(parent)
    return parent



    