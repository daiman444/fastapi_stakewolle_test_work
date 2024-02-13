from datetime import datetime

from fastapi import FastAPI, Response, Request, Cookie, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.schemas.settings import settings
from api.schemas.models import User, Feedback


app = FastAPI()
template = Jinja2Templates(directory="public/templates")


user_data = User(
    id=2,
    name="Vasyan",
    password=123,
    age=20
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # return {"message": "Hello World"}
    return template.TemplateResponse("index.html", {"request": request})


@app.get("/login")
async def login(response: Response, usermane: str, userpassword: int):
    if usermane == user_data.name:
        if userpassword == user_data.password:
            now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            response.set_cookie(key="set_time", value=now)
            return {"message": "coockies are set"}
        else:
            return {"message": "invelid passowrd"}
    else:
        return {"message": "user is not found"}
        


@app.get("/user")
async def user(set_time = Cookie(default=None)):
    if set_time is None:
        HTTPException(status_code=401, detail="you needed to signin or signup")
    else:
        user_info = {
            "user id": user_data.id,
            "user name": user_data.name,
            "user age": user_data.age,
        }
        return {
            "user info": user_info,
            "set_time": set_time,
        }
    
    
@app.post("/signout", status_code=204)
async def logout(response: Response):
    response.delete_cookie("set_time")
    return {"message": "you have left the session"}
