from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, Response, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.schemas.models import User, Feedback


app = FastAPI()
template = Jinja2Templates(directory="public/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # return {"message": "Hello World"}
    return template.TemplateResponse("index.html", {"request": request})

# TODO from here https://stepik.org/lesson/1044674/step/1?unit=1053248