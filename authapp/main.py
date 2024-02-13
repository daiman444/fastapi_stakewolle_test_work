import os

from fastapi import FastAPI

from api.schemas.settings import settings



app = FastAPI()


@app.get(f"/{settings.APP_PATH}")
async def root():
    return {"message": "Hello World"}