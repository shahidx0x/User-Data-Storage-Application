from sqlalchemy.orm import Session
from fastapi import Body
from app.models.parent_model import Parent
from app.models.child_model import Child
from app.schemas.Schema import ParentSchema, ParentUpdateSchema


def create(db: Session, parent_data: ParentSchema):
    try:
        parent_dict = parent_data.model_dump()
        parent = Parent(**parent_dict)
        db.add(parent)
        db.commit()
        db.refresh(parent)
        return parent
    except Exception as e:
        raise Exception(f"error creating parent : {str(e)}")


def read_many(db: Session, search: str, limit: int, page: int):
    skip = (page - 1) * limit
    try:
        parents = db.query(Parent).options().filter(
            Parent.first_name.contains(search)).limit(limit).offset(skip).all()
        return parents
    except Exception as e:
        print(e)
        raise Exception(f"unable to fetch parents : {str(e)}")


def update_one(db: Session, parent_id: int, parent_data: ParentUpdateSchema):
    print(parent_data.model_dump())
    try:
        parents_query = db.query(Parent).filter(Parent.id == parent_id)
        parents = parents_query.first()
        if not parents:
            raise Exception("parent not found")

        updated_data = parent_data.model_dump(exclude_unset=True)
        parents_query.filter(
            Parent.id == parent_id).update(
            updated_data,
            synchronize_session=False)
        db.commit()
        db.refresh(parents)
        return parents

    except Exception as e:
        raise Exception(
            f"unable to update parent with id {
                str(parent_id)} : {
                str(e)}")


def delete_one(db: Session, parent_id: int):
    try:
        parent = db.query(Parent).filter(Parent.id == parent_id).first()
        if not parent:
            raise Exception("parent not found")
        db.delete(parent)
        db.commit()
        return True
    except Exception as e:
        raise Exception(
            f"unable to delete parent with id {
                str(parent_id)} : {
                str(e)}")
