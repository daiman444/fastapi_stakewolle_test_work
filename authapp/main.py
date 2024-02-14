from fastapi import FastAPI, Response, Request, Header
from fastapi.templating import Jinja2Templates

from api.schemas.pd_models import User, Token


app = FastAPI()
template = Jinja2Templates(directory="public/templates")


@app.get("/")
async def root(request: Request):
    return {"message": "Hello World"}

# TODO from here https://stepik.org/lesson/1044674/step/1?unit=1053248