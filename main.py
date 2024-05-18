from fastapi import FastAPI
from app.routers.parent_router import router as parent_router
from app.routers.child_router import router as children_router
from app.database.database import engine, Base
from app.models import child_model,parent_model
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/api/v1",debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(parent_router)
app.include_router(children_router)
