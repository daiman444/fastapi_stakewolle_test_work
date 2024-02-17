import pickle

from api.schemas.settings import settings
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
    def __init__(self):
        ...
        
    async def add_user(self, user_data: Users):
        async with a_session() as session:
            try:
                session.add(user_data)
                await session.commit()
                await session.refresh(user_data)
                await redis_app.set(f"id:{user_data.id}", pickle.dumps(user_data))
                return True
            except Exception as e:
                print(e)               
                return False
            
            
    async def get_user(self, user_id: Users):
        user_cache = await redis_app.get(f"id:{user_id}")
        if user_cache:
            return pickle.loads(user_cache)
        
        async with a_session() as session:
            select_result = await session.execute(
                select(Users).where(Users.id == user_id )
            )
            
            user_data = select_result.first()
            return user_data
        
        
    async def get_all_users(self):
        async with a_session() as session:
            select_result = await session.execute(
                select(Users)
            )
            
            users_data = select_result.scalars().all()
            
            if users_data:
                return [(user.id, user.login, user.email) for user in users_data]
            else:
                return None
        
            
            