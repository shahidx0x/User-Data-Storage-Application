from sqlalchemy.orm import Session
from app.models.parent_model import Parent

def create(db:Session,parent_data):
    try:
        parent = Parent(**parent_data)
        db.add(parent)
        db.commit()
        db.refresh(parent)
        return parent
    except Exception as e:
        raise Exception(f"Error creating parent : {str(e)}")

def read_parents(db:Session):
    try:
        db.query(Parent).all()
    except Exception as e:
        raise Exception(f"Unable to fetch parents : {str(e)}")

def read_parrent(db:Session,parent_id:int):
    try:
        parent = db.query(Parent).filter(Parent.id == parent_id).first()
        if not parent:
            raise Exception("Parent Not Found")
        return parent
    except Exception as e:
        raise Exception(f"Unable to fetch parent with id {str(parent_id)} : {str(e)}")

def update_parent(db:Session,parent_id:int,parent_data):
    try: 
        parent = db.query(Parent).filter(Parent.id == parent_id).first()
        if not parent:
            raise Exception("Parent Not Found")
        for key,value in parent_data.items():
            setattr(parent,key,value)
        db.commit()
        db.refresh(parent)
        return parent
    except Exception as e:
        raise Exception(f"Unable to update parent with id {str(parent_id)} : {str(e)}")

def delete_parent(db:Session,parent_id:int):
    try:
        parent = db.query(Parent).filter(Parent.id == parent_id).first()
        if not parent:
            raise Exception("Parent Not Found")
        db.delete(parent)
        db.commit()
        return True
    except Exception as e:
        raise Exception(f"Unable to delete parent with id {str(parent_id)} : {str(e)}")




    