from redis.asyncio import Redis
from api.schemas.settings import settings

redis_app = Redis.from_url(settings.REDIS_URL.unicode_string(), 
                           auto_close_connection_pool=True)