from fastapi import FastAPI, Request, Cookie
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.schemas.settings import settings
from api.schemas.models import User, Feedback


app = FastAPI()
template = Jinja2Templates(directory="public/templates")

feedback_list = []

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # return {"message": "Hello World"}
    return template.TemplateResponse("index.html", {"request": request})


@app.get("/calculate",)
async def root(request: Request, num1: int, num2: int ):
    # return {"message": "Hello World"}
    result = num1 + num2
    return {"result": result}


@app.post("/user",)
async def root(user: User):
    user_data = user.model_dump()
    if user.age > 18:
        user_data["is_adult"] = True
    else:
        user_data["is_adult"] = False    
    return {"user_data": user_data}


@app.post("/feedback",)
async def root(feedback: Feedback):
    feedback_list.append(feedback)
    print(feedback_list)
    return {"message": "Feedback received"}
