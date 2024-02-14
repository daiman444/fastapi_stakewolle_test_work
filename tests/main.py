import pytest
from asynctest import CoroutineMock, MagicMock

from authapp.db_repo import UserRepo
from authapp.db.db_session import a_session
from authapp.db.redis import redis_app


@pytest.mark.asyncio
async def test_add_user():
    user_data = MagicMock()
    session = CoroutineMock()
    redis_app = MagicMock()
    
    user_repo = UserRepo()
    
    user_repo.
    
    
