import pickle

from authapp.api.schemas.settings import settings
from db.redis import redis_app
from db.db_session import a_session
from db.db_models import Users, Token

from sqlalchemy.future import select


class UserRepoInterface:
    async def add_user(self, user_data: Users):
        pass
    
    async def get_user(self, user_id):
        pass
    
    
class UserRepo(UserRepoInterface):
    def __init__(self) -> None:
        ...
        
    async def add_user(self, user_data: Users):
        async with a_session() as session:
            try:
                await session.add(user_data)
                await session.commit()
            except Exception as e:
                print(e)
                

if __name__ == "__main__":
    user_repo = UserRepo()
    user_repo.add_user(
        id=1,
        login="ddd",
        email="ddd@ddd.xyz",
        pass_hash="112233",
    )