from fastapi import APIRouter,Depends,HTTPException,Query,Body
from sqlalchemy.orm import Session
from app.controllers.parent_controller import (
    create,
    read_many,
    update_one
)

from app.database.database import get_db
from app.schemas.Schema import ParentSchema,ParentUpdateSchema

router = APIRouter()

@router.post("/parents",status_code=201)
def create_parent(parent_data:ParentSchema,db:Session = Depends(get_db)):
    try:
        create(db,parent_data)
        return {"message" : "Parent Successfully Created!"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal Server Error : {str(e)}")

@router.get("/parents")
def get_parents(db:Session=Depends(get_db),search:str = Query(default='',description='search by first name'),page:int = Query(default=1,description='page number'),limit:int =  Query(default=10,description='how much content should display in the first page')):
    try:
        parents = read_many(db,search,limit,page)
        return {'status': 'success', 'meta': {'limit' : limit,'page':page}, 'results': len(parents), 'data': parents}

    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal Server Error : {str(e)}")

@router.put("/parents/{parent_id}")
def update_parent(parent_id:int,parent_data: ParentUpdateSchema = Body(...), db:Session=Depends(get_db)):
    try:
    
        updated = update_one(db,parent_id,parent_data)
        return {'status': 'updated','data': updated}
        
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal Server Error : {str(e)}")


