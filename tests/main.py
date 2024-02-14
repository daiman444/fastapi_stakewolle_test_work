import asyncio
from authapp.api.schemas.settings import settings

from authapp.db.db_models import Users, Token
from authapp.db.db_session import a_session
from authapp.db.redis import redis_app
from authapp.db_repo import UserRepo

user_repo = UserRepo()

async def add_user():
    user_data = Users(
        id=1,
        login="ddd",
        email="ddd@ddd.xyz",
        pass_hash="123123123",
    )
    

asyncio.run(add_user())