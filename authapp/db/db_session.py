from api.schemas.settings import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

a_engine = create_async_engine(url=settings.SQLALCHEMY_DB_URL.unicode_string(), 
                                   echo=False)

async def a_session():
    async_session = async_sessionmaker(bind=a_engine)
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()