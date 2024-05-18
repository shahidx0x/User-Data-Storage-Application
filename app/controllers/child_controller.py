from sqlalchemy.orm import Session
from app.models.child_model import Child
from app.schemas.Schema import ChildSchema
from app.schemas.Schema import ChildrenUpdateSchema
from app.models.child_model import Child
from app.models.parent_model import Parent


def create(db: Session, child_data: ChildSchema):
    try:
        parent_id = child_data.parent_id
        parent = db.query(Parent).filter(Parent.id == parent_id).first()
        if not parent:
            raise Exception('parent not found')
        child_dict = child_data.model_dump()
        new_child = Child(**child_dict, parent=parent)
        db.add(new_child)
        db.commit()
        db.refresh(new_child)
        return new_child

    except Exception as e:
        raise Exception(f"error creating child : {str(e)}")


def read_many(db: Session, search: str, limit: int, page: int):
    skip = (page - 1) * limit
    try:
        children = db.query(Child).filter(
            Child.first_name.contains(search)).limit(limit).offset(skip).all()
        return children
    except Exception as e:
        print(e)
        raise Exception(f"unable to fetch child : {str(e)}")


def update_one(db: Session, children_id: int,
               children_data: ChildrenUpdateSchema):
    try:
        children_query = db.query(Child).filter(Child.id == children_id)
        children = children_query.first()
        if not children:
            raise Exception("children not found")

        updated_data = children_data.model_dump(exclude_unset=True)
        children_query.filter(
            Child.id == children_id).update(
            updated_data,
            synchronize_session=False)
        db.commit()
        db.refresh(children)
        return children

    except Exception as e:
        raise Exception(
            f"unable to update children with id {
                str(children_id)} : {
                str(e)}")


def delete_one(db: Session, children_id: int):
    try:
        parent = db.query(Child).filter(Child.id == children_id).first()
        if not parent:
            raise Exception("children not found")
        db.delete(parent)
        db.commit()
        return True
    except Exception as e:
        raise Exception(
            f"unable to delete children with id {
                str(children_id)} : {
                str(e)}")
