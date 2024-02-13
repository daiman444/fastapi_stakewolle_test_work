import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.schemas.settings import settings



app = FastAPI()
#app.mount("/static", StaticFiles(directory="public/templates", html=True))
template = Jinja2Templates(directory="public/templates")


@app.get(f"/{settings.APP_PATH}", response_class=HTMLResponse)
async def root(request: Request):
    # return {"message": "Hello World"}
    return template.TemplateResponse("index.html", {"request": request})


@app.get(f"/{settings.APP_PATH}/calculate/",)
async def root(request: Request, num1: int, num2: int ):
    # return {"message": "Hello World"}
    result = num1 + num2
    return {"result": result}