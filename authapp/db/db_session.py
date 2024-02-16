from api.schemas.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


a_engine = create_async_engine(url=settings.SQLALCHEMY_DB_URL.unicode_string(), 
                                   echo=False)
a_session = async_sessionmaker(bind=a_engine)
