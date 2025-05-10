from fastapi import FastAPI
from app.infrastructure.controller import controller

app = FastAPI()
app.include_router(controller.router, prefix="/api", tags=["countries"])