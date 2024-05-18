from fastapi import APIRouter, Depends, Query, HTTPException, Body
from sqlalchemy.orm import Session
from app.schemas.Schema import ChildSchema
from app.schemas.Schema import ChildrenUpdateSchema
from app.controllers.child_controller import (
    read_many,
    create,
    delete_one,
    update_one,
)

from app.database.database import get_db

router = APIRouter()


@router.get("/children", status_code=200)
def get_children(db: Session = Depends(get_db), search: str = Query(default='', description='search by children first name'), page: int = Query(
        default=1, description='page number'), limit: int = Query(default=10, description='how much content should display in first page')):
    try:
        childrens = read_many(db, search, limit, page)
        return {'status': 'success', 'meta': {'limit': limit,
                                              'page': page}, 'results': len(childrens), 'data': childrens}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error : {
                str(e)}")


@router.post("/children", status_code=201)
def make_children(children_data: ChildSchema, db: Session = Depends(get_db)):
    try:
        create(db, children_data)
        return {"message": "Child Successfully Created!"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error : {
                str(e)}")


@router.patch("/children/{children_id}")
def update_children(children_id: int, children_data: ChildrenUpdateSchema = Body(...),
                    db: Session = Depends(get_db)):
    try:
        updated = update_one(db, children_id, children_data)
        return {'status': 'updated', 'data': updated}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error : {
                str(e)}")


@router.delete("/children/{children_id}")
def delete_children(children_id: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_one(db, children_id)
        if deleted:
            return {'status': 'deleted', 'id': children_id}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error : {
                str(e)}")
