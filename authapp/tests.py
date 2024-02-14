import asyncio
from api.schemas.settings import settings

from db.db_models import Users, Token
from db.db_session import a_session
from db.redis import redis_app
from db_repo import UserRepo

user_repo = UserRepo()

async def add_user():
    user_data = Users(
        login="ddd",
        email="ddd@ddd.xyz",
        # pass_hash="123123123",
        tokens=[],
    )
    user_data.set_pass_hash("123123123123")
    result = await user_repo.add_user(user_data=user_data)
    print(result)
    
    
async def get_user(user_id: int):
    result: Users = await user_repo.get_user(user_id=user_id)
    print(result.id, result.login, result.email, result.pass_hash, result.get_pass("123123123123"))
    
    
async def main():
    await add_user()
    await get_user(32)

    
if __name__ == "__main__":
    asyncio.run(main())