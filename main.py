import jwt

from fastapi import FastAPI, Response, Request, Header
from fastapi.templating import Jinja2Templates

from api.schemas.pd_models import User, Token
from db.db_models import Users, Token
from db_repo.user_repo import UserRepo

user_repo = UserRepo()

async def users_data_list():
    users_data = await user_repo.get_all_users()
    return users_data
            


app = FastAPI()
template = Jinja2Templates(directory="public/templates")


@app.get("/")
async def root(request: Request):
    values = request.headers.values()
    print(values[0])
    return {"message": "Hello World",}

# TODO from here https://stepik.org/lesson/1044674/step/1?unit=1053248