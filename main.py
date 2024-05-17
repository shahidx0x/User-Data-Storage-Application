from fastapi import FastAPI
from app.routers.parent_router import router as parent_router
from app.database.database import engine, Base
from app.models import child_model,parent_model

Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/api/v1")

app.include_router(parent_router)
