from fastapi import FastAPI
from app.routers.parent_router import router as parent_router

app = FastAPI(root_path="/api/v1")

app.include_router(parent_router)
