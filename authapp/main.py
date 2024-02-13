import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.schemas.settings import settings



app = FastAPI()
app.mount("/static", StaticFiles(directory="public/templates", html=True))


@app.get(f"/{settings.APP_PATH}")
async def root():
    return {"message": "Hello World"}